<<<<<<< HEAD
#! python3

#The pg100.txt file can be downloaded in Project Gutenberg page at https://www.gutenberg.org/ebooks/100.txt.utf-8
#William Shakespeake's works are now public domain. 

import tweepy
import time

def remember_where_stop(linenumber):
    r = open("remember.txt","w")
    r.write(str(linenumber))
    r.close
    
def where_stop():
    try:
        r = open("remember.txt","r")
        ll = int(r.readline().strip())
        r.close
        return ll
    except:
        return 0

consumer_key="[INSERT YOUR DATA HERE]"
consumer_secret="[INSERT YOUR DATA HERE]"
access_token_key="[INSERT YOUR DATA HERE]" #use shakespearepi_gettoken.py to get this data
access_token_secret="[INSERT YOUR DATA HERE]" #use shakespearepi_gettoken.py to get this data

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token_key,access_token_secret)

api = tweepy.API(auth)

f = open("pg100.txt")
lastline = 0
stopedat = where_stop()
print("Interrompido na linha:" , stopedat)


for line in f:
    lastline += 1
    if not(line.strip() == ""):
        if lastline > stopedat:                  
            print(line.strip())
            api.update_status(line.strip())
            remember_where_stop(lastline)
            time.sleep(180) 
            
=======
#! python3
import tweepy
import time

def remember_where_stop(linenumber):
    r = open("remember.txt","w")
    r.write(str(linenumber))
    r.close
    
def where_stop():
    try:
        r = open("remember.txt","r")
        ll = int(r.readline().strip())
        r.close
        return ll
    except:
        return 0

consumer_key="[INSERT YOUR DATA HERE]"
consumer_secret="[INSERT YOUR DATA HERE]"
access_token_key="[INSERT YOUR DATA HERE]"
access_token_secret="[INSERT YOUR DATA HERE]"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token_key,access_token_secret)

api = tweepy.API(auth)

f = open("pg100.txt")
lastline = 0
stopedat = where_stop()
print("Interrompido na linha:" , stopedat)


for line in f:
    lastline += 1
    if not(line.strip() == ""):
        if lastline > stopedat:                  
            print(line.strip())
            api.update_status(line.strip())
            remember_where_stop(lastline)
            time.sleep(180) 
            
>>>>>>> origin/master
