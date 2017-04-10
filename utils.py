

def header(username):
    if username:
        return """
<div id="top">You are logged in as <strong>%s</strong> | 
<a href="profile">My Profile</a> | <a href="logout">Logout</a>
</div>

<div id="page">
"""%username
    else:
        return """
<div id="top"><strong>Welcome to Served!</strong> | 
<a href="login">Login</a> | 
<a href="register">Register</a>
</div>

<div id="page">
"""


def footer():
    return """
</div>

<!--<div id="footer"><strong>Served</strong></div>-->
"""
