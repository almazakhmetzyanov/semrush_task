from flask import Flask, Response, request
import json
from Tools.flask_app import flask_config as config

app = Flask(__name__)


# один бесконечный эндпоинт для удобного тестинга hiperfifo
@app.route('/get_custom_header/<something>', methods=['GET', 'POST'])
def get_custom_header(something):
    # можно заставить эту приложеньку возврашать какие захочешь хедеры
    if request.method == 'POST':
        try:
            with open(file='flask_app/response_headers.json', mode='w') as headers_file:
                headers_file.write(str(request.get_json()))
                headers_file.flush()
                headers_file.close()
            return 'Headers updated'
        except Exception as e:
            return 'Can not update headers. Error: {}'.format(e)
    elif request.method == 'GET':
        headers_file = open(file='flask_app/response_headers.json', mode='r')
        return Response(headers=json.loads(headers_file.read()))


if __name__ == '__main__':
    app.run(host=config.FLASK_APP_HOST, port=config.FLASK_APP_PORT, debug=True)
