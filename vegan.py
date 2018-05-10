import nltk
import json
from textblob import TextBlob
import textblob
import couchdb
from couchdb import Server
from couchdb.design import ViewDefinition
import time
import credentials

class vegan:
  global db
  global timelinedb

  def __init__(self, dbname,):
#    couch = couchdb.Server()
    couchserver = couchdb.Server(credentials.IP)
    
    if dbname in couchserver:
       self.db = couchserver[dbname]
    else:
       self.db = couchserver.create(dbname)
 
  def getVegan(self):
    vegan = 0
    viewName = "generalview"
    for item in self.db.view('tweets/'+viewName):
       try:
          text = item.value
         # print("type of text is : ", text)
          if(text == None):
            continue
          if( isinstance(text, str )):
        #  print("printing data : ",item.key, type(item.value))
          text = item.value
          if("vegan" in text or "vegetarian" in text):
             vegan = vegan +1
       except Exception as e:
          print("exception came ",e)
          pass
    
   print("vegan count is :",vegan  )



