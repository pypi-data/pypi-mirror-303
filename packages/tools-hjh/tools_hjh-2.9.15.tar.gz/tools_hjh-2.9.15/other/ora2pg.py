# coding:utf-8
from tools_hjh import DBConn, Tools, ProcessPool
from tools_hjh.Tools import locatdate
from tools_hjh import Log
from tools_hjh import ThreadPool
from tools_hjh import OracleTools
import time
import gc
from math import ceil
import sys
import uuid

date = locatdate().replace('-', '')

try:
    run_mode = sys.argv[2]
except:
    run_mode = None
try:
    config_file = sys.argv[1]
except:
    config_file = None
try:
    log_file = sys.argv[3]
except:
    log_file = date + '.log'
    
if config_file == None or config_file == 'help':
    print('python3 ora2pg.py xxx.conf mode_type xxx.log')
    print('mode_type: copy, report, compare_index, compare_constraint')
    print('xxx.log: default value YYYY-MM-DD.log')
    sys.exit()

Tools.rm(log_file)
log = Log(log_file)

conf = Tools.cat(config_file)
conf_map = {}
for line in conf.split('\n'):
    if '=' in line and '#' not in line:
        key = line.split('=', 1)[0].strip()
        val = line.split('=', 1)[1].strip()
        conf_map[key] = val

forever_number_to_numeric = conf_map['forever_number_to_numeric']
if forever_number_to_numeric == 'true':
    forever_number_to_numeric = True
else:
    forever_number_to_numeric = False

smallest_object = conf_map['smallest_object']
if_truncate = conf_map['if_truncate']
if_only_scn = conf_map['if_only_scn']

src_db_type = conf_map['src_db_type']
src_ip = conf_map['src_ip']
src_port = int(conf_map['src_port'])
src_database = conf_map['src_db']
src_read_username = conf_map['src_read_username']
src_read_password = conf_map['src_read_password']
# src_schema = conf_map['src_schema']

tables = conf_map['tables']
exclude_tables = conf_map['exclude_tables']
sqls = conf_map['copy_from_sql']

dst_db_type = conf_map['dst_db_type']
dst_ip = conf_map['dst_ip']
dst_port = int(conf_map['dst_port'])
dst_database = conf_map['dst_db']
dst_username = conf_map['dst_username']
dst_password = conf_map['dst_password']
# dst_schema = conf_map['dst_schema']

parallel_table_num = int(conf_map['parallel_table_num'])
table_parallel_num = int(conf_map['table_parallel_num'])
save_parallel_num = int(conf_map['save_parallel_num'])

commit_num = int(conf_map['commit_num'])
input_global_scn = conf_map['scn']

report_list = {}


# 主控制程序
def main():
    if run_mode == 'copy_data':
        copy_data()
        
    elif run_mode == 'copy_table':
        copy_table()
        
    elif run_mode == 'copy_index':
        copy_index()
        
    elif run_mode == 'copy_constraint':
        copy_constraint()
        
    elif run_mode == 'copy_sequence':
        copy_sequence()
        
    elif run_mode == 'report':
        get_report()
        
    elif run_mode == 'compare_index':
        compare_index()
        
    elif run_mode == 'compare_constraint':
        compare_constraint()
        
    elif run_mode == 'copy_from_sql':
        copy_from_sql()

        
def copy_data():
    # 获取连接
    src_db = DBConn(src_db_type, src_ip, src_port, src_database, src_read_username, src_read_password)
    dst_db = DBConn(dst_db_type, dst_ip, dst_port, dst_database, dst_username, dst_password)
    
    # 解析出需要迁移的表以及映射关系
    table_map_list = get_table_map_list(src_db)
    
    # 清理表
    if if_truncate == 'true':
        for table_map in table_map_list:
            dst_schema = table_map[2]
            dst_table = table_map[3]
            dst_conn = dst_db.dbpool.connection()
            truncate_table_sql = 'truncate table ' + dst_schema + '."' + dst_table.lower() + '" cascade'
            try:
                dst_cur = dst_conn.cursor()
                dst_cur.execute(truncate_table_sql)
                dst_conn.commit()
                log.info(truncate_table_sql)
            except Exception as _:
                log.warning(truncate_table_sql, str(_))
            finally:
                dst_cur.close()
            
    # 获取scn，如果需要
    if if_only_scn == 'true' and len(input_global_scn) == 0:
        global_scn = src_db.run('select to_char(current_scn) from v$database').get_rows()[0][0]
    elif if_only_scn == 'true' and len(input_global_scn) > 0:
        global_scn = input_global_scn
    else:
        global_scn = None
    
    # 多线程启动表分析程序
    tp = ThreadPool(parallel_table_num, while_wait_time=0.1)
    for table_map in table_map_list:
        tp.run(run_table, (table_map, global_scn), thread_id=table_map[0] + '.' + table_map[1])
    
    while True:
        log.info('running_tables : ' + str(tp.get_running_thread()))
        if tp.get_running_num() > 0:
            time.sleep(3)
        else:
            break
    tp.wait()
    
    src_db.close()
    dst_db.close()
    
    # 获取输出报告
    get_report()


