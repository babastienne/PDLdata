from web.bottle.bottle import *
from db.Requests import Requests


""" This function is the route to the main screen (index.tpl).
    For the initialization the server get all the activities and city and
    put them in parameters for the template. """
@route('/')
def index():
    r = Requests()
    activity = r.getActivity()
    city = r.getCity()
    output = template('web/index', activity = activity, city = city)
    return output


""" This function 'result' is called after the main screen. It show or not the result of the request """
@route('/result', method = 'POST')
def result():
    r = Requests()
    city = request.forms.get('city')
    activity = request.forms.get('activity')

    installations = r.getInstallations(activity, city)
    if len(installations) > 0:
        output = template('web/displayInstallations', instal = installations)
    else:
        output = template('web/displayNoResult')
    return output


""" Those functions are used to complete the html (contains scripts, css, img ...)
    The semantic files are issues of this github project : https://github.com/Semantic-Org/Semantic-UI-CSS"""
@route("/style/<filename>")
def style(filename):
    return static_file(filename, root='web/style/')

@route("/img/<filename>")
def img(filename):
	return static_file(filename,root="web/img/")

@route("/scripts/<filename>")
def script(filename):
    return static_file(filename, root='web/scripts/')

#Run the server on the port 8080 at the localhost adress.
run(host="localhost", port=8080, debug=False)
