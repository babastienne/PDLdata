from views.bottle.bottle import route, run, debug, template, post, request, static_file
from insert.traitement import Traitement


"""/*
    Function: index
    This will be the home page of the server, it will display all the activities and the city in the database
*/"""
@route('/')
def index():
    t = Traitement()
    activites = t.getActivites()
    villes = t.getVilles()
    output = template('views/index', activites = activites, villes = villes)
    return output


"""/*
    Function: result
    After selecting the activity and the city, this page will print the result matching the city and the activity wanted
*/"""
@route('/result', method = 'POST')
def result():
        activite = request.forms.get('activite')
        ville = request.forms.get('ville')
        t = Traitement()
        installations = t.getInstallations(activite, ville)
        if len(installations) > 0:
            output = template('views/affichageIns', installations = installations)
        else:
            output = template('views/affichageResultNull')
        return output

"""/*
    Function: css
    This function will return the css file
*/"""
@route("/semantic/<filename>")
def semantic(filename):
    return static_file(filename, root='views/semantic/')

@route("/scripts/<filename>")
def semantic(filename):
    return static_file(filename, root='views/scripts/')

run(host="localhost", port=8080, debug=True)
