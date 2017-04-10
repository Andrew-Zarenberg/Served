from flask import session
from pymongo import MongoClient
import hashlib
from operator import itemgetter

client = MongoClient()

db = client.Served


def register(username, pass1, pass2):
    if username == "" or pass1 == "" or pass2 == "":
        return "Missing fields"
    if pass1 != pass2:
        return "Passwords do not match"
    else:
        if db.user.find({"username": username}).count() != 0:
            return "Username already exists"
        else:
            db.user.insert({
                    "username": username,
                    "password": hashlib.sha256(pass1).hexdigest()
                    })
            return 1

def login(username, password):
    if db.user.find({"username": username, "password": hashlib.sha256(password).hexdigest()}).count() == 1:
        return 1
    else:
        return "Invalid login information"


def my_profile():
    if "username" not in session or session["username"] == "":
        return "Error: You must be logged in to vew 'My Profile'"

    dab = db.rating.find({"username": session["username"], "type":1})
    total = dab.count()

    r = ""

    total_rest = db.rating.find({"username": session["username"]}).count()
    r += '<div>So far, I have seen <strong>%d</strong> restaurant suggestions.</div><br />'%total_rest

    r += '<table id="preferences" cellspacing="0"><tr><th colspan="2"><strong>My Restaurant Preferences</strong></th></tr>'

    cats = []
    for x in dab:
        if [x["category"]] not in cats:
            cats.append([x["category"]])

    for x in range(0,len(cats)):
        perc = db.rating.find({"username": session["username"], "category": cats[x][0], "type":1}).count()
        cats[x].append(float(perc)/total*100)

    a = sorted(cats, key=itemgetter(1), reverse=True)

    for x in a:
        r += '<tr><th>%s</th><td>%.1f%%</td></tr>'%(x[0], x[1])

    

    r += '</table>'

    return r
