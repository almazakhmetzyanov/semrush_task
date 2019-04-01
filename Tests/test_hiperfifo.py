# -*- coding: utf-8 -*-
from Tests.base_test import BaseTest
import json
import pytest

expected_headers = ['custom_header_one: custom_header_content_one. QWEQRYT!@#%^&*( 123',
                    'custom_header_two: custom_header_content_two. QWEQRYT!@#%^&*( 123',
                    'custom_header_three: custom_header_content_three. QWEQRYT!@#%^&*( 123']

expected_headers_json = json.dumps({"custom_header_one": "custom_header_content_one. QWEQRYT!@#%^&*( 123",
                                    "custom_header_two": "custom_header_content_two. QWEQRYT!@#%^&*( 123",
                                    "custom_header_three": "custom_header_content_three. QWEQRYT!@#%^&*( 123"})


class TestHiperfifo(BaseTest):
    def test_hiperfifo_headers_validation(self):
        """
        1) Скармливаем вспомогательной апишке хедеры которые хотим увидеть в логе hiperfifo
        2) Отправляем запрос через fifo
        3) Достаем из логов нужные нам хедеры
        4) Проверяем найденные хедеры
        """
        url = '{}/get_custom_header/url'.format(self.base_url)
        resp = self.http_client.send_post_request(url=url, data=expected_headers_json)
        assert resp.status_code == 200, 'Wrong response status from {}'

        self.send_request_with_hiperfifo(url=url)
        extracted_headers = self.poll.poll(self.headers_extractor.extract_headers_from_log, host=self.host, api_method='GET')
        assert extracted_headers, 'Can not find request headers from url {}'.format(url)

        ret = self.validate_headers(received_headers=extracted_headers, expected_headers=expected_headers)
        assert ret, 'Received headers does not equal to expected: Received: {} Expected: {}'.format(extracted_headers, expected_headers)

    @pytest.mark.parametrize('url_suffix, is_success', [('a' * 983, True),
                                                        ('a' * 984, False)])
    def test_hiperfifo_urls_length(self, url_suffix, is_success):
        """
        1) Скармливаем вспомогательной апишке хедеры которые хотим увидеть в логе hiperfifo
        2) Отправляем запрос через fifo
        3) Достаем из логов нужные нам хедеры
        4) Проверяем найденные хедеры, либо их отсутствие
        """
        url = '{}/get_custom_header/{}'.format(self.base_url, url_suffix)
        resp = self.http_client.send_post_request(url=url, data=expected_headers_json)
        assert resp.status_code == 200, 'Wrong response status from {}'

        self.send_request_with_hiperfifo(url=url)
        extracted_headers = self.poll.poll(self.headers_extractor.extract_headers_from_log, host=self.host, api_method='GET')
        if not is_success:
            assert not extracted_headers, 'Headers found, but expected fail'
            return
        assert extracted_headers, 'Can not find request headers from url {}'.format(url)

        ret = self.validate_headers(received_headers=extracted_headers, expected_headers=expected_headers)
        assert ret, 'Received headers does not equal to expected: Received: {} Expected: {}'.format(extracted_headers, expected_headers)

    @pytest.mark.parametrize('url_suffix', ['what_a_nice_url',
                                            'what_a_not_nice_url?J!@*#',
                                            'search?q=dqwefqew',
                                            'search\?country=123123\?per_page=40\&allo=allo'])
    def test_hiperfifo_with_different_url_types(self, url_suffix):
        """
        1) Скармливаем вспомогательной апишке хедеры которые хотим увидеть в логе hiperfifo
        2) Отправляем запрос через fifo
        3) Достаем из логов нужные нам хедеры
        4) Проверяем найденные хедеры
        """
        url = '{}/get_custom_header/{}'.format(self.base_url, url_suffix)
        resp = self.http_client.send_post_request(url=url, data=expected_headers_json)
        assert resp.status_code == 200, 'Wrong response status from {}'

        self.send_request_with_hiperfifo(url=url)
        extracted_headers = self.poll.poll(self.headers_extractor.extract_headers_from_log, host=self.host, api_method='GET')
        assert extracted_headers, 'Can not find request headers from url {}'.format(url)

        ret = self.validate_headers(received_headers=extracted_headers, expected_headers=expected_headers)
        assert ret, 'Received headers does not equal to expected: Received: {} Expected: {}'.format(extracted_headers, expected_headers)