def copy_from_sql():
    dst_db = DBConn(dst_db_type, dst_ip, dst_port, dst_database, dst_username, dst_password)
        
    table_map_list = []
    for table_mess in sqls.split('[--split--]'):
        dst_schema = table_mess.split('-->')[1].split('.')[0]
        dst_table = table_mess.split('-->')[1].split('.')[1]
        src_sql = table_mess.split('-->')[0]
        table_map_list.append((None, None, dst_schema, dst_table, src_sql))
        
    # 清理表
    if if_truncate == 'true':
        for table_map in table_map_list:
            dst_schema = table_map[2]
            dst_table = table_map[3]
            dst_conn = dst_db.dbpool.connection()
            truncate_table_sql = 'truncate table ' + dst_schema + '.' + dst_table + ' cascade'
            try:
                dst_cur = dst_conn.cursor()
                dst_cur.execute(truncate_table_sql)
                dst_conn.commit()
                log.info(truncate_table_sql)
            except Exception as _:
                log.warning(truncate_table_sql, str(_))
            finally:
                dst_cur.close()
        
    # 多进程启动导数
    tp = ProcessPool(parallel_table_num, while_wait_time=0.1)
    for table_map in table_map_list:
        tp.run(get_data_from_sql, (table_map,))
    tp.wait()
    
    dst_db.close()

    
def copy_index():

    def copy_one_index(table_map):
        src_schema = table_map[0]
        src_table = table_map[1]
        dst_schema = table_map[2].lower()
        dst_table = table_map[3].lower()
        try:
            dst_db = DBConn(dst_db_type, dst_ip, dst_port, dst_database, dst_username, dst_password)
            src_db = DBConn(src_db_type, src_ip, src_port, src_database, src_read_username, src_read_password)
            dst_conn = dst_db.dbpool.connection()
            dst_cur = dst_conn.cursor()
            select_index_sql = '''
                select t.indexname 
                from pg_indexes t
                where not exists(
                  select 1 from information_schema.constraint_table_usage t2
                  where t2.table_catalog = ?
                  and t2.table_schema = t.schemaname
                  and t2.table_name = t.tablename
                  and t2.constraint_name = t.indexname
                ) and t.schemaname = ? 
                and t.tablename = ?
            '''
            rows = dst_db.run(select_index_sql, (dst_database, dst_schema, dst_table)).get_rows()
            for row in rows:
                index_name = row[0]
                drop_index_sql = 'drop index ' + dst_schema + '.' + index_name
                try:
                    dst_cur.execute(drop_index_sql)
                    dst_conn.commit()
                    log.info(drop_index_sql)
                except Exception as _:
                    log.error(drop_index_sql, str(_))
                    
            metadata = OracleTools.get_table_metadata(src_db, src_schema, src_table, partition=True)
            
            partition_columns = ''
            if metadata['partition'] != None:
                partition = metadata['partition']
                partition_columns = partition['partition_columns']
                
            for idx in metadata['indexes']:
                create_index_sql = ''
                name = idx['name']
                type_ = idx['type']
                my_cols = idx['columns']
                a = []
                for i in partition_columns.split(',') + my_cols.split(','):
                    if i not in a:
                        a.append(i)
                cols_partition_columns = str(a).replace('[', '').replace(']', '').replace("'", '').strip(',').strip()
                if type_ == 'NORMAL':
                    type_ = ''
                if type_ == 'UNIQUE':
                    cols = cols_partition_columns
                else:
                    cols = my_cols
                create_index_sql = create_index_sql + 'create ' + type_ + ' index ' + name + ' on ' + dst_schema + '.' + dst_table + ' (' + cols + ') '
                create_index_sql = Tools.merge_spaces(create_index_sql)
                create_index_sql = create_index_sql.replace(' ASC', '')
                try:
                    dst_cur.execute(create_index_sql)
                    dst_conn.commit()
                    log.info(create_index_sql)
                except Exception as _:
                    if 'does not exist' in str(_):
                        log.warning(create_index_sql, str(_))
                    elif 'already exists' in str(_):
                        name = 'rename_' + str(uuid.uuid4()).split('-')[0]
                        create_index_sql = ''
                        create_index_sql = create_index_sql + 'create ' + type_ + ' index ' + name + ' on ' + dst_schema + '.' + dst_table + ' (' + cols + ') '
                        create_index_sql = Tools.merge_spaces(create_index_sql)
                        create_index_sql = create_index_sql.replace(' ASC', '')
                        try:
                            dst_cur.execute(create_index_sql)
                            dst_conn.commit()
                            log.info(create_index_sql)
                        except Exception as _:
                            if 'does not exist' in str(_):
                                log.warning(create_index_sql, str(_))
                            else:
                                log.error(create_index_sql, str(_))
                    else:
                        log.error(create_index_sql, str(_))
        except Exception as _:
            log.error(dst_schema + '.' + dst_table, str(_))
        finally:
            dst_cur.close()
            dst_conn.close()
            src_db.close()
            dst_db.close()
            
    src_db = DBConn(src_db_type, src_ip, src_port, src_database, src_read_username, src_read_password)
    table_map_list = get_table_map_list(src_db)
    tp = ThreadPool(parallel_table_num, while_wait_time=0.1)
    for table_map in table_map_list:
        tp.run(copy_one_index, (table_map,))
    tp.wait()
    src_db.close()

    
