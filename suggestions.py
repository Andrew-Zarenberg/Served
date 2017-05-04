from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import session
import random
import time

client = MongoClient()

db = client.Served


RANDOM_IMAGES = [
    'http://parkresto.com/wp-content/themes/parkrestaurant/images/11onlinereservationpark.jpg',
    'http://basera-dfw.com/wp-content/uploads/2016/03/restaurant.jpeg',
    'https://upload.wikimedia.org/wikipedia/commons/1/1e/Tom%27s_Restaurant%2C_NYC.jpg',
    'https://media-cdn.tripadvisor.com/media/photo-s/06/45/0e/fe/fino-cocktail-bar-restaurant.jpg',
    'http://www.mahoneysirishpub.com//templates/template_20/images/background-1.jpg',
    'http://www.chateaueza.com/media/hotel-chateau-eza-imageLinkchateau-eza-restaurant11.jpg',
    'https://s-media-cache-ak0.pinimg.com/736x/6a/6d/59/6a6d592266d211232c88641cead840d1.jpg',
    'http://www.thedistractionnetwork.com/images/sign-fail-pics-0159.jpg',
    'https://static01.nyt.com/images/2009/04/04/nyregion/04chicken_xl.jpg',
    'https://s-media-cache-ak0.pinimg.com/736x/c1/6a/5d/c16a5dce1cf9a54bae1b03a1a37839d0.jpg',
    'http://www.africawanderer.com/wp-content/uploads/2013/01/fancy-restaurant-Marrakesh-by-rickpilot_2000.jpg',
    'http://photoshopcontest.com/images/large/pzmc7hmedw33b69ayinp2c3a9twrp4atqqfk.jpg',
    'http://i0.wp.com/www.foodrepublic.com/wp-content/uploads/2012/05/heartattack_fancyrestaurant.jpg?fit=1024%2C683'
    ]




def format_html(rest):

    """
    # TEMPORARY --- ONLY FOR TESTING
    if len(rest["pictures"]) == 0:
        pictures = []
        for x in range(0,3):
            pictures.append(RANDOM_IMAGES[random.randrange(0,len(RANDOM_IMAGES))])
    else:
        pictures = rest["pictures"]
    # end TEMPORARY
    """

    pictures = rest["pictures"]

    ratings = db.rating.find({"restaurant": rest["_id"]})
    ratings_count = ratings.count()

    r_sum = 0
    for x in ratings:
        r_sum += x["type"]

    if ratings_count != 0:
        ratings_num = float(r_sum)/ratings_count
    else:
        ratings_num = 0

    ratings_num *= 10
    

    r = '<div id="suggestion" style="margin-left:auto;margin-right:auto;width:550px;text-align:center;">'

    r += '<div id="suggestion_images" style="position:relative"><div class="result"></div><button onclick="prevImage()" id="prevImage" disabled="true" title="Previous Image" class="btn btn-default">&laquo;</button>'
    
    # Image
    if len(pictures) == 0:
        r += '<img class="img-rounded" src="http://hardisprayer.com/images/photo_not_available.jpg" width="400px" height="400px" />'
    else:
        r += '<img id="img0" src="%s" width="400px" height="400px" />'%pictures[0]

    for x in range(1, len(pictures)):
        r += '<img id="img%d" src="%s" width="400px" height="400px" style="display:none" />'%(
            x, pictures[x])

    r += '<button onclick="nextImage()" id="nextImage" title="Next Image" class="btn btn-default">&raquo;</button></div>'

    # Name
    r += '<table cellspacing="0" class="info"><tr><td class="name" colspan="3"><strong>%s</strong>, %s</td></tr>'%(rest["name"], rest["category"])

    # Address
    r += '<tr><td colspan="3" class="address"><a href="https://google.com/maps/place/%s" target="_blank">%s</a></td></tr>'%(rest["address"], rest["address"])
    
    r += '<tr><td colspan="3"><hr /></td></tr>'

    r += '<tr id="ratings_tr"><td class="dislike"><span onclick="ratingDown(\'%s\')" title="Dislike">&#10060;</span></td><td class="ratings">'%str(rest["_id"])

    # Ratings
    if ratings_num == 0:
        r += '<span class="ratings_num">N/A</span><br /><span class="ratings_count">No ratings</span>'
    else:
        rating_text = "rating"
        if ratings_count > 1:
            rating_text = "ratings"

        r += '<span class="ratings_num">%.1f</span> / 10<br /><span class="ratings_count">%d %s</span>'%(ratings_num, ratings_count, rating_text)

    # super like
    r += '<br /><span class="superlike" onclick="superlike(\'%s\')" title="I want to eat here!">&#10024</span><br /><br />'%rest["_id"]


    
    r += '</td><td class="like"><span onclick="ratingUp(\'%s\')" title="Like">&#9989;</span></td></tr></table>'%str(rest["_id"])
    r += '</div>'

    return r

