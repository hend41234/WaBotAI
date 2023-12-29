from app.api.message.create_message import CreateMessage
from twilio.rest import Client
import time 

account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'
client = Client(account_sid, auth_token)


class SendMessage:
    def __init__(self, bot, user, message):
        self.bot = bot
        self.user = user
        self.message = message
    
    def send_response(self):
        message = CreateMessage(self.bot, self.user)
        #response = message.create_message(self.message)
        response = "testing OK"
        response = response.replace("http://localhost", "localhost")# change http://localhost to localhost, because in twilio doesn't work to send a message
        lenght_response = len(response) 
        limit = 1599
        multiple = int(lenght_response/limit)

        def sender(user=self.user, bot=self.bot, message=response):
            client.messages.create(
                to=user,
                from_=bot,#"whatsapp:+14155238886",
                body=message
            )

        if multiple >= 1:
            for i in range(multiple):
                sender(
                    user=self.user,
                    bot=self.bot,#"whatsapp:+14155238886",
                    body=response[i*limit:(i+1)*limit]
                )
                time.sleep(3)

            sender(
                body=response[(i+1)*limit:]
            )
        else:
            sender()
    
        return response
