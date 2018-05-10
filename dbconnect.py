import json
import couchdb
from couchdb import Server
from couchdb.design import ViewDefinition

class dbconnect:
  global db
  global timelinedb

  def __init__(self, dbname, timelinedbname):
    couch = couchdb.Server()
    couchserver = couchdb.Server('http://admin:rave@localhost:5984/')
    if timelinedbname in couchserver:
       self.timelinedb = couchserver[timelinedbname]
    else:
       self.timelinedb = couchserver.create(timelinedbname)
    
    if dbname in couchserver:
       self.db = couchserver[dbname]
    else:
       self.db = couchserver.create(dbname)
  
  def getDBInfor(self):
      print("db infor is : ",self.db.info())
  
  def saveToDB(self, data):
    self.db[str(data["id"])] = data
    print("data should be saved")
  
  def saveTimeline(self,data):
     print("data to write to timeline : ", type(data))
     for tweets in data:
        tweet = json.dumps(tweets._json)
        tw = json.loads(tweet)
        try:
          self.timelinedb[str(tw["id"])] = tw
          print(tw["id"],"   timeline should be saved") 
        except Exception as e:
          print(tw["id"],"exception while writing timeline ", e)
          pass 

  def getUserTimeline(self, api): 
    viewName = 'uniqueuserview'
    count = 0
    for item in self.db.view('tweets/'+viewName):
      doc = self.db.get(item.id)
      uid = item.key
      if(item.value == None):
         count = count + 1
         data = api.user_timeline(user_id = uid,count = 200) 
         self.saveTimeline(data)   
         doc["timelineDone"] = "done"
    	 self.db.save(doc)
      else:
         print("already saved for this user:")
  #       print("doc id : ",item.id)
 
  def justSearch(self,api,word):
#    geocode="38.376,-0.5,8km", rpp=1000
 #   data = api.search(q=["vegan","veg","vegetarian", "vegg","vegetarinism"],  count = 1000000)
    data = api.search(q= word ,gecode = "151.143366 , -33.822120, 500km",  count = 1000)
    for tweets in data:
        tweet = json.dumps(tweets._json)
        tw = json.loads(tweet)
        try:
          self.timelinedb[str(tw["id"])] = tw
          print("search should be saved")
        except Exception as e:
          print("exception while writing timeline ", e)
          pass

  def getData(self, viewName):
    for item in self.db.view('tweets/'+viewName):
      print("printing data : ",item.key, item.id, item.value)

  def createView(self,viewName):
    view = ViewDefinition('tweets', viewName, '''function(doc) {
         emit(doc.text, doc.coordinates);
      }''')
    view.get_doc(self.db)
    view.sync(self.db)
    print("create view user, view should be created")

  def createViewUsers(self):
    view = ViewDefinition('tweets', "users", '''function(doc) {
         emit(doc.user["id"], doc.done);
      }''')
    view.get_doc(self.db)
    view.sync(self.db)
    print("user view should be created")