def copy_table():

    def copy_one_table(table_map):
        src_schema = table_map[0]
        src_table = table_map[1]
        dst_schema = table_map[2].lower()
        dst_table = table_map[3].lower()
        src_db = DBConn(src_db_type, src_ip, src_port, src_database, src_read_username, src_read_password)
        dst_db = DBConn(dst_db_type, dst_ip, dst_port, dst_database, dst_username, dst_password)
        dst_conn = dst_db.dbpool.connection()
        dst_cur = dst_conn.cursor()
        
        try:
            drop_sql = 'drop table if exists ' + dst_schema + '."' + dst_table + '"'
            dst_cur.execute(drop_sql)
            dst_conn.commit()
            log.info(drop_sql)
        except Exception as _:
            log.error(drop_sql, str(_))

        sqls = OracleTools.get_table_ddl_pg(src_db, src_schema, src_table, forever_number_to_numeric=forever_number_to_numeric)
        for sql in sqls:
            try:
                if sql.startswith('alter table') and ' add foreign key ' in sql:
                    pass
                elif sql.startswith('alter table') and ' add primary key ' in sql:
                    pass
                elif sql.startswith('alter table') and ' add unique (' in sql:
                    pass
                elif sql.startswith('create index ') or sql.startswith('create UNIQUE index '):
                    pass
                else:
                    sql = sql.replace(' ' + src_schema.lower() + '.', ' ' + dst_schema + '.')
                    dst_cur.execute(sql)
                    dst_conn.commit()
            except Exception as _:
                log.error(src_schema + '.' + src_table, sql, str(_))
        log.info(dst_schema + '.' + dst_table + ' created')
        
        dst_cur.close()
        dst_conn.close()
        src_db.close()
        dst_db.close()
            
    src_db = DBConn(src_db_type, src_ip, src_port, src_database, src_read_username, src_read_password)
    dst_db = DBConn(dst_db_type, dst_ip, dst_port, dst_database, dst_username, dst_password)
    dst_conn = dst_db.dbpool.connection()
    dst_cur = dst_conn.cursor()
    
    table_map_list = get_table_map_list(src_db)
    
    for table_map in table_map_list:
        dst_schema = table_map[2]
        dst_cur.execute('create schema if not exists ' + dst_schema)
        dst_conn.commit()
    
    tp = ThreadPool(32, while_wait_time=0.1)
    for table_map in table_map_list:
        tp.run(copy_one_table, (table_map,))
    tp.wait()
    src_db.close()
    dst_cur.close()
    dst_conn.close()
    dst_db.close()


def copy_constraint():

    def copy_one_constraint_1(table_map):
        src_schema = table_map[0]
        src_table = table_map[1]
        dst_schema = table_map[2].lower()
        # dst_table = table_map[3].lower()
        src_db = DBConn(src_db_type, src_ip, src_port, src_database, src_read_username, src_read_password)
        dst_db = DBConn(dst_db_type, dst_ip, dst_port, dst_database, dst_username, dst_password)
        dst_conn = dst_db.dbpool.connection()
        dst_cur = dst_conn.cursor()
        sqls = OracleTools.get_table_ddl_pg(src_db, src_schema, src_table, forever_number_to_numeric=forever_number_to_numeric)
        for sql in sqls:
            try:
                if sql.startswith('create table '):
                    pass
                elif sql.startswith('create index ') or sql.startswith('create UNIQUE index '):
                    pass
                elif sql.startswith('comment on '):
                    pass
                elif sql.startswith('alter table ') and 'foreign key' in sql:
                    pass
                else:
                    sql = sql.replace(' ' + src_schema.lower() + '.', ' ' + dst_schema + '.')
                    dst_cur.execute(sql)
                    dst_conn.commit()
                    log.info(sql)
            except Exception as _:
                log.error(sql, str(_))
        
        dst_cur.close()
        dst_conn.close()
        src_db.close()
        dst_db.close()
        
    def copy_one_constraint_2(table_map):
        src_schema = table_map[0]
        src_table = table_map[1]
        dst_schema = table_map[2].lower()
        # dst_table = table_map[3].lower()
        src_db = DBConn(src_db_type, src_ip, src_port, src_database, src_read_username, src_read_password)
        dst_db = DBConn(dst_db_type, dst_ip, dst_port, dst_database, dst_username, dst_password)
        dst_conn = dst_db.dbpool.connection()
        dst_cur = dst_conn.cursor()
        sqls = OracleTools.get_table_ddl_pg(src_db, src_schema, src_table, forever_number_to_numeric=forever_number_to_numeric)
        for sql in sqls:
            try:
                if sql.startswith('create table '):
                    pass
                elif sql.startswith('create index ') or sql.startswith('create UNIQUE index '):
                    pass
                elif sql.startswith('comment on'):
                    pass
                elif sql.startswith('alter table ') and 'foreign key' in sql:
                    sql = sql.replace(' ' + src_schema.lower() + '.', ' ' + dst_schema + '.')
                    dst_cur.execute(sql)
                    dst_conn.commit()
                    log.info(sql)
                else:
                    pass
            except Exception as _:
                log.error(sql, str(_))
        
        dst_cur.close()
        dst_conn.close()
        src_db.close()
        dst_db.close()
            
    src_db = DBConn(src_db_type, src_ip, src_port, src_database, src_read_username, src_read_password)
    dst_db = DBConn(dst_db_type, dst_ip, dst_port, dst_database, dst_username, dst_password)
    dst_conn = dst_db.dbpool.connection()
    dst_cur = dst_conn.cursor()
    
    table_map_list = get_table_map_list(src_db)
    
    for table_map in table_map_list:
        src_schema = table_map[0]
        dst_cur.execute('create schema if not exists ' + src_schema)
        dst_conn.commit()
    
    tp = ThreadPool(32, while_wait_time=0.1)
    for table_map in table_map_list:
        tp.run(copy_one_constraint_1, (table_map,))
    tp.wait()
    
    for table_map in table_map_list:
        copy_one_constraint_2(table_map)
        
    src_db.close()
    dst_cur.close()
    dst_conn.close()
    dst_db.close()

    
