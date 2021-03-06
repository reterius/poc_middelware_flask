from werkzeug.wrappers import Request, Response, ResponseStream


class middleware():
    '''
    Simple WSGI middleware
    '''

    def __init__(self, app):
        self.app = app
        self.username = 'admin'
        self.password = '1234'
        self.name = 'Mehmet'

    def __call__(self, environ, start_response):
        request = Request(environ)

        username = request.authorization['username']
        password = request.authorization['password']

        # these are hardcoded for demonstration
        # verify the username and password from some database or env config variable
        if username == self.username and password == self.password:
            environ['user'] = {'user': self.username, 'name': self.name}
            return self.app(environ, start_response)

        res = Response(u'Authorization failed', mimetype='text/plain', status=401)
        return res(environ, start_response)
