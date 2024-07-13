from flask import render_template, flash, redirect
from app import app 
from app.forms import LoginForm
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
@app.route('/login', methods=['GET', 'POST']) 
def login(): 
    form = LoginForm() 
    if form.validate_on_submit(): 
        flash('Login in for user {}, remember me {}'.format(form.username.data,form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title = 'Sign In', form=form)
