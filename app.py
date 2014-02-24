from bottle import route, run

@route('/')
def index():
    return '<h1>Hello Bottle</h1>'

run()

