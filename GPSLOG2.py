#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import pandas as pd
import sys

args = sys.argv

while 1:
        s = serial.Serial('/dev/serial0', 9600, timeout=10)
        s.readline()
        sentence = s.readline().decode('utf-8')
        li = sentence.split(',')
        print(li)
        data1= '$GPGLL'
        if data1 in li:
                print(li)
                timeutc = li[5]
                #longitude:経度、latitude:緯度
                lat = li[1]
                lon = li[3]
                w = pd.DataFrame([[timeutc,lat,lon]])
                w.to_csv(args[1],index=False,encoding="utf-8",mode='a',header=False)
