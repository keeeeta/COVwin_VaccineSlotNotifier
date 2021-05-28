import datetime
from datetime import date
import requests
import time
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62'}
d = date.today().strftime("%d-%m-%Y")

p=0


    
api = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=<YOUR_DISTRICT_ID>&date='+str(d)
ap= api+str(d)
r= requests.get(ap,headers=headers).json()   
centers = r['centers']

for c in centers:
    sess=c['sessions']
    res=''
    for s in sess:
        if s['available_capacity_dose1'] > 0 or s['available_capacity_dose2'] >0 :
            res+="DATE: "+str(s['date'])+"\n"
            res+="VACCINE : "+str(s['vaccine'])+"\n"
            res+="MINIMUN AGE: "+str(s['min_age_limit'])+"\n"                
           #res+="CENTER ID: "+str(c['center_id'])+"\n"
            res+="PINCODE: "+str(c['pincode'])+"\n"
            res+="CENTER NAME:  "+str(c['name'])+"\n"
            res+="AREA : "+str(c['block_name'])+"\n"
            res+="FEE TYPE : "+str(c['fee_type'])+"\n"
            res+="DOSE1 AVAILABLE SLOTS: "+str(s['available_capacity_dose1'])+"\n"
            res+="DOSE2 AVAILABLE SLOTS: "+str(s['available_capacity_dose2'])+"\n"
            res+="TIME SLOTS:\n"
            i=1
            for t in s['slots']:
                res+="\t"+str(i)+". "+str(t)+"\n"
                i=i+1
            res+="\n"
            res+="----------------------------------------\n\n"
    
    url='https://api.telegram.org/bot<BOT_TOKEN>/sendMessage?chat_id=<CHAT_ID>&text={}'.format(res)  
    requests.get(url,headers=headers)  
    time.sleep(3)   
    
    #time.sleep(4) 
        
    
