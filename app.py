from flask import Flask,jsonify,request
from scrapper import *
import concurrent.futures

app =   Flask(__name__)
  
@app.route('/fundamental-data', methods = ['GET'])
def return_fundamental():
    if(request.method == 'GET'):
        
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for i in fundamental_urls:
                executor.submit(get_fundamental_data, i)
  
        return jsonify(fundamental_data)
    
@app.route('/cot-data', methods = ['GET'])
def return_cot():
    if(request.method == 'GET'):
        
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for j in cot_currency_codes:
                executor.submit(get_cot_data, j)
  
        return jsonify(cot_data)
    
@app.route('/retail-data', methods = ['GET'])
def return_retail():
    if(request.method == 'GET'):
        
        get_retail_data()
  
        return jsonify(retail_data)
  
if __name__=='__main__':
    app.run()