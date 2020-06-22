# pip install flask --user
# pip install requests --user

import requests
from flask import Flask, render_template, request, redirect, url_for, flash, session
from api_modules.RequestsApi import RequestsApi
from models.User import User
from models.RealState import RealState
from models.Vote import Vote

app = Flask(__name__)

app.secret_key = "565646lfljkhjg"

@app.route('/')
def index():
    res = RequestsApi.get_all_api()
    print(res)
    return render_template("index.html")

@app.route('/new-user')
def new_user():
    return "New record"

@app.route('/save')
def save():
    #user = User(name="")
    vote = Vote(value=1)
    res = RequestsApi.save_api(vote)
    print(res)
    return "Saved"

@app.route('/view/<id>')
def view(id):
    res = RequestsApi.get_one_api(id)
    print(res)
    return "View"

@app.route('/delete/<id>')
def delete(id):
    res= RequestsApi.delete_api(id)
    print(res)
    return "Deleted"

if __name__ == '__main__':
    app.run(port=8081, debug=True)


#5109000 solicitudes
#70138648
#4-2

