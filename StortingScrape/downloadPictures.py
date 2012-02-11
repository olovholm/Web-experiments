# -*- coding: utf-8 -*-
from urllib2 import urlopen
from urllib import urlretrieve
import os

'''
This script is dependent on output-file created by findPerId.py. Reads through
file generated and downloads pictures based on the MP's ident. 
Creates new folder "repr_pictures/" if not existent and saves for each MP a 
small and large picture. 
'''

f = open("stortingsrepr.txt","r")

path_big_pre = "http://stortinget.no/Personimages/PersonImages_Large/"
path_big_post = "_stort.jpg"
path_little_pre = "http://stortinget.no/Personimages/PersonImages_Small/"
path_little_post = "_lite.jpg"

out_folder = "repr_pictures/"
if not os.path.exists(out_folder):
    os.makedirs(out_folder)
    
for line in f:
    (etternavn, fornavn, ident) = line.split(';')
    ident = ident.rstrip()
    print "Downloading image of: ",fornavn, etternavn
    filename_big = path_big_pre+ident+path_big_post
    filename_little = path_little_pre+ident+path_little_post
    done_big = out_folder+ident+"_stort.jpg"
    done_little = out_folder+ident+"_lite.jpg"
    urlretrieve(filename_big, done_big)
    urlretrieve(filename_little, done_little)
    
f.close()
    
    