def copy_sequence():
    src_db = DBConn(src_db_type, src_ip, src_port, src_database, src_read_username, src_read_password)
    dst_db = DBConn(dst_db_type, dst_ip, dst_port, dst_database, dst_username, dst_password)
    dst_conn = dst_db.dbpool.connection()
    dst_cur = dst_conn.cursor()
    table_map_list = get_table_map_list(src_db)
    sql = 'select * from dba_sequences where sequence_owner = ?'
    
    schemas = []
    for table_map in table_map_list:
        if (table_map[0], table_map[2]) not in schemas:
            schemas.append((table_map[0], table_map[2]))
            
    for schema in schemas:
        src_schema = schema[0]
        dst_schema = schema[1]        
        rows = src_db.run(sql, (src_schema,)).get_rows()
        for row in rows:
            # sequence_owner = row[0]
            sequence_name = row[1]
            min_value = row[2]
            max_value = row[3]
            increment_by = row[4]
            cycle_flag = row[5]
            # order_flag = row[6]
            cache_size = row[7]
            last_number = row[8]
            if max_value > 9223372036854775807:
                max_str = 'no maxvalue'
            else:
                max_str = 'maxvalue ' + str(max_value)
            if cache_size == 0:
                cache_str = ''
            else:
                cache_str = 'cache ' + str(cache_size)
            if cycle_flag == 'N':
                cycle_str = ''
            else:
                cycle_str = 'cycle'
            drop_sql = 'drop sequence if exists ' + dst_schema.lower() + '.' + sequence_name.lower()
            dst_cur.execute(drop_sql)
            dst_conn.commit()
            log.info(drop_sql)
            create_sql = 'create sequence ' + dst_schema.lower() + '.' + sequence_name.lower() + ' increment ' + str(increment_by) + ' minvalue ' + str(min_value) + ' ' + max_str + ' start ' + str(last_number) + ' ' + cache_str + ' ' + cycle_str 
            create_sql = Tools.merge_spaces(create_sql).strip()
            try:
                dst_cur.execute(create_sql)
                dst_conn.commit()
                log.info(create_sql)
            except Exception as _:
                log.error(create_sql, str(_))
            
    src_db.close()
    dst_cur.close()
    dst_conn.close()
    dst_db.close()


def get_table_map_list(src_db):
    # 解析出需要迁移的表以及映射关系
    table_map_list = []
    for table_mess in tables.split('[--split--]'):
        table_mess = table_mess.strip()
        src_where = '1=1'
        if '-->' in table_mess:
            if 'where' in table_mess:
                src_schema = table_mess.split('-->')[0].split('.')[0].strip()
                src_table = table_mess.split('-->')[0].split('.')[1].split('where')[0].strip()
                src_where = table_mess.split('-->')[0].split('.')[1].split('where')[1].strip()
            else:
                src_schema = table_mess.split('-->')[0].split('.')[0].strip()
                src_table = table_mess.split('-->')[0].split('.')[1].strip()
            dst_schema = table_mess.split('-->')[1].split('.')[0].strip()
            dst_table = table_mess.split('-->')[1].split('.')[1].strip()
        else:
            if 'where' in table_mess:
                src_schema = table_mess.split('.')[0].strip()
                src_table = table_mess.split('.')[1].split('where')[0].strip()
                src_where = table_mess.split('.')[1].split('where')[1].strip()
            else:
                src_schema = table_mess.split('.')[0].strip()
                src_table = table_mess.split('.')[1].strip()
            dst_schema = src_schema.lower()
            dst_table = src_table.lower()
            
        if src_table == '*':
            select_tables_sql = "select table_name from dba_tables where owner = '" + src_schema + "' order by 1"
            tables_from_sql = src_db.run(select_tables_sql).get_rows()
            for table_from_sql in tables_from_sql:
                if '-->' in table_mess:
                    table_map = (src_schema, table_from_sql[0], dst_schema, table_from_sql[0], src_where)
                else:
                    table_map = (src_schema, table_from_sql[0], src_schema.lower(), table_from_sql[0].lower(), src_where)
                if table_map not in table_map_list and table_map[0] + '.' + table_map[1] not in exclude_tables:
                    table_map_list.append(table_map)
        else:
            table_map = (src_schema, src_table, dst_schema, dst_table, src_where)
            if table_map not in table_map_list and table_map[0] + '.' + table_map[1] not in exclude_tables:
                table_map_list.append(table_map)
        
    return table_map_list


