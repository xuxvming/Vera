from flask_restplus import fields
from flask_restplus import reqparse
from .restplus import api


message = api.model('message',{
    'input':fields.String(readOnly = True,description = 'send a message to Vera')
})

response = api.model('response',{
    'submitted message':fields.String(readOnly = True,description = 'send a message to my gf'),
    'socketID':fields.String(readOnly = True,description = 'socketID'),
    'time':fields.String(readOnly = True,description = 'timestamp'),
    'response message':fields.String(readOnly = True,description = 'response messages'),
})

book_ranking_response = api.model('book_response',{
'submitted message':fields.String(readOnly = True,description = 'send a message to my gf'),
    'socketID':fields.String(readOnly = True,description = 'socketID'),
    'time':fields.String(readOnly = True,description = 'timestamp'),
    'response message':fields.List(fields.Raw(readOnly = True,description = 'response messages')),
})

book_review_response = api.model('book_response',{
'submitted message':fields.String(readOnly = True,description = 'send a message to my gf'),
    'socketID':fields.String(readOnly = True,description = 'socketID'),
    'time':fields.String(readOnly = True,description = 'timestamp'),
    'response message':fields.String(readOnly = True,description = 'response messages'),
})

book_detail_response = api.model('book_response',{
'submitted message':fields.String(readOnly = True,description = 'send a message to my gf'),
    'socketID':fields.String(readOnly = True,description = 'socketID'),
    'time':fields.String(readOnly = True,description = 'timestamp'),
    'response message':fields.Raw(readOnly = True,description = 'response messages'),
})


book_query_params = reqparse.RequestParser()
book_query_params.add_argument('title', type =str, required = True)
book_query_params.add_argument('author', type =str, required = False)

book_list_query_params = reqparse.RequestParser()
book_list_query_params.add_argument('page', type =int, required = False)
book_list_query_params.add_argument('search_text', type =str, required = False)
book_list_query_params.add_argument('search_field', type =str, required = False)


temp_data = {'fulfillment_text':None,'submitted_message':None}