from flask import Flask, render_template
from azure.cosmosdb.table.tableservice import TableService
table_service = TableService(account_name='cloudshell703046314', account_key='fTJlnFKqcwkuu4BCIJiOnIqGEB3aNBkY/yaZ55tm7UWKtzuTv5/pdHgzL2HunOGu8IuMHEEV92nMY0wi2ZANGw==')
task = {'PartitionKey': 'first', 'RowKey': '002','ID': '0002', 'address': 'India','stock':40}
table_service.update_entity('customer1', task)
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World! This is from Python Flask Home Page"

@app.route('/about')
def about():
    cntry = 'India'
    return "<h2> Hello World from About page %s </h2>" %cntry

@app.route('/profile/<name>')
def profile(name):
    return render_template("Profile.html",name=name)
