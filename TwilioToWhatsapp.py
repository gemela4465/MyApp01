
from twilio.rest import Client 
 
account_sid = 'AC1e1ae70d8dca4cd1c4894aea91f78028' 
auth_token = '46afd4b90f0aafe9fa78e6ad97fc7a29' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='hello~',      
                              to='whatsapp:+886918325809' 
                          ) 
 
print(message.sid)
