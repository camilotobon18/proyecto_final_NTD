# pip install flask --user
# pip install requests --user

import requests
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask import session
from api_modules.RequestsApi import RequestsApi
from models.User import User
from models.Property import Property
from models.Vote import Vote
from models.form import UserForm, LoginForm
import random
import os
from os import listdir

app = Flask(__name__)
app.secret_key = "565646lfljkhjg"

def session_validate():
    if 'login' in session:
        return True
    else:
        return False


@app.route('/')
def index():
    res = RequestsApi.get_all_api()
    print(res)
    return render_template("index.html", votes = res)

@app.route('/new-user', methods = ['GET', 'POST'])
def new_user():
    return render_template('create_user.html')

@app.route('/save', methods = ['GET', 'POST'])
def save():
    #user = User(name="")
    #vote = Vote(value=0, image_id=img)
    #res = RequestsApi.save_api(vote)
    #print(res)
    #user_form = UserForm(request.form)
    if request.method == 'POST':
        try:
            #ruta = os.getcwd()+'\\static\\img'
            #imglist = listdir(ruta)
            #img = random.choice(imglist)
            #name_input = user_form.name.data
            #last_name_input = user_form.last_name.data
            #email_input = user_form.email.data
            #password_input =user_form.password.data
            name_input = request.form['name_user']
            last_name_input = request.form['last_name']
            email_input = request.form['email']
            password_input = request.form['password']
            user = User(name=name_input, last_name=last_name_input, email=email_input, password=password_input)
            #res = RequestsApi.save_api(user)
            print(name_input,last_name_input,email_input,password_input, sep=" ")
            return redirect(url_for('index'))
        except:
            return 'Not saved'
        #return render_template("create_user.html", form=user_form)

@app.route('/delete/<id>')
def delete(id):
    res= RequestsApi.delete_api(id)
    print(res)
    return "Deleted"






@app.route('/new-property', methods = ['GET', 'POST'])
def new_property():
    return render_template('create_property.html')

@app.route('/save-property', methods = ['GET', 'POST'])
def save_property():
    if request.method == 'POST':
        try:
            title_input = request.form['title_property']
            type_input = request.form['type_property']
            address_input = request.form['address']
            rooms_input = request.form['rooms']
            price_input = request.form['price']
            area_input = request.form['area']
            new_property = Property(title_property=title_input, type_property=type_input, address=address_input, rooms=rooms_input, price=price_input, area=area_input)
            #res = RequestsApi.save_api(new_property)
            return redirect(url_for('index'))
        except:
            return 'Not saved property'

@app.route('/view/<id>')
def view(id):
    #res = RequestsApi.get_one_api(id)
    #print(res)
    return render_template('property_detail.html', one_property= res)



@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            email_input = request.form['email']
            password_input = request.form['password']
            
            if(email_input == 'p'):
                session

            return redirect(url_for('index'))
        except:
            return 'Not saved'





#@app.route('/login', methods = ['GET', 'POST'])
#def login():
#    login_form = LoginForm(request.form)
#    if request.method == 'POST' and login_form.validate():
#        session['username'] = login_form.email.data
#    return render_template('login.html', form = login_form)


if __name__ == '__main__':
    app.run(port=8081, debug=True)