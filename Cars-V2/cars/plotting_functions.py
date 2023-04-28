# Load the current model:
import pandas as pd
import plotly.express as ex

def isBase(row):
    if row == 0:
        return 'Base'
    if row != 0:
        return 'Lux'

df = pd.read_pickle('data/cleaned_cars_db.pickle')
def getPlot(brand,mileage,year,df,year_range=1, mileage_range=15000,count=0):
    if count ==1500:
        with(open('output.html')) as file:
            file.write('<h1> There is no available results for the inputs </h1>')
        return None
    temp = df[df['manufacturer']==brand]
    year_index = (temp['year']>=year-year_range) & (temp['year']<=year+year_range)
    odometer_index = (temp['odometer']>=mileage-mileage_range) & (temp['odometer']<=mileage+mileage_range)
    ind = year_index & odometer_index
    
    plotly_df = temp[ind].copy()
    if len(plotly_df)<3:
        return getPlot(brand=brand,mileage=mileage,df=df,
                       year=year,year_range=year_range+1,
                       mileage_range=mileage_range+10000,count=count+1)
    
    plotly_df['year'] = plotly_df['year'].astype(int).astype(str)
    plotly_df.sort_values('year',inplace=True)
    plotly_df['model'] = plotly_df['model1'].apply(lambda x: f'{brand} ' +x)
    plotly_df['trim_size'] = plotly_df['trim'].apply(lambda x: x/10 + 0.1)
    plotly_df['Trim'] = df['trim'].apply(isBase)
    
    fig = ex.scatter(plotly_df, x='odometer',y='price',color='year',
                 size='trim_size', size_max=10,
                 hover_name='model', 
                 hover_data={'trim_size':False,'Trim':True},
                 title =f'Similar Prices for {brand} Vehicles')
    fig.update_layout(title_x=0.5)
    
    print(len(plotly_df))
    
    return fig.write_html('static/plotly/output.html',full_html=False)