# 表分析程序
def run_table(table_map, global_scn):
    src_schema = table_map[0]
    src_table = table_map[1]
    dst_schema = table_map[2]
    dst_table = table_map[3]
    src_where = table_map[4]
    try:
        # 获取连接
        src_db = DBConn(src_db_type, src_ip, src_port, src_database, src_read_username, src_read_password)
         
        # 如果没有scn，则此处获取
        if global_scn is None:
            table_scn = src_db.run('select to_char(current_scn) from v$database').get_rows()[0][0]
        else:
            table_scn = global_scn
            
        # 判定“表”是什么
        object_type = ''
        sql = 'select object_type from dba_objects where owner = ? and object_name = ?'
        rows = src_db.run(sql, (src_schema, src_table)).get_rows()
        if len(rows) == 0:
            object_type = 'other'
        elif 'TABLE' in rows[0]:
            object_type = 'table'
        elif rows[0] == 'VIEW':
            object_type = 'view'
        elif rows[0] == 'SYNONYM':
            object_type = 'synonym'
        else:
            object_type = 'other'
                
        # 获取表数量，用于对数
        count_sql = 'select /*+parallel(4)*/ count(1) from ' + src_schema + '."' + src_table + '" as of scn ' + table_scn + ' where ' + src_where
        src_num = src_db.run(count_sql).get_rows()[0][0]
        report_table_id = src_schema + '.' + src_table + '-->' + dst_schema + '.' + dst_table
        report_list[report_table_id] = [table_scn, src_num, None]
        
        tp = ProcessPool(table_parallel_num, while_wait_time=0.1)
        # 如果是表，获取表元数据信息，遍历分区子分区，多进程分配查询任务及后续任务
        if object_type == 'table':
            table_metadata = OracleTools.get_table_metadata(src_db, src_schema, src_table, partition=True)
            partition_mess = table_metadata['partition']
            if partition_mess is not None and smallest_object != 'table':
                for partition in partition_mess['partitions']:
                    partition_name = partition['name']
                    subpartitions = partition['subpartitions']
                    if len(subpartitions) > 0 and smallest_object == 'subpartition':
                        for subpartition in subpartitions:
                            subpartition_name = subpartition['name']
                            mess = src_schema + '."' + src_table + '" subpartition(' + subpartition_name + ')'
                            tp.run(get_data_from_oracle, (table_map, mess, table_scn, table_metadata))
                    else:
                        mess = src_schema + '."' + src_table + '" partition(' + partition_name + ')'
                        tp.run(get_data_from_oracle, (table_map, mess, table_scn, table_metadata))
            else:
                mess = src_schema + '."' + src_table + '"'
                tp.run(get_data_from_oracle, (table_map, mess, table_scn, table_metadata))
                # page_num = ceil(src_num / commit_num)
                # if page_num <= table_parallel_num:
                    # tp.run(get_data_from_oracle, (table_map, mess, table_scn))
                # else:
                    # page_rn = ceil(src_num / table_parallel_num)
                    # for page in range(1, table_parallel_num + 1):
                        # tp.run(get_data_from_oracle, (table_map, mess, table_scn, page, page_rn))
        # 其他类型直接进行，也无法获取元数据
        else:
            table_metadata = None
            mess = src_schema + '."' + src_table + '"'
            tp.run(get_data_from_oracle, (table_map, mess, table_scn, table_metadata))
        tp.wait()
        src_db.close()
    except Exception as _:
        log.error('run_table', src_schema + '.' + src_table, str(_))

        
