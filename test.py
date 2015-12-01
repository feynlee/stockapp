from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure
from bokeh.embed import components
import requests
import simplejson as json
import pandas as pd
import urllib2

# app = Flask(__name__)

# app.vars={}




api_url = 'https://www.quandl.com/api/v1/datasets/WIKI/%s.json' %'GOOG'
session = requests.Session()
session.mount('http://', requests.adapters.HTTPAdapter(max_retries=3))
raw_data = session.get(api_url)
json_data = raw_data.json()
# stock_data = json_data['data']
# stock_column = [json_data['column_names']]
# stock_combined = json_data['data']
# pd_column = pd.DataFrame(stock_column)
# pd_data = pd.DataFrame(stock_data)
# pd_combined = pd.DataFrame(stock_combined)
pd_combined = pd.DataFrame(json_data['data'], columns=json_data['column_names'])
plot = figure(title='Data from Quandle WIKI set', x_axis_label='date', x_axis_type='datetime')
plot.line(pd_combined['Date'], pd_combined['Open'], line_color='red')
# content = json.dumps(json_data)
# with open('~/OneDrive/Programming/Python/Dataincubator/flask-demo/data.txt', 'w') as f:
    # f.write(content)

# json_object = urllib2.urlopen('https://www.quandl.com/api/v1/datasets/WIKI/GOOG.json')

# json_object
        # data = pd.read_json(raw_data)
# json_data=json.load(json_object)
# data = pd.read_json(json_data)
# json_data

        #
        # plot = figure(
        #       # tools=TOOLS,
        #       title='Data from Quandle WIKI set',
        #       x_axis_label='date',
        #       x_axis_type='datetime')

        # app.vars['Open']=request.form['Open']
        # app.vars['Close']=request.form['Close']
        # app.vars['Adj_Open']=request.form['Adj. Open']
        # app.vars['Adj_Close']=request.form['Adj. Close']

# print(json_data['Open'])
# print(json_data)


        # f = open('data.txt','w')
        # f.write('tiker: %s\n%s\n%s\n%s\n%s\n'%(app.vars['ticker'],app.vars['Open'],app.vars['Close'],app.vars['Adj_Open'],app.vars['Adj_Close']))
        # f.close()

        # script, div = components(plot)
        # return render_template('graph.html', script=script, div=div)
        # return 'request.method was not a GET!'

# @app.route('/graph',methods=['GET','POST'])
# def index():
#     if request.method == 'GET':
#         return render_template('index.html')
#     else:
#         app.vars['ticker']=request.form['ticker_name']
#         f = open('data.txt','w')
#         f.write('tiker: %s/n'%app.vars['ticker'])

