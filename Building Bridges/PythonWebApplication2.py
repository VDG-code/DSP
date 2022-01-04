###################################################################################################################################
## get libraries
##import xlrd
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import folium

from flask import Flask, render_template, request 
from flask import send_file
 



###################################################################################################################################
## get data
bridgeData = pd.read_excel('Gemeente Almere bruggen paspoort gegevens.xlsx')

###################################################################################################################################
## Bridge mapping
Bridge_location = pd.read_csv('Bridge.csv')

Bridge_locations = Bridge_location[["Latitude", "Longitude", "Name", "Number"]]




###################################################################################################################################
## app rendering



app = Flask(__name__)  
 
@app.route("/")  
def index():  
     return render_template('index.html')  

@app.route('/Streetmap')
def render_the_map():
    map = folium.Map(location=[Bridge_locations.Latitude.mean(), Bridge_locations.Longitude.mean()], zoom_start=14, control_scale=True)

    for index, location_info in Bridge_locations.iterrows():
        folium.Marker([location_info["Latitude"], location_info["Longitude"]], popup=location_info["Number"]).add_to(map)
    map.save('templates/Streetmap.html')
    
    return render_template('Streetmap.html')
 
  
@app.route('/hello', methods=['POST'])  
def hello():  
    first_name = request.form['first_name'] 
    last_name = request.form['last_name']
    #last_name = bridgeData.iloc[0,1]  
    data=' %s %s ' % (first_name, last_name) 
    
    if (first_name == "Municipality") and (last_name == "Municipality"):
        HTMLtemplate = 'Municipality.html'
    else:
         HTMLtemplate = 'hello.html'
    return render_template(HTMLtemplate,value=data)  
     




if __name__ == '__main__':
    app.run(debug = True)    
if __name__ == '__main__':  
    #app.run(use_debugger=False, use_reloader=False, passthrough_errors=True)  
    app.run('localhost', 4459) 
