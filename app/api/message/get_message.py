from app.api.message.create_log import Log
class GetMessage:
    def __init__(self, data):
        self.data = data
        self.update_history
    @property
    def from_message(self):
        return self.data.get("To")
    @property
    def to_message(self):
        return self.data.get("From")
    @property
    def message(self):
        return self.data.get("Body")
    @property
    def update_history(self):
        # update history
        log = Log(self.from_message, self.to_message)
        log.check_history()
        log.create_history(self.data)