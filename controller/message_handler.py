from flask_restplus import Resource

from model.intent_detector import *
from .restplus import api
from .serilizers import message, response

namespace = api.namespace('v1/message/', description='Send messages')


@namespace.route('/send_message/')
class MessageHandler(Resource):

    @api.expect(message)
    @api.marshal_list_with(response)
    def post(self):
        response = send_message()
        response = response.serialize()
        return response


