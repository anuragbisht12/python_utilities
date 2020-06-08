from flask import Flask,request, url_for, redirect, render_template
import pandas as pd
import pickle
import numpy as np
app = Flask(__name__)

INPUTPATH=r''
df=pd.read_csv(INPUTPATH) 



@app.route('/')
def home():
    return render_template("index.html",keywordvalues='')
@app.route('/generatekeyword/',methods=['POST'])
def generatekeyword(): 
    int_features = [x for x in request.form.values()]
#    id=int_features[0]
    try:
        id=int(int_features[0])
        link=df.iloc[id,:].File
        kw=df.iloc[id,:].keywords
    except:
        link='link not found'
        kw=''
    return render_template("index.html",filelink=link,keywordvalues=kw)
#    return render_template('index.html', pred='{}'.format(kw))
    
    
#    int_features = [x for x in request.form.values()]
#    final = np.array(int_features)
#    data_unseen = pd.DataFrame([final], columns = cols)
#    prediction = predict_model(model, data=data_unseen, round = 0)
#    prediction = int(prediction.Label[0])
#    return render_template('home.html',pred='Expected Bill will be {}'.format(prediction))

#@app.route('/predict_api',methods=['POST'])
#def predict_api():
#    data = request.get_json(force=True)
#    data_unseen = pd.DataFrame([data])
#    prediction = predict_model(model, data=data_unseen)
#    output = prediction.Label[0]
#    return jsonify(output)

if __name__=="__main__":
     app.run(port=5000, debug=True)
