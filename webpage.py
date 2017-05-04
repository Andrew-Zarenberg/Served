from flask import Flask, render_template, request, redirect, url_for, session
import user_actions, utils, suggestions

app = Flask(__name__)

header = ""
footer = ""#utils.footer()

# This is only fetched through a GET request

@app.route("/see_repeats")
def see_repeats():
    suggestions.see_repeats()
    return "true"

@app.route("/suggestion")
def suggestion():
    return suggestions.next_restaurant(request.args.get("neighborhood"))

@app.route("/superlike")
def superlike():
    return suggestions.superlike(request.args.get("restaurant"))

@app.route("/clear_superlikes")
def superlike_remove_all():
    return suggestions.clear_superlikes()

@app.route("/remove_superlike")
def superlike_remove():
    return suggestions.remove_superlike(request.args.get("restaurant"))

@app.route("/no_more_rests")
def no_more_rests():
    return '<div id="suggestion" style="margin-left:auto;margin-right:auto;width:550px;text-align:center;">You have rated all restaurants.<br /><br /><a href="#" onclick="seeRepeats()">See restaurants you have already rated?</a></div>'

# END GET REQUESTS

# REDIRECTS

@app.route("/delete_restaurant")
def delete_restaurant():
    if "username" in session and session["username"] != "":
        ret_val = user_actions.delete_restaurant(request.args.get("id"))
        if ret_val == True:
            return redirect("my_restaurants?deleted=1")

    else:
        return "<script>window.location='/'</script>" #FIX

@app.route("/add_restaurant_image", methods=["GET", "POST"])
def add_restaurant_image():
    if "username" in session and session["username"] != "":
        ret_val = user_actions.add_restaurant_image(request.form["id"], request.form["url"])

        if ret_val == True:
            return redirect("/view_restaurant?added=1&id=%s"%(request.form["id"]))
        else:
            return redirect("/view_restaurant?added=-1&id=%s"%(request.form["id"]))

    else:
        return "<script>window.location='/'</script>" #FIX

@app.route("/delete_restaurant_image")
def delete_restaurant_image():
    if "username" in session and session["username"] != "":
        ret_val = user_actions.delete_restaurant_image(request.args.get("id"), request.args.get("img"))

        if ret_val == True:
            return redirect("/view_restaurant?deleted=1&id=%s"%(request.args.get("id")))
        else:
            return redirect("/view_restaurant?deleted=-1&id=%s"%(request.args.get("id")))

    else:
        return "<script>window.location='/'</script>" #FIX

@app.route("/add_restaurant", methods=["GET","POST"])
def new_restaurant():
    if "username" in session and session["username"] != "":
        name = request.form["name"]
        address = request.form["address"]
        cat = request.form["category"]
        nabe = request.form["neighborhood"]

        user_actions.add_restaurant(name, address, cat, nabe)

        return redirect("/my_restaurants")
    else:
        return "<script>window.location='/'</script>" #FIX


# END OF REDIRECTS


@app.route("/view_restaurant")
def view_restaurant():
    if "username" in session and session["username"] != "":
        rest = user_actions.view_restaurant(request.args.get("id"))

        added = ""
        if request.args.get("added") == "1":
            added = '<div class="alert alert-success" role="alert">Image successfully added!</div>'
        elif request.args.get("added") == "-1":
            added = '<div class="alert alert-danger" role="alert">Error adding image.</div>'
        elif request.args.get("deleted") == "1":
            added = '<div class="alert alert-success" role="alert">Image successfully deleted!</div>'
        elif request.args.get("deleted") == "-1":
            added = '<div class="alert alert-danger" role="alert">Error deleting image.</div>'


        return render_template("view_restaurant.html", rest=rest["rest"], name=rest["name"], category=rest["category"], id=request.args.get("id"), added=added)


    else:
        return "<script>window.location='/'</script>" #FIX

@app.route("/my_restaurants")
def my_restaurants():
    if "username" in session and session["username"] != "":
        rest = user_actions.my_restaurants()
        return render_template("my_restaurants.html", rest=rest["rest"], cat=rest["cat"], nabes=rest["nabes"])

    return "<script>window.location='/'</script>" #FIX

@app.route("/profile")
def profile():
    if "username" in session and session["username"] != "":
        header = utils.header(session["username"])

    prof = user_actions.my_profile()
    return render_template("profile.html", profile=prof, header=header, footer=footer)

@app.route("/")
def index():
    nabes = ["Downtown Brooklyn", "Williamsburg", "Upper East Side", "Upper West Side", "Midtown East"]
    footer = utils.footer()
    if "username" in session and session["username"] != "":
        header = utils.header(session["username"])

        if request.args.get("neighborhood") not in nabes:
            return redirect("/?neighborhood=%s"%nabes[0])

        nabes = user_actions.nabes(request.args.get("neighborhood"))

        sug = suggestions.next_restaurant(request.args.get("neighborhood"))
        eatlist = suggestions.generate_superlike_table()
        return render_template("homepage.html", restaurant=sug, superlike=eatlist, header=header, footer=footer, neighborhoods=nabes)
    else:
        header = utils.header("")
        return render_template("index.html", header=header, footer=footer)

@app.route("/rate")
def rate():
    return_code = suggestions.rate(request.args.get("restaurant"),
                                   request.args.get("type"))
    return str(return_code)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if "username" in session and session["username"] != "":
        return "<script>window.location='/'</script>" #FIX

    header = utils.header("")
    footer = utils.footer()


    if request.method == 'POST':
        return_code = user_actions.login(request.form["username"],
                                         request.form["password"])
        if return_code == 1:
            session["username"] = request.form["username"]
            return "<script>window.location='/'</script>" #FIX
        else:
            return render_template("login.html", return_code=return_code, header=header, footer=footer)
    else:
        return render_template("login.html", header=header, footer=footer)

@app.route("/logout")
def logout():
    session["username"] = ""
    return "<script>window.location='/'</script>" #FIX

@app.route("/register", methods=['GET', 'POST'])
def register():
    if "username" in session and session["username"] != "":
        return "<script>window.location='/'</script>" #FIX

    header = utils.header("")
    footer = utils.footer()

    if request.method == 'POST':
        return_code = user_actions.register(request.form["username"],
                                            request.form["pass1"],
                                            request.form["pass2"])
        if return_code == 1:
            session["username"] = request.form["username"]
            return "<script>window.location='/'</script>" #FIX
        else:
            return render_template("register.html", return_code=return_code, header=header, footer=footer)
    else:
        return render_template("register.html", header=header, footer=footer)

app.secret_key = "$&CYT4NCYT847yct3"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)
