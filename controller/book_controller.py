import logging
from datetime import datetime

from flask import request
from flask_restplus import Resource

from model.book_discovery import search_book_info, search_for_top_books
from model.message_response import MessageResponse
from .restplus import api
from .serilizers import book_query_params, temp_data

namespace = api.namespace('v1/book/', description='Query Books')


@namespace.route('/query_books/')
class BookDiscovery(Resource):
    @api.expect(book_query_params)
    def get(self):
        args = book_query_params.parse_args(request)
        name = args.get('title')
        author = args.get('author')

        return search_book_info(name, author)


@namespace.route('/n_most_popular/<string:query_text>')
@namespace.route('/n_most_popular/<string:query_text>/<int:search_field>')
@namespace.route('/n_most_popular/<string:query_text>/<int:search_field><int:page>')
class BookListDiscovery(Resource):
    def get(self, query_text, page=1, search_field="all"):
        return search_for_top_books(num_page=page, search_field=search_field, query_text=query_text)


@namespace.route('/book_info')
class BookLists(Resource):

    def get(self):
        response = MessageResponse(fullfillment_text=temp_data.get('fullfillment_text'), socketId=None,
                                   submitted_message=temp_data.get('submitted_message'), timestamp=datetime.now())
        return response.serialize()

    def post(self):
        data = request.get_json(silent=True)
        try:

            if 'bookarea' in data['queryResult']['parameters']:
                search_area = data['queryResult']['parameters']['bookarea']
                books = search_for_top_books(search_area)
                book_list = []
                for i in range(len(books)):
                    rank = {str(i + 1): books[i]['title']}
                    book_list.append(rank)
                temp_data['fullfillment_text'] = book_list

            elif 'bookname' in data['queryResult']['parameters']:
                book_title = data['queryResult']['parameters']['bookname']
                book = search_book_info(book_title)
                temp_data['fullfillment_text'] = book

            elif 'bookreview' in data['queryResult']['parameters']:
                book_title = data['queryResult']['parameters']['bookreview']
                book = search_book_info(book_title)
                temp_data['fullfillment_text'] = book['reviews_widget']
        except:
            temp_data['fullfillment_text'] = "Could not get details at the moment, please try again"

        temp_data['submitted_message'] = data['queryResult']['queryText']
        return temp_data

