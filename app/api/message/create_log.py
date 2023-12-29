import os
import subprocess
import json
import datetime

class Log:
    def __init__(self, bot, user):
        self.bot = bot
        self.user = user
        self.date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    def check_log(self):
        """check if log file exist, if not create one"""
        if os.path.exists("logs"):
            pass
        else:
            subprocess.run(['mkdir', 'logs'])
        if os.path.exists(f"logs/{self.user}.json"):
            pass
        else:
            subprocess.run(['touch', f'logs/{self.user}.json'])
            x = open(f"logs/{self.user}.json", "w")
            x.write("[]")
            x.close()

    def create_log(self, new_log):
        """this only update the log file"""

        with open(f"logs/{self.user}.json", "r") as f:
            old_log = json.load(f)
        old_log.extend(new_log)
        
        with open(f"logs/{self.user}.json", "w") as f:
            json.dump(old_log, f)
    def read_log(self):
        with open(f"logs/{self.user}.json", "r") as f:
            log = json.load(f)
            return log

    #-> HISTORY
    def check_history(self):
        """check history file exist, if not create one"""

        if os.path.exists("history"):
            pass
        else:
            subprocess.run(['mkdir', 'history'])
        if os.path.exists(f"history/{self.user}.json"):
            pass
        else:
            subprocess.run(['touch', f'history/{self.user}.json'])
            x = open(f"history/{self.user}.json", "w")
            x.write("[]")
            x.close()
    def create_history(self, new_log):
        """this only update the history file

            params:
                new_log (dict): is all required data.
                you can modify new_data body as needed. more detail you can look at the new_log
        """

        new_data = {
            "Profile": new_log.get("ProfileName"),
            "ID": new_log.get("WaId"),
            "MessageSID": new_log.get("MessageSId"),
            "Body": new_log.get("Body"),
            "To": new_log.get("To"),
            "NumMedia": new_log.get("NumMedia"),
            "NumSegment": new_log.get("NumSegments"),
            "datetime": self.date_time
        }
        with open(f"history/{self.user}.json", "r") as f:
            old_log = json.load(f)
        old_log.append(new_data)
        
        with open(f"history/{self.user}.json", "w") as f:
            json.dump(old_log, f)
    
    
