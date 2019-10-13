import dialogflow_v2 as dialogflow
from flask import request
from model.message_response import MessageResponse
import settings
import pusher
import logging
from datetime import datetime



pusher_client = pusher.Pusher(
    app_id=settings.PUSHER_APP_ID,
    key=settings.PUSHER_KEY,
    secret=settings.PUSHER_SECRET,
    cluster=settings.PUSHER_CLUSER,
    ssl=True)

def send_message():
    try:
        socketId = request.form['sockerId']
    except:
        socketId = ''

    message = request.json.get('input')
    project_id = settings.DIALOG_PROJECT_ID
    fulfillment_text = detect_intent_texts(project_id, "unique", message, 'en')
    logging.info("response message is:"+fulfillment_text)
    pusher_client.trigger(
        'movie_bot',
        'new_message',
        {
            'human_message': message,
            'bot_message': fulfillment_text,
        },
        socketId
    )

    return MessageResponse(fullfillment_text=fulfillment_text,socketId=socketId,submitted_message=message,timestamp=datetime.now())



def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    if text:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(
            session=session, query_input=query_input)

        return response.query_result.fulfillment_text