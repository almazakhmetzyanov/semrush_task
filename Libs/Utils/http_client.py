# -*- coding: utf-8 -*-
import requests
import json


class HTTPClient:
    @staticmethod
    def send_get_request(url):
        try:
            response = requests.get(url=url)
            return response
        except Exception as e:
            print('Can not receive response: {}'.format(e))
            return False

    @staticmethod
    def send_post_request(url, data):
        try:
            response = requests.post(url=url, json=data)
            return response
        except Exception as e:
            print('Can not receive response: {}'.format(e))
            return False


if __name__ == '__main__':
    HTTPClient().send_post_request(url='http://127.0.0.1:5000/get_custom_header/urhew',
                                   data=json.dumps({"custom_header_one": "custom_header_content_one. QWEQRYT!@#%^&*( 123",
                                                    "custom_header_two": "custom_header_content_two. QWEQRYT!@#%^&*( 123",
                                                    "custom_header_three": "custom_header_content_two. QWEQRYT!@#%^&*( 123"}))
