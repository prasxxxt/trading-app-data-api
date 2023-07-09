from flask import Flask,jsonify,request
from scrapper import *
from utils import *
from summarize import *
app =   Flask(__name__)

@app.route('/init', methods = ['GET'])
def init():
    if(request.method == 'GET'):
        collect_data()
        response = return_summary()
        return response

@app.route('/retail', methods = ['GET'])
def retail():
    if(request.method == 'GET'):
        response = return_retail()
        return response

@app.route('/cot', methods = ['GET'])
def cot():
    if(request.method == 'GET'):
        response = return_cot()
        return response

@app.route('/fundamental', methods = ['GET'])
def fundamental():
    if(request.method == 'GET'):
        response = return_fundamental()
        return response


        
if __name__=='__main__':
    app.run()