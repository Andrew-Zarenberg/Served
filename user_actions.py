from flask import session
from pymongo import MongoClient
import hashlib
from operator import itemgetter
from bson.objectid import ObjectId

client = MongoClient()

db = client.Served

nab = ["Downtown Brooklyn", "Williamsburg", "Upper East Side", "Upper West Side", "Midtown East"]

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
                    "password": hashlib.sha256(pass1).hexdigest(),
                    "time": 0
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

    #r += '<table id="preferences" cellspacing="0"><tr><th colspan="2"><strong>My Restaurant Preferences</strong></th></tr>'
    r += '<table class="table" cellspacing="0"><tr><th colspan="2"><strong>Restaurant Categores Like Percentages</strong></th></tr>'

    cats = []
    for x in dab:
        if [x["category"]] not in cats:
            cats.append([x["category"]])

    """
    for x in range(0,len(cats)):
        perc = db.rating.find({"username": session["username"], "category": cats[x][0], "type":1}).count()
        cats[x].append(float(perc)/total*100)

    """
    for x in range(0, len(cats)):
        total = 0
        perc = db.rating.find({"username": session["username"], "category": cats[x][0]})
        for y in perc:
            total += y["type"]

        cats[x].append(float(total*100)/perc.count())

    a = sorted(cats, key=itemgetter(1), reverse=True)

    for x in a:
        r += '<tr><th>%s</th><td>%.1f%%</td></tr>'%(x[0], x[1])

    

    r += '</table>'

    return r


def my_restaurants():

    r = ""

    my_rest = db.restaurants.find({"creator":session["username"]})
    for x in range(0, my_rest.count()):
        rest = my_rest[x]

        ratings = db.rating.find({"restaurant": rest["_id"]})
        ratings_count = ratings.count()

        r_sum = 0
        for y in ratings:
            r_sum += y["type"]

        if ratings_count != 0:
            ratings_num = float(r_sum)/ratings_count
        else:
            ratings_num = 0

        ratings_num *= 10

        if ratings_count == 0:
            r += '<tr><td>%d</td><td><a href="view_restaurant?id=%s">%s</a></td><td>%s</td><td style="text-align:center;">No ratings</td></tr>'%(x+1, rest["_id"], rest["name"], rest["category"])
        else:
            r += '<tr><td>%d</td><td><a href="view_restaurant?id=%s">%s</a></td><td>%s</td><td style="text-align:center;">%.1f<br /><small>%d ratings</small></td></tr>'%(x+1, rest["_id"], rest["name"], rest["category"], ratings_num, ratings_count)

    nabes = '<select name="neighborhood">'

    for x in nab:
        nabes += '<option value="%s">%s</option>'%(x,x)

    nabes += '</select>'


    cat = '<select name="category">'
    cats = []
    cc = db.restaurants.find()
    for x in cc:
        if x["category"] not in cats:
            cats.append(x["category"])

    cats.sort()

    for x in cats:
        cat += '<option value="%s">%s</option>'%(x,x)
    cat += '</select>'

    return {"rest":r, "nabes":nabes, "cat":cat}


def view_restaurant(n):
    rest = db.restaurants.find({"_id": ObjectId(n), "creator": session["username"]})

    count = 0
    r = ""
    for x in rest[0]["pictures"]:
        count += 1
        r += '<tr><td><br /><strong>Image #%d</strong> <a href="delete_restaurant_image?id=%s&img=%s" class="btn btn-danger">Delete Image</a><br /><br /><img src="%s" width="400px" height="400px" /></td></tr>'%(count, n, x, x)
        #r += '<tr><td>%d</td><td><img src="%s" width="400px" height="400px" /></td><td><a href="delete_restaurant_image?id=%s&img=%s" class="btn btn-danger">Delete Image</a></td></tr>'%(count, x, n, x)

    return {"name": rest[0]["name"],
            "category": rest[0]["category"],
            "rest": r}


def add_restaurant_image(n, url):
    confirm = db.restaurants.find({"_id": ObjectId(n),
                                   "creator": session["username"]})
    if confirm.count() == 1:
        new_images = confirm[0]["pictures"]
        new_images.append(url)

        db.restaurants.update({"_id": ObjectId(n)},
                              {"$set":{"pictures":new_images}})

        return True

    return False


def delete_restaurant_image(n, url):    
    confirm = db.restaurants.find({"_id": ObjectId(n),
                                   "creator": session["username"]})
    if confirm.count() == 1:
        new_images = confirm[0]["pictures"]
        new_images.remove(url)

        db.restaurants.update({"_id": ObjectId(n)},
                              {"$set":{"pictures":new_images}})

        return True

    return False


def nabes(n):

    if n in nab:
        neb = n
    else:
        neb = nab[0]

    r = '<div class="btn-group"><button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Neighborhood: %s <span class="caret"></span></button><ul class="dropdown-menu">'%neb

    for x in nab:
        r += '<li><a href="/?neighborhood=%s">%s</a></li>'%(x,x)

    r += '</ul></div>'

    return r


def add_restaurant(name, address, category, neighborhood):
    k = db.restaurants.insert({"name":name,
                               "address":address,
                               "neighborhood":neighborhood,
                               "category":category,
                               "pictures":[],
                               "ratings":[],
                               "creator":session["username"]})
    print("EDROFGYUIDIDFG: %s"%k)


def delete_restaurant(n):
    db.restaurants.remove({"_id":ObjectId(n), "creator":session["username"]})
    return True
