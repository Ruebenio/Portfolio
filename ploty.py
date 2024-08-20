import pandas as pd
import plotly.express as px
import plotly.io as pio

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 12)
pd.set_option('display.width', 400)

pd.options.mode.copy_on_write = True

def plot (dataframe,title) :
  
  dataframe = dataframe.loc[0:120,:]
  dataframe['date'] = pd.to_datetime(dataframe['date'])
  plot_data = dataframe.sort_values(by='date')
 
  # Creating the Plotly figure
  fig = px.line(plot_data, x='date', y='value', title=f'{title}')

  # Converting Plotly figure to an image (PNG format)
  img_bytes = pio.to_image(fig, format="svg")

  # Saving the image to a file
  with open(f'static/currency/images/{title}.svg', "wb") as img_file:
      img_file.write(img_bytes)


#return Bitcoin CAD price change rate over four months
def dates (data) :
  data_sub = data.loc[0:120,:]

  data_sub['date'] = pd.to_datetime(data_sub['date'])
    
  data_sub['date']=data_sub['date'].dt.strftime('%Y-%m-%d')
  
  dates = []
  
  s_date = data_sub.loc[0, ['date'][0]]
  e_date = data_sub.loc[120, ['date'][0]]

  dates.append(s_date)
  dates.append(e_date)
  
  return dates
  
#Calculating basic statistics
def stats (data) :
  data_sub = data.loc[0:120,:]

  min = round(data_sub['value'].min(),2)
  max = round(data_sub['value'].max(),2)
  std = round(data_sub['value'].std(),2)
  mean = round(data_sub['value'].mean(),2)
  curr_price = data_sub['value'][0]

  #Defining the first and thrid quartile
  q1 = data_sub['value'].quantile(0.25)
  q3 = data_sub['value'].quantile(0.75)

  # Calculating the Interquartile range
  iqr = q3 - q1
 
  # Define the lower and upper bounds for outliers
  lower_bound = q1 - 1.5 * iqr
  upper_bound = q3 + 1.5 * iqr

   # Calculating the outliers
  outliers = data_sub[(data_sub['value'] < lower_bound) | (data_sub['value'] > upper_bound)]

  statis = {'cur_price' : curr_price,'min': min, 'max': max, 'std': std,'mean': mean} 
  
  return statis