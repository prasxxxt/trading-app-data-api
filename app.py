from flask import Flask, request
from utils.return_data import *
from utils.update_data import check_collect_data
from utils.collect_data import *
from calculate.summarize import *
app =   Flask(__name__)

json_data = open("./data/data.json")
data = json.load(json_data)
cot = data["cot-data"]
print(cot)
json_data.close()

@app.route('/init', methods = ['GET'])
def init():
    if(request.method == 'GET'):
        check_collect_data()
        response = {}
        for pair in all_pairs:
            response[pair] = get_summary(pair)
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
    
@app.route('/technical', methods = ['GET'])
def technical():
    if(request.method == 'GET'):
        response = return_technical()
        return response
    
@app.route('/seasonality', methods = ['GET'])
def seasonality():
    if(request.method == 'GET'):
        response = return_seasonality()
        return response


        
if __name__=='__main__':
    app.run()