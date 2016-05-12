#! python3
# coding=UTF-8
import tweepy
import time

#The pg100.txt file can be downloaded in Project Gutenberg page at https://www.gutenberg.org/ebooks/100.txt.utf-8
#William Shakespeake's works are now public domain. 

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
        
def dolog(logtext):
    try:
        l = open("logshakespeare.txt","a")
        l.write(logtext + "\n")
        l.close
    except:
        print("Erro gravando log", logtext)

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
dolog('Interrompido na linha: ' + str(stopedat))

for line in f:
    lastline += 1
    if not(line.strip() == ""):
        if lastline > stopedat:
            dolog(line.strip() + " " + str(lastline))
            continuar = True
            while continuar:
                try:
                    api.update_status(line.strip())
                    remember_where_stop(lastline)
                    continuar = False
                except tweepy.error.TweepError as e:
                    dolog('Erro ao tuitar:' + e)                    
                    if e.api_code == 187:
                        continuar = False
                        dolog('Tuíte duplicado, passando para o próximo')
                    else:
                        continuar = True
                        dolog ('Aguardando para tentar novamente')
                        time.sleep(180)
                time.sleep(45) 
                    
