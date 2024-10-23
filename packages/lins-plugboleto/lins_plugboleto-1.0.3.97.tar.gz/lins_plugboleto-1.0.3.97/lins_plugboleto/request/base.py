import uuid
import json
import time
from requests import Request, Session, codes


class Base(object):

    def __init__(self, authorize):

        self.authorize = authorize

    def send_request(self, method, uri, data=None, params=None):

        s = Session()

        body = data

        headers = {
            'cnpj-sh': self.authorize.cnpjsh,
            'token-sh': self.authorize.tokensh,
            'cnpj-cedente': self.authorize.cnpjcedente
        }

        if not body:
            headers['Content-Length'] = '0'
        else:
            headers["Content-Type"] = "application/json"

            if not isinstance(data, dict):
                body = body.toJSON()

        req = Request(method, uri, data=body, headers=headers, params=params)

        prep = s.prepare_request(req)

        response = s.send(prep)

        i=0
        while response.status_code in [codes.gateway_timeout, codes.bad_gateway]:
            time.sleep(3)
            response = s.send(prep)
            if i>1:
                break
            i += 1

        if 'json' in response.headers['Content-Type'].lower():
            answers = response.json()
        else:
            answers = [{
                'Code': str(response.status_code),
                'Message': response.text
            }]

        if response.status_code >= 400:
            errors = response.json()
            raise Exception(errors)

        return answers, body

    def request_numerodoc(self, method, uri):

        s = Session()

        req = Request(method, uri)

        prep = s.prepare_request(req)

        response = s.send(prep)

        body = None

        if 'json' in response.headers['Content-Type'].lower():
            answers = response.json()
        else:
            answers = [{
                'Code': str(response.status_code),
                'Message': response.text
            }]

        if response.status_code >= 400:
            errors = []

            for answer in answers:
                errors.append('\r\n * [%s] %s\r\n' % (answer['Code'], answer['Message']))

            data_send = json.loads(body or 'null')

            raise Exception('\r\n%s\r\nMethod: %s\r\nUri: %s\r\nData: %s' % (
                ''.join(errors), method, response.url, json.dumps(data_send, indent=2)))

        return answers
