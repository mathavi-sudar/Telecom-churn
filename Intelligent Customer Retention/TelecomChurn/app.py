from flask import Flask, render_template, request
import keras
from keras.models import load_model
import numpy as np


app = Flask(__name__)

model = load_model("telcom_churn.h5")

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/submit')
def predict():
	return render_template('predict.html')

@app.route('/predict',methods=['POST'])
def predicted():
    #x=[[int(x) for x in request.form.values()]]
    #print(x)
    
    #x = np.array(x)
    #print(x.shape)
    
    a = request.form["gender"]
    b = request.form["srcitizen"]
    c = request.form["partner"]
    d = request.form["dependents"]
    e = request.form["tenure"]
    f = request.form["phservices"]
    g = request.form["multi"]
    print(g)
    if (g == "0"):
        g1,g2,g3 = 1,0,0
    if (g== "1"):
        g1,g2,g3 = 0,1,0
    if (g== "2"):
        g1,g2,g3 = 0,0,1
        
    h=request.form["is"]
    if (h== "0"):
        h1,h2,h3 = 1,0,0
    if (h== "1"):
        h1,h2,h3 = 0,1,0
    if (h== "2"):
        h1,h2,h3 = 0,0,1
        
    i = request.form["os"]
    if (i== "0"):
        i1,i2,i3 = 1,0,0
    if (i== "1"):
        i1,i2,i3 = 0,1,0
    if (i== "2"):
        i1,i2,i3 = 0,0,1
        
    j = request.form["ob"]
    if (j== "0"):
        j1,j2,j3 = 1,0,0
    if (j== "1"):
        j1,j2,j3 = 0,1,0
    if (j== "2"):
        j1,j2,j3 = 0,0,1
        
    k = request.form["dp"]
    if (k== "0"):
        k1,k2,k3 = 1,0,0
    if (k== "1"):
        k1,k2,k3 = 0,1,0
    if (k== "2"):
        k1,k2,k3 = 0,0,1
        
    l = request.form["ts"]
    if (l== "0"):
        l1,l2,l3 = 1,0,0
    if (l== "1"):
        l1,l2,l3 = 0,1,0
    if (l== "2"):
        l1,l2,l3 = 0,0,1
        
    m = request.form["stv"]
    if (m== "0"):
        m1,m2,m3 = 1,0,0
    if (m== "1"):
        m1,m2,m3 = 0,1,0
    if (m== "2"):
        m1,m2,m3 = 0,0,1
        
    n = request.form["stm"]
    if (n== "0"):
        n1,n2,n3 = 1,0,0
    if (n== "1"):
        n1,n2,n3 = 0,1,0
    if (n== "2"):
        n1,n2,n3 = 0,0,1
        
    
        
    o = request.form["contract"]
    if (o== "0"):
        o1,o2,o3 = 1,0,0
    if (o== "1"):
        o1,o2,o3  = 0,1,0
    if (o== "2"):
        o1,o2,o3  = 0,0,1
        
    p = request.form["pmt"]
    if (p== "0"):
        p1,p2,p3,p4 = 1,0,0,0
    if (p== "1"):
        p1,p2,p3,p4 = 0,1,0,0
    if (p== "2"):
        p1,p2,p3,p4 = 0,0,1,0
    if (p== "3"):
        p1,p2,p3,p4 = 0,0,0,1
        
    q = request.form["plb"]
    
    r = request.form["mcharges"]
    
    s = request.form["tcharges"]
    
    t= [[int(g1),int(g2),int(g3),int(h1),int(h2),int(h3),
         int(i1),int(i2),int(i3),int(j1),int(j2),int(j3),
         int(k1),int(k2),int(k3),int(l1),int(l2),int(l3),
         int(m1),int(m2),int(m3),int(n1),int(n2),int(n3),
         int(o1),int(o2),int(o3),int(p1),int(p2),int(p3),int(p4),
         int(q),int(r),int(s),int(a),int(b),int(c),int(d),int(e)
         ]]
    
    
    print(t)
    pred = model.predict(t)
    if(pred[[0]]<=0.5):
        return render_template('result.html', prediction_text='NO')
    
    if(pred[[0]]>=0.5):
        return render_template('result.html', prediction_text='YES')


if __name__ == '__main__':
	app.run(debug=True)