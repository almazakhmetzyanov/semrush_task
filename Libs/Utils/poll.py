# -*- coding: utf-8 -*-
from time import sleep


class Poll:
    @staticmethod
    def poll(func, max_poll_time=15, *args, **kwargs):
        """
        Метод для ожидания возвращения правды от какой-либо функции
        :param func: функция
        :param max_poll_time: сколько итераций ждать
        :param args: неименованные аргументы для функции
        :param kwargs: именованные аргументы дла функции
        :return: возвращает либо ничего, либо результат выполнения функции
        """
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