def next_restaurant(nabe):
    return next_restaurant_nodup(nabe)
    last_reset = db.user.find({"username": session["username"]})
    total_rated = db.rating.find({"username": session["username"],
                                  "time": {"$gt": last_reset[0]["time"]}})

    print(str(total_rated.count()),"-",str(db.restaurants.find().count()))
    if total_rated.count() == db.restaurants.find().count():
        print("You have rated all restaurants.")
        

def next_restaurant_nodup(nabe):
    last_reset = db.user.find({"username": session["username"]})
    already_rated = db.rating.find({"username": session["username"],
                                    "time": {"$gt": last_reset[0]["time"]}})

    if already_rated.count() == db.restaurants.find().count():
        print("You already rated all restaurants.")



    already_rated_list = []
    for x in already_rated:
        already_rated_list.append(x["restaurant"])

    print("len: "+str(already_rated.count()))
    print(str(already_rated_list))
    # list of categories
    categories = []
    total_len = 0
    rests = db.restaurants.find({"neighborhood": nabe, "_id": {"$nin": already_rated_list}} )

    if rests.count() <= 1:
        in_nabe = db.restaurants.find({"neighborhood": nabe})
        if in_nabe.count() == 0:
            return '<div id="suggestion" style="margin-left:auto;margin-right:auto;width:550px;text-align:center;">There are no entries for restaurants in this neighborhood.<br /><br />Perhaps try a different neighborhood?</div>'
        elif in_nabe.count() == 1:
            return format_html(in_nabe[0])
        else:
            return '<div id="suggestion" style="margin-left:auto;margin-right:auto;width:550px;text-align:center;">You have rated all restaurants.<br /><br /><a href="#" onclick="seeRepeats()">See restaurants you have already rated?</a></div>'
    for x in rests:
        if x["category"] not in categories:
            user_times = max(1,db.rating.find({"username": session["username"], "category": x["category"], "type":1}).count())
            total_len += user_times
            categories.append([x["category"],user_times])

    next_suggestion = random.randrange(0, total_len)

    chosen_cat = ""
    
    cur_num = 0
    for x in categories:
        cur_num += x[1]

        if cur_num <= next_suggestion:
            chosen_cat = x[0]
            

    print("Suggestion: %s"%chosen_cat)

    r = db.restaurants.find({"category": chosen_cat})

    if r.count() == 0:
        return next_restaurant(nabe)

    restaurant = r[random.randrange(0, r.count())]

    return format_html(restaurant)




def next_restaurant2():
    # list of categories
    categories = []
    total_len = 0
    for x in db.restaurants.find():
        if x["category"] not in categories:
            user_times = max(1,db.rating.find({"username": session["username"], "category": x["category"], "type":1}).count())
            total_len += user_times
            categories.append([x["category"],user_times])


    next_suggestion = random.randrange(0, total_len)

    chosen_cat = ""
    
    cur_num = 0
    for x in categories:
        cur_num += x[1]

        if cur_num <= next_suggestion:
            chosen_cat = x[0]
            

    print("Suggestion: %s"%chosen_cat)

    r = db.restaurants.find({"category": chosen_cat})

    restaurant = r[random.randrange(0, r.count())]

    last_rated = db.rating.find({"restaurant": restaurant["_id"],
                                 "username": session["username"]})

    if last_rated.count() > 0:
        my_last_time = db.user.find({"username":session["username"]})

        if(last_rated[0]["time"] > my_last_time[0]["time"]):
            return next_restaurant2()

    return format_html(restaurant)


