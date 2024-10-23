# coding:utf-8
import time
import threading
from uuid import uuid1
import eventlet

mylist = []


def main():
    pp = ThreadPool(2)
    for num in range(1, 10):
        pp.run(a1, (num,))
    pp.wait()

    
def a1(a):
    pp = ThreadPool(2)
    for num in range(10, 20):
        pp.run(a2, (num, a))
    pp.wait()

    
def a2(a, b):
    print(b, a)
    time.sleep(3)


class ThreadPool():
    """ 维护一个线程池 """
    
    def __init__(self, size, save_result=False, while_wait_time=0.1, report=False):
        self.size = size
        self.running_thread = []
        self.result_map = {}
        self.save_result = save_result
        self.while_wait_time = while_wait_time
        self.report = report

    def run(self, func, args, kwargs={}, time_out=None, thread_id=uuid1()):
        """ 主线程命令当前线程池从空闲线程中取一个线程执行给入的方法，如果池满，则主线程等待 """
        if len(self.running_thread) < self.size:
            self.running_thread.append(thread_id)
            t = myThread(func, args=args, kwargs=kwargs, thread_id=thread_id, running_thread=self.running_thread, result_map=self.result_map, save_result=self.save_result, time_out=time_out)
            t.start()
            return thread_id
        else:
            while len(self.running_thread) >= self.size:
                time.sleep(self.while_wait_time)
            return self.run(func, args, kwargs, time_out, thread_id=thread_id)

    def get_results(self):
        return self.result_map
    
    def get_result(self, thread_id):
        return self.result_map[thread_id]
    
    def clear_result(self):
        self.result_map = {}

    def wait(self):
        """ 主线程等待，直到线程池不存在活动线程 """
        while len(self.running_thread) > 0:
            time.sleep(self.while_wait_time)
    
    def get_running_num(self):
        return len(self.running_thread)
    
    def get_running_thread(self):
        return self.running_thread


class myThread (threading.Thread):

    def __init__(self, func, args, kwargs, thread_id, running_thread, result_map, save_result, time_out):
        threading.Thread.__init__(self)
        threading.Thread.daemon = True
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.thread_id = thread_id
        self.running_thread = running_thread
        self.result_map = result_map
        self.save_result = save_result
        self.time_out = time_out

    def run(self):
        try:
            if self.time_out is None:
                result = self.func(*self.args, **self.kwargs)
                if self.save_result:
                    self.result_map[self.thread_id] = result
            else:
                # 实测效率很低
                eventlet.monkey_patch()
                with eventlet.Timeout(self.time_out, False):
                    result = self.func(*self.args, **self.kwargs)
                    if self.save_result:
                        self.result_map[self.thread_id] = result
        finally:
            self.running_thread.remove(self.thread_id)


if __name__ == '__main__':
    main()