def get_data_from_oracle(table_map, mess, table_scn, table_metadata=None, page=None, page_rn=None): 
    src_where = table_map[4]
    try:
        # 获取连接
        src_db = DBConn(src_db_type, src_ip, src_port, src_database, src_read_username, src_read_password)
        
        # copy中转为csv要用
        cols_for_copy = src_db.run('select * from ' + mess + ' where rownum = 1').get_cols_description()
        if table_metadata is not None:
            idx = 0
            for col in table_metadata['columns']:
                virtual = col['virtual']
                if virtual == 'YES':
                    cols_for_copy.pop(idx)
            idx = idx + 1
        
        if table_metadata is not None:
            for col in table_metadata['columns']:
                virtual = col['virtual']
        
        # 解析列，用于拼接cols_str和merge_col，处理char，拆分clob
        if_exists_clob = False
        cols_str = ''
        idx = 0
        idx2 = 0
        merge_col = []
        for col in cols_for_copy:
            merge_col.append([])
            if 'CHAR' in str(col[1]):
                merge_col[idx] = [idx2]
                idx2 = idx2 + 1
                cols_str = cols_str + 'replace("' + col[0] + '",chr(0),chr(32)),' 
            elif 'CLOB' in str(col[1]):
                if_exists_clob = True
                merge_col[idx] = []
                sql = 'select nvl(max(length(' + col[0] + ')),0) from ' + mess + ' as of scn ' + table_scn
                max_len = src_db.run(sql).get_rows()[0][0]
                col_split_num = ceil(int(max_len) / 1300)
                for sub_idx in range(1, col_split_num + 1):
                    cols_str = cols_str + 'nvl(replace(to_char(substr(' + col[0] + ',' + str(sub_idx - 1) + "*1300+1,1300)),chr(0),chr(32)),''),"
                    merge_col[idx].append(idx2)
                    idx2 = idx2 + 1
            elif 'DATE' in str(col[1]):
                merge_col[idx] = [idx2]
                idx2 = idx2 + 1
                cols_str = cols_str + '''replace(replace(replace(to_char("''' + col[0] + '''",'yyyy-mm-dd hh24:mi:ss'),'0000-','0001-'),'-00-','-01-'),'-00','-01'),'''
            elif 'TIMESTAMP' in str(col[1]):
                merge_col[idx] = [idx2]
                idx2 = idx2 + 1
                cols_str = cols_str + '''replace(replace(replace(to_char("''' + col[0] + '''",'yyyy-mm-dd hh24:mi:ss.ff9'),'0000-','0001-'),'-00-','-01-'),'-00','-01'),'''
            else:
                merge_col[idx] = [idx2]
                idx2 = idx2 + 1
                cols_str = cols_str + '"' + col[0] + '",' 
            idx = idx + 1
        cols_str = cols_str[:-1]
        
        # 组装抽数sql
        if page is None:
            select_sql = 'select /*+ FIRST_ROWS */ ' + cols_str + '  from ' + mess + ' as of scn ' + table_scn + ' where ' + src_where
        else:
            select_sql = '''
                select ''' + cols_str + ''' from (
                    select t.*,rownum rn 
                    from ''' + mess + ''' 
                    as of scn ''' + str(table_scn) + ''' t
                    where rownum <= ''' + str(page) + ''' * ''' + str(page_rn) + '''
                    and ''' + src_where + '''
                ) where rn <= ''' + str(page) + ''' * ''' + str(page_rn) + '''
                and rn > ''' + str(page - 1) + ''' * ''' + str(page_rn) + '''
            '''
        
        # 开始抽数
        rs = src_db.run(select_sql)
        i = 1
        tp = ThreadPool(save_parallel_num, while_wait_time=0.1)
        while True:
            if page is None:
                my_mess = mess + '(' + str(i) + ')'
            else:
                my_mess = mess + '(' + str(page) + '-' + str(i) + ')'
            time_start = time.time()
            rows = rs.get_rows(commit_num)
            rows_new = []
            # 如果含有clob，之前有做拆分，此处再拼接回来
            if if_exists_clob:
                for row in rows:
                    idx = 0
                    row_new = []
                    for cols_idx in merge_col:
                        if len(cols_idx) == 1:
                            cell = row[cols_idx[0]]
                        else:
                            cell = None
                            for col_idx in cols_idx:
                                if row[col_idx] is None:
                                    pass
                                elif type(row[col_idx]) == str:
                                    if type(cell) != str:
                                        cell = ''
                                    cell = cell + row[col_idx]
                                elif type(row[col_idx]) == bytes:
                                    if type(cell) != bytes:
                                        cell = b''
                                    cell = cell + row[col_idx]
                        row_new.append(cell)
                        idx = idx + 1
                    rows_new.append(row_new)
            else:
                rows_new = rows
                    
            select_time = time.time() - time_start
            if len(rows_new) == 0:
                break
            tp.run(save_to_pg, (table_map, rows_new, cols_for_copy, my_mess, select_time, table_scn))
            i = i + 1
            if len(rows_new) < commit_num:
                break
            del rows_new, rows
            gc.collect()
        tp.wait()
        src_db.close()
    except Exception as _:
        log.error('get_data_from_oracle', mess, select_sql, str(_))

        