# rating_type = Like or Dislike
def rate(restaurant_id, rating_type):
    if "username" not in session or session["username"] == "":
        return "f1"
    if rating_type != "Like" and rating_type != "Dislike":
        return "f2"
    else:
        try:
            r = db.restaurants.find({"_id": ObjectId(restaurant_id)})
            
            if r.count() == 0:
                return "f3"

            rating = 1
            if rating_type == "Dislike":
                rating = 0

            exists = db.rating.find({"restaurant": ObjectId(restaurant_id),
                                     "username": session["username"]})
            if exists.count() > 0:
                new_entry = {}
                new_entry["restaurant"] = exists[0]["restaurant"]
                new_entry["category"] = exists[0]["category"]
                new_entry["username"] = exists[0]["username"]
                new_entry["type"] = float(exists[0]["type"]*exists[0]["num_ratings"]+rating)/(exists[0]["num_ratings"]+1)
                new_entry["num_ratings"] = exists[0]["num_ratings"]+1
                new_entry["time"] = time.time()

                db.rating.update({"restaurant": ObjectId(restaurant_id),
                                  "username": session["username"]},
                                 new_entry)
            else:
                db.rating.insert({"restaurant": ObjectId(restaurant_id),
                                  "category": r[0]["category"],
                                  "username": session["username"],
                                  "type": rating,
                                  "num_ratings": 1,
                                  "time": time.time()})

            return True
        except:
            return "f4"
        

def superlike(restaurant_id):
    if db.superlike.find({"username": session["username"],
                          "restaurant": restaurant_id}).count() == 0:

        rest = db.restaurants.find({"_id": ObjectId(restaurant_id)})

        if rest.count() != 0:

            rate(restaurant_id, "Like")

            db.superlike.insert({"username": session["username"],
                                 "name": rest[0]["name"],
                                 "category": rest[0]["category"],
                                 "address": rest[0]["address"],
                                 "restaurant": restaurant_id
                                 })

    return generate_superlike_table()


def generate_superlike_table():        
    # Create the new html list output
    r = '<table class="table table-bordered" cellspacing="0" id="eatlist"><tr><th class="header"><h4>"I want to eat here!" list</h4></th></tr><tr><th style="text-align:center;"><a href="javascript:void(0)" onclick="clearSuperlikes()">Clear all entries</a></th></tr>'
    for x in db.superlike.find({"username": session["username"]}):
        r += '<tr><td><div class="remove_superlike" style="float:left;" onclick="removeSuperlike(\'%s\')">&#10060</div><span><strong>%s</strong>, %s<br /><a href="https://google.com/maps/place/%s" target="_blank">%s</a></span></td></tr>'%(x["restaurant"], x["name"], x["category"], x["address"], x["address"])

    r += '</table>'
    return r

def clear_superlikes():
    db.superlike.remove({"username": session["username"]})

    cur = db.user.find({"username": session["username"]})

    new_entry = {}
    new_entry["username"] = cur[0]["username"]
    new_entry["password"] = cur[0]["password"]
    new_entry["time"] = time.time()

    db.user.update({"username": session["username"]},
                   new_entry)


    return generate_superlike_table()

def remove_superlike(restaurant_id):
    db.superlike.remove({"username": session["username"],
                         "restaurant": restaurant_id})
    return generate_superlike_table()


def see_repeats():
    cur = db.user.find({"username": session["username"]})

    new_entry = {}
    new_entry["username"] = cur[0]["username"]
    new_entry["password"] = cur[0]["password"]
    new_entry["time"] = time.time()

    db.user.update({"username": session["username"]},
                   new_entry)


    


def test():
    r = "<html><head><link rel='stylesheet' href='static/style.css' /></head><body>"
    r += format_html(db.restaurants.find()[0])
    r += "<script type='text/javascript' src='static/logic.js'></script></body></html>"
    return r


if __name__ == "__main__":
    print(next_restaurant())
