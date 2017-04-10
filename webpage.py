from flask import Flask, render_template, request, redirect, url_for, session
import user_actions, utils, suggestions

app = Flask(__name__)

header = ""
footer = ""#utils.footer()

# This is only fetched through a GET request
@app.route("/suggestion")
def suggestion():
    return suggestions.next_restaurant()

@app.route("/superlike")
def superlike():
    return suggestions.superlike(request.args.get("restaurant"))

@app.route("/clear_superlikes")
def superlike_remove_all():
    return suggestions.clear_superlikes()

@app.route("/remove_superlike")
def superlike_remove():
    return suggestions.remove_superlike(request.args.get("restaurant"))

@app.route("/profile")
def profile():
    if "username" in session and session["username"] != "":
        header = utils.header(session["username"])

    prof = user_actions.my_profile()
    return render_template("profile.html", profile=prof, header=header, footer=footer)

@app.route("/")
def index():
    footer = utils.footer()
    if "username" in session and session["username"] != "":
        header = utils.header(session["username"])

        sug = suggestions.next_restaurant()
        eatlist = suggestions.generate_superlike_table()
        return render_template("homepage.html", restaurant=sug, superlike=eatlist, header=header, footer=footer)
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
