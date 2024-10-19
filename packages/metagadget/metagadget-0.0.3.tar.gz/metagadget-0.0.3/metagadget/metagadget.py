from werkzeug.wrappers import Response, Request
from werkzeug.serving import run_simple
import ngrok
import json
import os

PORT = int(os.environ.get("PORT", 5001))
DOMAIN = os.environ.get("NGROK_DOMAIN")
VERIFY = os.environ.get("VERIFY_TOKEN")


class MetaGadget:
    def __init__(self):
        pass

    def dispatch_request(self, request):
        data = request.get_json()
        _res = self._dispatch_request(data['request'])

        res = {
            "verify": VERIFY,
            "response": _res
        }
        if not VERIFY:
            print("The response will not be received by the client. Please set the VERIFY_TOKEN environment variable.")
        return Response(json.dumps(res), content_type='application/json')        

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def receive(self, func):
        self._dispatch_request = func
        return func

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

    def run(self):
        if not os.environ.get("WERKZEUG_RUN_MAIN"):
            print("Starting ngrok")
            ngrok.forward(PORT, authtoken_from_env=True, domain=DOMAIN)
        run_simple('127.0.0.1', PORT, self, use_debugger=True, use_reloader=True)


if __name__ == '__main__':
    app = MetaGadget()

    @app.receive
    def handle(request):
        print(f'Hello World {request}')
    app.run()
