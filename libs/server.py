import bottle
from bottle import route, template, run

@route('/')
@route('/index.html')
def index():
	return template('web/montemplate', { 'commune' : "void", 'activite' : "void", 'installation' : "void"})

run(host='localhost', port=8080)



@get('/action')
def action():
	commune = request.query.get('commune','void') #void correspond à la valeur par défaut si jamais le champ est vide (on aurai pu mettre 'blabla')
	activite = request.query.get('activite','void')
	installation = request.query.get('installation','void')
	return template('web/montemplate', { 'commune' : commune, 'activite' : activite, 'installation' : installation})
