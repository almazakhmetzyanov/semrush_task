# -*- coding: utf-8 -*-
from time import sleep


class Poll:
    @staticmethod
    def poll(func, max_poll_time=15, *args, **kwargs):
        for i in range(0, max_poll_time):
            try:
                ret = func(*args, **kwargs)
                if ret:
                    return ret
                else:
                    print('Poll try {}, func {}, ret = {}'.format(i, func.__name__, ret))
                    sleep(1)
                    continue
            except Exception as e:
                print('Poll try {}, func {}. Error: {}'.format(i, func.__name__, e))
                sleep(1)
                continue
