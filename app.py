from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure
from bokeh.embed import components
import simplejson as json
# import pandas as pd
import Quandl

app = Flask(__name__)


@app.route('/')
def main():
    return redirect('/index')


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        r = request.form
        stock = r['ticker_name']
        options = ['Close', 'Adj. Close', 'Open', 'Adj. Open']
        selectoptions = []
        for item in options:
            if item in r:
                selectoptions.append(item)

        with open("Quandl.json.nogit") as fh:
            secrets = json.loads(fh.read())
        api_key = secrets['api_key']
        mydata = Quandl.get('WIKI/'+stock, authtoken=api_key)

        plot = figure(
            # tools=TOOLS,
            title='Data from Quandle WIKI set',
            x_axis_label='date',
            x_axis_type='datetime')

        colorselect = dict(
            [('Close', 'blue'), ('Adj. Close', 'green'), ('Open', 'orange'),
             ('Adj. Open', 'red')])
        for item in selectoptions:
            plot.line(
                x=mydata.index.tolist(),
                y=mydata[item],
                line_color=colorselect[item],
                legend=stock+": "+item)
        # plot.legend.orientation = "top_left"

        # print(r)
        # print(selectoptions)

        script, div = components(plot)
        return render_template(
            'graph.html',
            script=script,
            div=div,
            stock=stock)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(port=33507)
