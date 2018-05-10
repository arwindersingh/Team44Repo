import urllib3
import json
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import credentials
import datetime
import time
from sentiment import sentiment
from vegan import vegan

global cdb

class StdOutListener(tweepy.StreamListener):

  def test():
    print("test")
 

if (__name__ == "__main__"):
   try:
    # cdb = sentiment("nswcandb", "timelinedb") 
      cdb = vegan(credentials.DB) 
#     cdb.createView("sentiview")
#     cdb.doSentiment()
      cdb.getVegan()
   except Exception as e:
       print("Exception main : ",e)  
