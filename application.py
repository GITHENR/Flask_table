from flask import Flask, render_template
from azure.cosmosdb.table.tableservice import TableService
table_service = TableService(account_name='cloudshell2122165139', account_key='0uelOpdtMmiwzejGvxN+4XprMykfStZP1eywpjFvcJA4BFeDH9pYJTDUM0/x1mBvjSDPOH5186LQsE7Lh6xYLw==')
task = {'PartitionKey': 'first', 'RowKey': '002','ID': '0002', 'address': 'India','stock':20}
table_service.update_entity('customer', task)
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
