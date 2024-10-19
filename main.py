from textextraction import TextExtract
from description import GenrateText
from FreshRottenDect import FreshRotton
from flask import Flask,jsonify,request
import os

app = Flask(__name__) 

@app.route('/', methods = ['GET'])
def home(): 
    data = "This is an backend Api use Proper request"
    return data
  
@app.route('/tex/<imgp>', methods=['GET']) 
def Tex(imgp):

    imgp = 'images/' + imgp
    
    if not os.path.isfile(imgp):
        return jsonify({'error': 'File not found', 'path': imgp}), 404

    te = TextExtract()
    p = te.Textdata(imgp)

    de = GenrateText()
    res = de.LlmText(p)

    return jsonify({'Extract text': p, 'enhanced text': res})


@app.route('/dect/<path>',methods=['GET'])
def pred(path):

    path='images/'+path

    if not os.path.isfile(path):
        return jsonify({'error': 'File not found', 'path': path}), 404
    
    frd=FreshRotton()
    out=frd.detect(path)
    return jsonify({'response class':out})

if __name__ == '__main__': 
  
    app.run(debug = True) 