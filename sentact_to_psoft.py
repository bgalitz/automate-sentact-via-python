#selenium imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#need os for file moving and renaming when complete
import os
#need datetime to timestamp filename
import datetime

driver = webdriver.Firefox()
#open nmi
driver.get(#insert nmi address here!!!)
#login to nmi
elem = driver.find_element_by_name(#username?)
elem.send_keys("username")
elem = driver.find_element_by_name(#password?)
elem.send_keys("password")
elem.send_keys(Keys.RETURN)
#navigate to express issue page


#open sentact file for reading data
f = open("sentact.txt","r")

#open txt file to write error log
e = open("errorlog.txt","w")

location = "Sentact"
bu = "NM301"

for line in f:
    sentact_filled = line.split(",")
    dept = sentact_filled[0]
    psoft_num = sentact_filled[1]
    qty = sentact_filled[2]

    #do we need to import time and sleep for x seconds

    #selenium find BU box
    elem = driver.find_element_by_name(#incomplete)
    #selenium send BU
    elem.send_keys(bu)
    #selenium find dept box
    elem = driver.find_element_by_name(#incomplete)
    #selenium send dept
    elem.send_keys(dept)
    #selenium find location box
    elem = driver.find_element_by_name(#incomplete)
    #selenium send location
    elem.send_keys(location)
    
    #selenium find psoft box
    elem = driver.find_element_by_name(#incomplete)
    #selenium send psoft
    elem.send_keys(psoft)
    #must check for psoft error? how?
    #if error - write to error file with string "psoft item number issue"
    e.write("Dept: %s Psoft Num: %s Qty: %s -- psoft item issue\n" % (dept, psoft_num, qty))
    
    #selenium find qty box
    elem = driver.find_element_by_name(#incomplete)
    #selenium send qty
    elem.send_keys(qty)
    #must check for qty error? how?
    #if error --write info to error file with string "qty discrepancy"
    e.write("Dept: %s Psoft Num: %s Qty: %s -- qty discrepancy\n" % (dept, psoft_num, qty))

#once there are no more lines to read close the sentact file
f.close()

#at this point there should be no more lines to write either - close the error log
e.close()

#close firefox - we're done with peoplesoft
driver.close()

#get the datetime   
now = datetime.datetime.now()

#navigate to the directory and rename the file so we know it's complete
#need complete filename
os.rename("sentact.txt", "%d_COMPLETE_sentact" % now))
