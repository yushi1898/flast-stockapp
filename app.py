# -*- coding: utf-8 -*-

from flask import flask, render_template, request, url_for,redirect
from stocklookup import plotstockprice
from bokeh.embed import components

app = Flask(__name__)
app.vars={}



@app.route('/')
@app.route('/index', methods=['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        app.vars['ticker']=request.form['ticker']
        app.vars['plotitem']=request.form.getlist('plotitem')
        return redirect('/graph')
    
    
@app.route('/graph',methods=['GET','POST'])
def graph():
    if request.method == 'GET':
        plot = plotstockprice(app.vars['plotitem'],app.vars['ticker'])
        script, div = components(plot)
        return render_template('graph.html',script = script, div = div)
    
    
    
if __name__ == '__main__':
  app.run(debug=True)
