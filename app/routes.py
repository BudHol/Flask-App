from flask import render_template
from app import app 
@app.route('/') 
@app.route('/index') 
def index(): 
    user = {"username": "Gopal"} 
    posts = [
        {
            "author":{"username":"Mikel"},
            "body":"Hi, the weather is great here in Portland!!"
        }, 
        {
            "author":{"username":"Gege"},
            "body":"Nah, imma bring back Kenny once more"
        }
        
    ]
    return render_template('index.html', title = 'Home', user=user, posts=posts)