def get_data_from_sql(table_map): 
    dst_schema = table_map[2]
    dst_table = table_map[3]
    src_sql = table_map[4]
    try:
        # 获取连接
        src_db = DBConn(src_db_type, src_ip, src_port, src_database, src_read_username, src_read_password)
        
        select_sql = src_sql
        
        rs = src_db.run(select_sql)
        cols = rs.get_cols_description()
        
        i = 1
        tp = ThreadPool(save_parallel_num, while_wait_time=0.1)
        while True:
            time_start = time.time()
            rows = rs.get_rows(commit_num)
            select_time = time.time() - time_start
            if len(rows) == 0:
                break
            tp.run(save_to_pg, (table_map, rows, cols, dst_schema + '.' + dst_table, select_time, ''))
            i = i + 1
            if len(rows) < commit_num:
                break
            del rows
            gc.collect()
        tp.wait()
        src_db.close()
    except Exception as _:
        log.error('get_data_from_sql', dst_schema + '.' + dst_table, str(_))

        
def save_to_pg(table_map, rows, cols, mess, select_time, table_scn):
    dst_schema = table_map[2]
    dst_table = table_map[3]
    src_where = table_map[4]
    time_start = time.time()
    # 获取连接
    try:
        dst_db = DBConn(dst_db_type, dst_ip, dst_port, dst_database, dst_username, dst_password, options='-c search_path=' + dst_schema + ',public')
    except Exception as _:
        log.error('save_to_pg', mess, str(_))
        return
    
    wenhaos = ''
    for _ in cols:
        wenhaos = wenhaos + '?,'
    wenhaos = wenhaos[0:-1]
    insert_sql = 'insert into ' + dst_table + ' values(' + wenhaos + ')'
    
    try:
        num = dst_db.pg_copy_from(dst_table.lower(), rows, cols)
        num = str(num) + '(copy)' 
        del rows
        gc.collect()
        dst_db.close()
    except Exception as _:
        # log.warning(mess, str(_))
        try:
            num = dst_db.run(insert_sql, rows)
            if num == -1:
                raise Exception('unknown error, num = -1')
            num = str(num) + '(insert)' 
            del rows
            gc.collect()
            dst_db.close()
        except Exception as _:
            log.error(mess, str(_).replace('\n', ' '))
            dst_db.close()
            return

    save_time = time.time() - time_start
    if src_where == '1=1':
        src_where = ''
    log.info(mess, src_where, num, str(round(select_time, 2)) + 's', str(round(save_time, 2)) + 's', 'scn=' + table_scn)


def get_report():
    tp = ThreadPool(16)

    def count(db, sql, k):
        e1 = ''
        try:
            num = int(db.run(sql).get_rows()[0][0])
        except Exception as _:
            num = -1
            e1 = str(_)
        report_list[k][2] = num
        log.info('report', report_list[k][1] == report_list[k][2], k, report_list[k][1], report_list[k][2], 'scn=' + str(report_list[k][0]), str(e1))
    
    def count2(table_map, src_db, dst_db, global_scn):
        src_schema = table_map[0]
        src_table = table_map[1]
        dst_schema = table_map[2]
        dst_table = table_map[3]
        
        src_sql = 'select  /*+full(t)*/ count(1) from ' + src_schema + '."' + src_table + '" as of scn ' + global_scn
        dst_sql = 'select count(1) from ' + dst_schema + '."' + dst_table.lower() + '"'
        
        e1 = ''
        e2 = ''
        try:
            src_num = int(src_db.run(src_sql).get_rows()[0][0])
        except Exception as _:
            src_num = -1
            e1 = str(_)
        try:
            dst_num = int(dst_db.run(dst_sql).get_rows()[0][0])
        except Exception as _:
            dst_num = -2
            e2 = str(_)
            
        report_table_id = src_schema + '.' + src_table + '-->' + dst_schema + '.' + dst_table
        report_list[report_table_id] = [global_scn, src_num, dst_num]
        log.info('report', report_list[report_table_id][1] == report_list[report_table_id][2], report_table_id, report_list[report_table_id][1], report_list[report_table_id][2], 'scn=' + global_scn, str(e1), str(e2))
    
    if run_mode == 'copy_data':
        log.info('Generating report')
        try:
            dst_db = DBConn(dst_db_type, dst_ip, dst_port, dst_database, dst_username, dst_password, poolsize=8)
        except Exception as _:
            log.error('report', str(_))
        error_table = ''
        
        for k in report_list:
            src_schema = k.split('-->')[1].split('.')[0]
            src_table = k.split('-->')[1].split('.')[1]
            dst_sql = 'select count(1) from ' + src_schema + '."' + src_table.lower() + '"'
            tp.run(count, (dst_db, dst_sql, k))
        tp.wait()
        
        for k in report_list:
            if report_list[k][1] != report_list[k][2]:
                error_table = error_table + k + '[--split--]'
        error_table = error_table.rstrip('[--split--]')
                
        log.info('error_table : ' + error_table)
        dst_db.close()
            
    elif run_mode == 'report':
        try:
            src_db = DBConn(src_db_type, src_ip, src_port, src_database, src_read_username, src_read_password, poolsize=8)
            dst_db = DBConn(dst_db_type, dst_ip, dst_port, dst_database, dst_username, dst_password, poolsize=8)
        except Exception as _:
            log.error('report', str(_))
            
        # 如果没有scn，则此处获取
        if len(input_global_scn) == 0:
            global_scn = src_db.run('select to_char(current_scn) from v$database').get_rows()[0][0]
        else:
            global_scn = input_global_scn
        
        # 解析出需要迁移的表以及映射关系
        table_map_list = get_table_map_list(src_db)
        
        error_table = ''
        for table_map in table_map_list:
            tp.run(count2, (table_map, src_db, dst_db, global_scn))
        tp.wait()
            
        for k in report_list:
            if report_list[k][1] != report_list[k][2]:
                error_table = error_table + k + '[--split--]'
        error_table = error_table.rstrip('[--split--]')
                
        log.info('error_table : ' + error_table)
        src_db.close()
        dst_db.close()

        
