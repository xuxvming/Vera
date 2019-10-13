# Flask settings
FLASK_SERVER_NAME = 'localhost:8080'
FLASK_DEBUG = True  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

DIALOGFLOW_KEY = 'small-talk-ffuybr-79d788400596.json'
DIALOG_PROJECT_ID = 'small-talk-ffuybr'

PUSHER_APP_ID = '878134'
PUSHER_KEY = '9c0987ec962f516d0382'
PUSHER_SECRET= 'f8bc4b2686c4f4e0d1b0'
PUSHER_CLUSER = 'eu'

GOOD_READS_API = 'B8cygGUuRsmPMoNaKiimQ'
GOOD_READS_SECRET = 'pUphWdeaAjlfYMKEvqAd7hAHJxLZ86nkVB2aHk7jB84'

NGROK_COMMAND ='./ngrok http 8080 -host-header="localhost:8080"'