# pip install flask --user
# pip install requests --user

import requests
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask import session
from api_modules.RequestsApi import RequestsApi
from api_modules.RequestsApiUser import RequestsApiUser
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
    return render_template("index.html", properties = res['properties'])

@app.route('/new-property', methods = ['GET', 'POST'])
def new_property():
    return render_template('create_property.html')

@app.route('/save-property', methods = ['GET', 'POST'])
def save_property():
    
    if request.method == 'POST':
        try:
            title_input = request.form['title_property']
            type_input = request.form['type_property']
            payment_input = request.form['payment_type']
            address_input = request.form['address']
            rooms_input = request.form['rooms']
            price_input = request.form['price']
            area_input = request.form['area']
            new_property = Property(title_property=title_input, type_property=type_input, payment_type=payment_input, address=address_input, rooms=rooms_input, price=price_input, area=area_input, property_image="img.jpg")
            res = RequestsApi.save_api(new_property)
            print(res)
            return redirect(url_for('index', result=res))
        except:
            return 'Not saved property'

@app.route('/view-property/<id>')
def view(id):
    res = RequestsApi.get_one_api(id)
    return render_template('property_detail.html', one_property= res['property'])

@app.route('/delete-property/<id>')
def delete(id):
    res= RequestsApi.delete_api(id)
    print(res)
    return "Deleted"




@app.route('/new-user', methods = ['GET', 'POST'])
def new_user():
    return render_template('create_user.html')

@app.route('/save-user', methods = ['GET', 'POST'])
def save():
    if request.method == 'POST':
        try:
            email_input = request.form['email']
            password_input = request.form['password']
            user = User(email=email_input, password=password_input)
            res = RequestsApiUser.save_api(user)
            print(res)
            return redirect(url_for('index', res_user=res))
        except:
            return 'Not saved'
       


@app.route('/login', methods = ['GET', 'POST'])
def login():
    #if request.method == 'POST':
    #    try:
    #        email_input = request.form['email']
    #        password_input = request.form['password']
    #        
    #        if(email_input == 'p'):
    #            session

    #            return redirect(url_for('index'))
    #    except:
    #        return 'Not saved'

    return render_template('login.html')






if __name__ == '__main__':
    app.run(port=8081, debug=True)