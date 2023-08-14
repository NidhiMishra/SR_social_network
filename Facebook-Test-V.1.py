import sys
import os
sys.path.append("../../i2p/i2pThrift/gen-py")
sys.path.append("../../i2p/i2pThrift/tools/py")

import SocialNetwork
from SocialNetwork import constants
from SocialNetwork import ttypes
import SocialNetwork.Facebook as Facebook_Service
import SocialNetwork.Google as Google_Service

#include wrappers
import json
import facebook

import requests
requests.packages.urllib3.disable_warnings()
#to ease client server creation in python
import ThriftTools

class FacebookHandler:
    def __init__(self):
		ACCESS_TOKEN = 'EAAF1ghdq9oEBAICblQbQUBZCTtQH7RYZANYiyXrZBBblNGfcKy4kEg4Qj0tBxUkRKF0XO1bdriht9ZAQ3muSlxHl8sFaZC4MFb44ZBB41AHvz0AQrRd4djnFr0itK08iHqDgcSW5ccXEqoQ7OmZBEvDbvy7LXkZAmOoZD'	
		self.graph = facebook.GraphAPI(access_token=ACCESS_TOKEN, version='2.3')
    def takePicture(self, message):
		print message
	  
    #WARNING: Apparently there is an http error when we send two times the exact same message...
    def postMessage(self, message):
		print message
		#print self.graph
		self.graph.put_object(parent_object='me', connection_name='feed',  message= message )	
    
    #WARNING: Apparently there is an http error when we send two times the exact same message...    
    def postMessageAndPicture(self, message, picture):
        print message
        filename = 'picture_out.png'
        with open(filename, 'wb') as f:
			f.write(picture)
			self.graph.put_photo(image=open(filename, 'rb'), message=message)
			print "Posted"
			
    def getDateofBirth(self, uName):
		return
        
        
#initializing

facebook_handler = FacebookHandler()
facebook_server = ThriftTools.ThriftServerThread(constants.DEFAULT_GOOGLE_SERVICE_PORT,Facebook_Service,facebook_handler,'Facebook Server','localhost') #14001
facebook_server.start()	
print 'Server Connected'




