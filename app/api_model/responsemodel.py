from pydantic import BaseModel
##################################################
### The response model for the "/wa" endpoint. ###
class ResponseModel(BaseModel):
    datetimestamp: str = None
    message: str = None
    user: str = None
    bot: str = None
    class Config:
        json_schema_extra = {
            "example": {
                "datetimestamp": "2022-01-01 00:00:00",
                "message": "Hello",
                "user": "whatsapp:+14155238886",
                "bot": "whatsapp:+14155238886"
            }
        }
