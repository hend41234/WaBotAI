
from app.api.gpt.gpt import gpt
from app.api.message.create_log import Log


class CreateMessage:
    
    def __init__(self, bot, user):
        """
        Initializes a new instance of the class.

        Parameters:
            bot (Bot): The bot instance.
            user (User): The user instance.
        """
        self.bot = bot
        self.user = user
    def create_message(self, message_client):
        # print(message_client)
        log = Log(self.bot, self.user)
        log.check_log()# check if log file exist, if not create one

        old_log = log.read_log() # read log file
        message_user = [{"role":"user", "content":message_client}]# shape user message
        old_log.extend(message_user)# add user message to log thi is for gpt
        response_gpt = gpt(old_log) # get response from gpt 
        response_message = {"role":"system", "content":response_gpt}# shape response bot message
        message_user.append(response_message)# add response bot message to log
        
        # log
        log.create_log(message_user)# update log
        return response_gpt