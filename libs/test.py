from bottle import route, template, run

@route('/hello/<name>')
def index(name):
	return template('<b>Hello {{blab}}</b>!', blab=name)

run(host='localhost', port=8080)

