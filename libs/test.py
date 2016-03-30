from bottle import route, template, run

@route('/hello/<name>')
def index(name):
	return template('montemplate', blab=name)

run(host='localhost', port=8080)

