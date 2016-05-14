#!/usr/bin/python3
# coding=UTF-8
import tweepy
import time
import RPi.GPIO as GPIO

#The pg100.txt file can be downloaded in Project Gutenberg page at https://www.gutenberg.org/ebooks/100.txt.utf-8
#William Shakespeake's works are now public domain.

#LED GPIO Definitions

ledgreen = [2,3,4]
ledyellow = [17,27]
ledred = [22,10,11]
buzzer = 9

#GPIO Init
GPIO.cleanup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
for l in ledgreen:
    GPIO.setup(l, GPIO.OUT)
    GPIO.output(l, False)
for l in ledyellow:
    GPIO.setup(l, GPIO.OUT)
    GPIO.output(l, False)    
for l in ledred:
    GPIO.setup(l, GPIO.OUT)
    GPIO.output(l, False)    
GPIO.setup(buzzer, GPIO.OUT)
GPIO.output(buzzer, False)

### ***Functions*** ###

#Lembra-se de onde parou para continuar depois
def remember_where_stop(linenumber):
    r = open("remember.txt","w")
    r.write(str(linenumber))
    r.close

#Recupera o numero da linha que parou
def where_stop():
    try:
        r = open("remember.txt","r")
        ll = int(r.readline().strip())
        r.close
        return ll
    except:
        return 0

#Grava arquivo de log
def dolog(logtext):
    try:
        l = open("logshakespeare.txt","a")
        l.write(logtext + "\n")
        l.close
    except:
        print("Erro gravando log", logtext)
        
#Piscar LED Normal por s segundos
def blinkgreen(s):
    for i in range(0,s):
        for l in ledgreen:
            GPIO.output(l, True)
            time.sleep(1/len(ledgreen))
            GPIO.output(l, False)
            
#Acender ou Apaga todos os leds verdes
def solidgreen(s):
    for l in ledgreen:
        GPIO.output(l,s) 
            
#Piscar LED Amarelo por s segundos
def blinkyellow(s):
    for i in range(0,s):
        for l in ledyellow:
            GPIO.output(l, True)
        time.sleep(0.3)
        for l in ledyellow:    
            GPIO.output(l, False)
        time.sleep(0.7)            

#Piscar LED Vermelho por s segundos. Também toca o Buzzer a cada minuto, caso esteja entre as 9:00 e 23:00
def blinkred(s):
    for i in range(0,s):
        for l in ledred:
            GPIO.output(l, True)
            time.sleep(0.4/len(ledred))
        for l in ledred:
            GPIO.output(l, False)
            time.sleep(0.4/len(ledred))
        if (i % 60 == 0) and (time.localtime().tm_hour > 8) and (time.localtime().tm_hour < 24):
            GPIO.output(buzzer,True)
            time.sleep(0.2)
            GPIO.output(buzzer,False)
        else:
            time.sleep(0.2)

#MAIN PROGRAM

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
    duplicado = False
    lastline += 1
    if not(line.strip() == ""):
        if lastline > stopedat:
            solidgreen(True)
            dolog(line.strip() + " " + str(lastline))
            continuar = True
            while continuar:
                try:
                    api.update_status(line.strip())
                    remember_where_stop(lastline)
                    continuar = False
                except tweepy.error.TweepError as e:
                    dolog('Erro ao tuitar:' + str(e))
                    if e.api_code == 187:
                        continuar = False
                        dolog('Tuíte duplicado, passando para o próximo')
                        duplicado = True
                    else:
                        continuar = True
                        dolog ('Aguardando para tentar novamente')
                        blinkred(300)
                solidgreen(False)
                if duplicado:
                    blinkyellow(45)
                else:
                    blinkgreen(45)
