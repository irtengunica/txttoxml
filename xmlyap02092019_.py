#!/usr/bin/python

import xml.etree.ElementTree as ET
import argparse
import sys
import glob
import os
import numpy as np
import cv2
import json 
import urllib.request


#engin
with open("response1.json") as json_file1:
 dosyalistesi=json.load(json_file1)
dosyasayisi= len(dosyalistesi)-1
#print(dosyalistesi)
#print(dosyasayisi)
frame_idlist=[]
secilendosyalist=[]
resimadilist=[]
for item in dosyalistesi:
 frame_idlist=frame_idlist+[(item['frame_id'])]
 secilendosya=item['frame_link']
 dosyaAdi = secilendosya.replace("http://212.68.57.202/images/", "")
 dosyaAdi5 = dosyaAdi.replace("B23072019_V1_K1/", "")
 dosyaAdi5 = dosyaAdi.replace("T190619_V4_K1/", "")
 #resimadi = dosyaAdi5.replace(".jpg", "")
 resimadi = dosyaAdi5
 secilendosyalist=secilendosyalist+[dosyaAdi]
 resimadilist=resimadilist+[resimadi]
 #dosyasayisi=dosyasayisi-1
print(secilendosyalist,frame_idlist,resimadilist)
#print((frame_idlist))
dx=0
