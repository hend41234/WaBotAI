from fastapi import APIRouter, Request, Form

import datetime

from app.api_model.responsemodel import ResponseModel
from app.api.message.get_message import GetMessage
from app.api.message.send_message import SendMessage

app_router = APIRouter(prefix="/api")

@app_router.post("/wa", response_model=ResponseModel)
async def wa(request: Request):
    """
    POST request handler for the "/wa" endpoint.

    Parameters:
        request (Request): The incoming request object.
        for try we need 3 fields: 
            1. Body
            2. To
            3. From
        3 fields are required and process the message
        
        with curl we can use this command:
            curl -X POST -d Body="Hello" -d To="whatsapp:+14155238886" -d From="whatsapp:+6285869144649" http://localhost:8000/api/wa
            

    Returns:
        ResponseModel: The response model containing the datetimestamp, message, user, and bot.
    """
    data = await request.form()
    get_message = GetMessage(data)
    create_message = SendMessage(get_message.from_message, get_message.to_message, get_message.message)
    create_message.send_response()
    
    result = ResponseModel(
        datetimestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        message=get_message.message,
        user=get_message.from_message,
        bot=get_message.to_message
    )

    return result
