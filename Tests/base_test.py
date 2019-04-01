# -*- coding: utf-8 -*-
import tests_config
import os
from Libs.Utils.headers_extractor import HeadersExtractor
from Libs.Utils.http_client import HTTPClient
from Libs.Utils.poll import Poll


class BaseTest:
    host = tests_config.HOST
    port = tests_config.PORT
    base_url = tests_config.BASE_URL
    http_client = HTTPClient()
    headers_extractor = HeadersExtractor()
    poll = Poll()

    @classmethod
    def setup_method(cls):
        # чистим файлик с логами перед началом тестов
        open(tests_config.HIPERFIFO_LOG_FILE_PATH, 'w').close()
        pass

    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_method(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    @staticmethod
    def _execute_sys_command(cmd):
        os.system(cmd)
        print('Executed shell command: {}'.format(cmd))

    def send_request_with_hiperfifo(self, url):
        self._execute_sys_command('echo {} > {}'.format(url, tests_config.HIPERFIFO_PIPE_FILE_PATH))

    @staticmethod
    def validate_headers(received_headers, expected_headers):
        number_of_coincidences = len(list(set(received_headers).intersection(expected_headers)))
        print(number_of_coincidences)
        if number_of_coincidences == len(expected_headers):
            return True
        else:
            return False
