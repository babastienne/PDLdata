from web.bottle.bottle import *
from db.Requests import Requests


"""/*
    Function: index
    This will be the home page of the server, it will display all the activities and the city in the database
*/"""
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
@route("/semantic/<filename>")
def semantic(filename):
    return static_file(filename, root='web/semantic/')

@route("/static/<filename>")
def serve_static(filename):
	return static_file(filename,root="web/static/")

@route("/scripts/<filename>")
def script(filename):
    return static_file(filename, root='web/scripts/')

#Run the server on the port 8080 at the localhost adress.
run(host="localhost", port=8080, debug=False)
