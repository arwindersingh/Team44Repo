import json
from textblob import TextBlob
import textblob
import couchdb
from couchdb import Server
from couchdb.design import ViewDefinition
import time
import credentials

class sentiment:
  global db
  global timelinedb

  def __init__(self, dbname):
   # couch = couchdb.Server()
    couchserver = couchdb.Server(credentials.IP)
    
    if dbname in couchserver:
       self.db = couchserver[dbname]
    else:
       self.db = couchserver.create(dbname)
  
  #method to do sentiments analysis using textblob
  def doSentiment(self):
    viewName = "sentiview"
    polarity = 0
    neg = 0
    pos = 0
    neutral = 0
    for item in db.view('tweets/'+viewName):
     try:
       text = item.value
       print("type of text is : ", text)
       if(text == None):
          continue
       if( isinstance(text, str )):
        #  print("printing data : ",item.key, type(item.value))
          text = item.value
          analyzer = TextBlob(text)
          if(analyzer.sentiment.polarity >0):
               pos+=1
          elif(analyzer.sentiment.polarity<0):
               neg+=1
          elif(analyzer.sentiment.polarity==0):
              neutral+=1
       else:
         print("type not string ", type(text))
     except Exception as e:
          print("exception came ",e)
          pass
     
    print("pos :",pos, "  neg :",neg,"neut  :", neutral,"  total : ",polarity )




