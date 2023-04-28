# ## Fonctions utiles
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.models import Panel, Tabs
import numpy as np
import pandas as pd

def season(datetime):
    if (datetime.month < 7):
        return(str(datetime.year - 1) + '/' + str(datetime.year))
    else:
        return(str(datetime.year) + '/' + str(datetime.year + 1))
    
def shot_location(name, df):
    dff = df.loc[df['Player Name'] == name]
    dff["Game Date"] = pd.to_datetime(df['Game Date'],format = '%Y-%m-%d')
    dff['Period'] = dff['Period']*2
    dff['Season'] = dff['Game Date'].apply(lambda x : season(x))
    tabs = []
    for s in dff['Season'].unique():
        source = ColumnDataSource(data = dff.loc[(df['Shot Made Flag'] == 1) & (dff['Season'] == s)])
        source_1 = ColumnDataSource(data = dff.loc[(df['Shot Made Flag'] == 0)   & (dff['Season'] == s)])
        p = figure(outer_width = 500,outer_height = 470,x_range = [-250,250],y_range = (-40,430)
        ,background_fill_color = "#ba926c")
        p.grid.grid_line_color= "#ba926c"
        p.circle(source = source, x = 'X Location',y = 'Y Location',fill_color = 'green'
            ,size = 'Period',fill_alpha = 0.7, line_color = 'green',
            legend_label = 'Shot in' + ' ' + str(np.round(dff.loc[dff['Season'] == s]['Shot Made Flag'].mean()*100,2)) + '%')
        p.circle(source = source_1, x = 'X Location',y = 'Y Location',fill_color = 'red',
            size = 'Period',fill_alpha = 0.7, line_color = 'red',
            legend_label = 'Shot out' + ' ' + str(100-np.round(dff.loc[dff['Season'] == s]['Shot Made Flag'].mean()*100,2)) + '%')
        p.line([-80,-80,80,80],[-70,150,150,-70],line_width = 1.5,color='black')
        p.line([-220,-220],[-70,94],line_width = 1.5,color='black')
        p.line([220,220],[-70,96],line_width = 1.5,color='black')
        x = np.arange(-220,220,1)
        y = np.sqrt((239**2) - x**2)
        p.line(x,y,line_width = 1.5,color='black')
        p.circle(0,430,size = 150,fill_color = "#ba926c",line_color='black',line_width = 1.5)
        p.circle(0,430,size = 2,color='black')
        p.legend.click_policy = 'hide'
        tabs.append(Panel(child=p,title=str(s)))
    tab = Tabs(tabs=tabs)
    return tab