def compare_index():

    def compare_index_one(table_map):
        src_schema = table_map[0]
        src_table = table_map[1]
        dst_schema = table_map[2].lower()
        dst_table = table_map[3].lower()
        try:
            src_db = DBConn(src_db_type, src_ip, src_port, src_database, src_read_username, src_read_password, poolsize=8)
            dst_db = DBConn(dst_db_type, dst_ip, dst_port, dst_database, dst_username, dst_password, poolsize=8)
        except Exception as _:
            log.error('compare_index', str(_))
        
        e1 = ''
        e2 = ''
        src_sql = "select count(distinct t.index_name) from dba_indexes t where not exists(select 1 from dba_constraints t2 where t2.owner = t.table_owner and t2.table_name = t.table_name and t2.constraint_name = t.index_name) and t.index_type not in('LOB') and t.table_owner = '" + src_schema + "' and t.table_name = '" + src_table + "'"
        dst_sql = "select count(distinct t.indexname) from pg_indexes t where not exists(select 1 from information_schema.constraint_table_usage t2 where t2.table_catalog = ? and t2.table_schema = t.schemaname and t2.table_name = t.tablename and t2.constraint_name = t.indexname) and t.schemaname = '" + dst_schema + "' and t.tablename = '" + dst_table + "'"
        try:
            src_num = src_db.run(src_sql).get_rows()[0][0]
        except Exception as _: 
            src_num = -1
            e1 = str(_)
        try:
            dst_num = dst_db.run(dst_sql, (dst_database,)).get_rows()[0][0]
        except Exception as _:
            dst_num = -2
            e2 = str(_)
        log.info('compare_index', src_num == dst_num, src_schema + '.' + src_table, 'oracle=' + str(src_num), 'pgsql=' + str(dst_num), str(e1), str(e2))
        dst_db.close()
        src_db.close()
    
    try:
        src_db = DBConn(src_db_type, src_ip, src_port, src_database, src_read_username, src_read_password, poolsize=8)
    except Exception as _:
        log.error('compare_index', str(_))
    
    # 解析出需要迁移的表以及映射关系
    table_map_list = get_table_map_list(src_db)
    
    tp = ThreadPool(32, while_wait_time=0.1)
    for table_map in table_map_list:
        tp.run(compare_index_one, (table_map,))
    tp.wait()

    src_db.close()

    
def compare_constraint():

    def compare_constraint_one(table_map):
        src_schema = table_map[0]
        src_table = table_map[1]
        dst_schema = table_map[2].lower()
        dst_table = table_map[3].lower()
        src_db = DBConn(src_db_type, src_ip, src_port, src_database, src_read_username, src_read_password, poolsize=8)
        dst_db = DBConn(dst_db_type, dst_ip, dst_port, dst_database, dst_username, dst_password, poolsize=8, options='-c search_path=' + dst_schema + ',public')
        e1 = ''
        e2 = ''
        src_sql = "select count(distinct index_name) from dba_constraints where owner = '" + src_schema + "' and table_name = '" + src_table + "'"
        dst_sql = "select count(distinct constraint_name) from information_schema.constraint_table_usage where table_catalog = '" + dst_database + "' and table_schema = '" + dst_schema + "' and table_name = '" + dst_table + "'"
        try:
            src_num = src_db.run(src_sql).get_rows()[0][0]
        except Exception as _: 
            src_num = -1
            e1 = str(_)
        try:
            dst_num = dst_db.run(dst_sql).get_rows()[0][0]
        except Exception as _:
            dst_num = -2
            e2 = str(_)
        log.info('compare_constraint', src_num == dst_num, src_schema + '.' + src_table, 'oracle=' + str(src_num), 'pgsql=' + str(dst_num), str(e1), str(e2))
        src_db.close()
        dst_db.close()
    
    try:
        src_db = DBConn(src_db_type, src_ip, src_port, src_database, src_read_username, src_read_password, poolsize=8)
    except Exception as _:
        log.error('compare_index', str(_))
    
    # 解析出需要迁移的表以及映射关系
    table_map_list = get_table_map_list(src_db)
    
    tp = ThreadPool(32, while_wait_time=0.1)
    for table_map in table_map_list:
        tp.run(compare_constraint_one, (table_map,))
    tp.wait()

    src_db.close()

            
if __name__ == '__main__': 
    main()
