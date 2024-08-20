from flask import Flask, render_template, request, redirect, url_for
import nasdaqdatalink
import pandas as pd
import plotly.express as px
import plotly.io as pio
from ploty import plot,dates,stats
from rates import rate,appr
import os
import random
from space import people_space
from weather import temp
from harry import get_char
import json
import urllib.request
from twilio.rest import Client
from get_country import country
from get_iss import iss_loc 
from get_weather import get_weather
from get_address import address
from get_country import country
from get_distance import dist

app = Flask('app')

#Flask activation of home page
@app.route('/')
def index():
    
    return render_template('index.html')


#Flask activation of home page Bitcoin graphs and maps
@app.route ('/curr')
def curs():

    try :
      
        #Saving the API key
        nasdaqdatalink.ApiConfig.api_key = os.environ['NASDAQ_KEY']
        # nasdaqdatalink.ApiConfig.api_key = 'X1xxhhECwuyNPezdQtmg'
        #Saving the Bitcoin Trade Volume vs Transaction Volume dataframe
        TVTVR_data = nasdaqdatalink.get_table('QDL/BCHAIN', code='TVTVR')
    
        #Saving the Bitcoin price over time dataframe
        MKPRU_data = nasdaqdatalink.get_table('QDL/BCHAIN', code='MKPRU')
    
    
      #Graphing the Bitcoin Trade Volume vs Transaction Volume ratio over time using the ploty library
        title = 'Bitcoin Trade Volume vs Transaction Volume Ratio Graph'
        TVTVR_sub = plot(TVTVR_data,title)
    
        #Graphing the Bitcoin price over time using the ploty library
        MKPRU_title = 'Bitcoin Price over time'
        MKPRU_sub = plot(MKPRU_data,MKPRU_title)
    
        #Extracting the dates from the Bitcoin price over time dataframe
        MKPRU_sub = dates(MKPRU_data)
    
        print (MKPRU_sub)
        #Calculating the Bitcoin price change rate over four months
        MKPRU_appr = appr(MKPRU_sub)
    
        print(MKPRU_appr)
    
        #Calculating the BTC/CAD rate
        cur_rate = rate(MKPRU_sub)
    
        #Calculating basic statisitcs of the bitcoin price.
        MKPRU_stats = stats(MKPRU_data)
        print (MKPRU_stats)
    
      #Calculating basic statisitcs of the bitcoin price
        TVTVR_stats = stats(TVTVR_data)
        print (TVTVR_stats)

    except Exception as e:
        print(f'The error : {e} ocurred while retrieving the data.Please try again at a later time.')

  # Rendering the template and passing the variables via Jinga
    return render_template ('curr.html' , min = MKPRU_stats['min'], max= MKPRU_stats['max'], std = MKPRU_stats['std'], avg = MKPRU_stats['mean'] ,start_dt = MKPRU_sub[1],end_dt = MKPRU_sub[0] , rate = cur_rate, appr = MKPRU_appr,curpr = MKPRU_stats['cur_price'],tvtvr_min = TVTVR_stats['min'],tvtvr_max = TVTVR_stats['max'],tvtvr_std= TVTVR_stats['std'],tvtvr_avg = TVTVR_stats['mean'],bit_plot = MKPRU_sub, mkpru_plot = TVTVR_sub)


#Flask activation of home page Harry Porter & Twilio
@app.route('/twiliohp')
def twiliohp():
    char = get_char()
    name, image, actor = char[0],char[1],char[2]
    status = ''

    if not image :
      status ='No Image found'
    else :
        status ='Image found'
    if not actor :
        actor = 'Name not avaialable'

    space_num = people_space()
    city = 'Tema'
    weather = temp(city)

    return render_template('twiliohp.html', name=name, image=image, actor=actor, space_num=space_num, city=city, weather=weather,status=status)

#Flask activation of response page
@app.route('/response')
def response():
    return render_template('response.html')

#Flask activation of message
@app.route('/send_message', methods=['POST'])
def send_message():
    char = get_char()
    name, image, actor = char[0], char[1], char[2]
    i_na = 'Image not available'
    n_na = 'Name not available'
    if image == "":
      image = i_na

    if actor == "":
      actor = n_na

    space_num = people_space()
    city = 'Tema'
    weather = temp(city)

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    msg = f'The name of the actor, {name} ({image}), is {actor}. With {space_num} people in space, the weather in {city} is {weather} degrees Celsius.'

    message = client.messages.create(
        body=msg,
        from_='+12075485667',  # your Twilio number
        to='+17059237766'  # the receiver's phone number
    )
    log_res = f'SID :{message.sid} \nMessage :{msg} \nFrom: {message.from_} \nTo : {message.to}\n\n'

    #Saving the Twilio response to a txt file
    with open('message.txt', 'a') as outfile:  
        outfile.write(log_res)

#Printing twilio message response
    print(message.sid)
    return redirect(url_for('response'))

#Flask activation of space and weather homepage
@app.route('/spaceweather')
def spaceweather():
  data = iss_loc()
  lat,lon,loct = data[0],data[1],data[2]

  # Weather description
  weather =get_weather(lat,lon)
  temp_c = round(weather["main"]["temp"]-273.15,2)
  description = weather["weather"][0]["description"]
  print(str(temp_c) + " C " + description)

  #Creating a Random choice for the water picture
  sea = ['sw1','sw2','sw3','sw4']
  pic = random.choice(sea)
  flag = ""

  #address reverse geolocation
  add = address(lat,lon)

  #finding the country name
  cn = add['countryName']
  if cn == "":
    cn = "water"
  else :
    cn = cn


  #Setting conditions to display country flag or water image 
  print("Country Code is :",add["countryCode"])
  if(add["countryCode"]==""):
    location = 'water'
    print("The ISS is over Water")
    flag = f"static/spaceweather/images/{pic}.jpg"


  else:
    location= add["countryCode"]
    flag= country(location)[0]["flags"]["png"]
    print(flag)

  #Distance between ISS and me at Cambrian College 
  distance = dist(lat,lon,46.524757901,-80.9379729148)
  print(f"You are {distance} km from ISS !")

  # Rendering the template and passing the variables via Jinga
  return render_template('spaceweather.html',lat=lat,lon =lon,temp_c=temp_c,description=description,location=location,flag=flag,distance=distance,cn=cn,loct = loct)
    
app.run(host='0.0.0.0', port=8080, debug= False)