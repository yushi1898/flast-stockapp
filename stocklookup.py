import requests
import pandas as pd
from bokeh.plotting import figure, output_file, show

def plotstockprice(plotitem,ticker):
    APIkey = 'yQzj7vQce7HxogcAzG71'
    colorlist = ['blue','green','red','orange']
    baseurl = 'https://www.quandl.com/api/v3/datasets/WIKI/'
    
    furl = baseurl+ticker+'.json?'+'start_date=2017-01-01&api_key='+APIkey
    
    stockseries = requests.get(furl).json()
    
    pricetable=stockseries['dataset']['data']
    column_names = [x.lower().replace('. ','_') for x in stockseries['dataset']['column_names']]
    
    
    
    stockprice = pd.DataFrame(pricetable, columns = column_names)
    
#    output_file('graph.html')
    p=figure(title='Quandl WIKI EOD Stock Prices - 2017',x_axis_label ='date', y_axis_label = 'Price',x_axis_type='datetime')
    dateseries = pd.to_datetime(stockprice['date'].to_list())
    for item in plotitem:
        linecolor = colorlist[plotitem.index(item)]
        priceseries = stockprice[item].to_list()
        p.line(dateseries,priceseries,legend=ticker+':'+item,color=linecolor)
    
    return p
#    show(p)