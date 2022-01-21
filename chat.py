from httplib2 import Http
import json

class Bot:
    def __init__(self,webhook_url):
        self.webhook_url = webhook_url
        
    def send_message(self,bot_msg,args={}):
    
        message = {
            "text": bot_msg
        }
        
        for k, v in args.items():
            message[k] = v
        
        msg_headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        
        http_obj = Http()
        
        response = http_obj.request(
            uri=self.webhook_url,
            method = 'POST',
            headers=msg_headers,
            body=json.dumps(message)
        )
        
        return response