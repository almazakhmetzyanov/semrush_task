# -*- coding: utf-8 -*-
import tests_config
import re


class HeadersExtractor:
    @staticmethod
    def _prepare_url_for_regexp(url):
        # символы которые надо спрятать от регулярного выражения, это тупо, зато просто
        symbols_for_replacing = ['?', '.', '-', '+']
        for i in symbols_for_replacing:
            url = url.replace(i, '\\{}'.format(i))
        return url

    def extract_headers_from_log(self, host, api_method):
        # я перенаправил stderr канал hiperfifo в файлик и беру всю информацию оттуда
        log = open(file=tests_config.HIPERFIFO_LOG_FILE_PATH, mode='r').read()
        # для более простого регулярного выражения я сделал лог одной строкой, чтобы не мучаться с переносами
        log_without_line_break = log.replace('\n', '')
        # вычленяем всю информацию по связке урл + апи метод, чтобы не вытянуть чего лишнего, берём последнее актуальное
        prepared_url = self._prepare_url_for_regexp(host)
        search_result = re.findall(r'> {}.*Host: {}.*<'.format(api_method, prepared_url), log_without_line_break)[-1]
        # убираем уже ненужные строки из того что нашлось + разделяем на список
        headers_list = re.search(r'<.*<', search_result).group().split('< ')[2:]
        # убираем ненужный лишний символ <
        headers_list[-1] = headers_list[-1][:-1]
        return headers_list


if __name__ == "__main__":
    print(HeadersExtractor().extract_headers_from_log(host='http://127.0.0.1:5000', api_method='GET'))
