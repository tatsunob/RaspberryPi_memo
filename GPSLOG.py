#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import datetime
from math import modf
import pandas as pd


while 1:
        s = serial.Serial('/dev/serial0', 9600, timeout=10)
        s.readline()
        sentence = s.readline().decode('utf-8')
        li = sentence.split(',')
        data1= '$GPRMC'
        if data1 in li:
                print(li)
                timeutc=li[1]
                timeutc=map(str,timeutc)
                hour=timeutc[0]+timeutc[1]
                minute=timeutc[2]+timeutc[3]
                second=timeutc[4]+timeutc[5]
                jst=datetime.datetime(100,1,1,int(hour),int(minute),int(second))
                deff= datetime.timedelta(hours=9)
                jst=jst+deff
                #longitude:経度、latitude:緯度
                lat2 =float(li[3])
                lon2 =float(li[5])
                syousu, seisu = modf(lat2)
                syousu1,seisu1=modf(seisu/100)
                lat = seisu1+(syousu1*100+syousu)/60
                syousu2, seisu2 = modf(lon2)
                syousu3,seisu3 =modf(seisu2/100)
                lon = seisu3+(syousu3*100+syousu2)/60
                #print(jst.time())
                #lon=str(lon)
                #lat=str(lat)
                w = pd.DataFrame([[jst.time(), lat, lon]])
                w.to_csv("GPSLOG.csv", index=False, encoding="utf-8", mode='a', header=False)
