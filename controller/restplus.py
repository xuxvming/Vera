import logging

from flask_restplus import Api
import os


log = logging.getLogger(__name__)

api = Api(version='1.0', title='Vera, a book assistant',
          description='REST endpoints chatbot')


@api.errorhandler
def default_error_handler(e):
    message = str(e)
    log.exception(message)

    if not os.getenv('FLASK_DEBUG'):
        return {'message': message}, 500

