# Make a python class that will fetch one’s photo on giving
# roll number as an input to photos.iitm.ac.in. The output should be an
# image and the input should be given through the command line.
# IITM Students, by roll number:
# https://photos.iitm.ac.in/byroll.php?roll=AA00A000
# IITM Employees, by Employee ID:
# https://photos.iitm.ac.in/byid.php?id=000000

import sys
from datetime import date
import urllib.request

roll = sys.argv[1]

url = "https://photos.iitm.ac.in/byroll.php?roll=" + roll

r = urllib.request.urlopen(url)

with open("picture.jpg", "wb") as f:
    f.write(r.read())
