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
        response = MessageResponse(fullfillment_text=temp_data.get('fulfillment_text'), socketId=None,
                                   submitted_message=temp_data.get('submitted_message'), timestamp=datetime.now())
        return response.serialize()

    def post(self):
        data = request.get_json(silent=True)

        try:
            temp_data['submitted_message'] = data['queryResult']['queryText']
            if data['queryResult']['intent']['displayName'] == 'book.area':
                temp_data['fulfillment_text'] = None
                search_area = data['queryResult']['parameters']['bookarea']
                books = search_for_top_books(search_area)
                book_list = 'Here is a list of top 5 books:\n'
                for i in range(len(books)):
                    rank = str(i+1)+':'+books[i]['title']
                    book_list = book_list + rank + '\n'
                    if i == 4:
                        break
                temp_data['fulfillment_text'] = book_list

            elif data['queryResult']['intent']['displayName'] == 'book.area.search':
                if temp_data['fulfillment_text'] is None:
                    temp_data['fulfillment_text'] = 'Sorry, I could not find anything at the moment'
                return temp_data

            elif data['queryResult']['intent']['displayName'] == 'book.name':
                book_title = data['queryResult']['parameters']['bookname']
                book = search_book_info(book_title)
                return {'fulfillment_text':'Author: {} \n'.format(book['authors']['author']['name']) +
                                           'Rating on GoodReads: {} \n'.format(book['average_rating']) +
                                           'Published in: {}\n'.format(book['publication_year']) +
                                           'link: {}\n'.format(book['url'])}

            elif data['queryResult']['intent']['displayName']=='book.similar':
                book_title = data['queryResult']['parameters']['bookname']
                book = search_book_info(book_title)
                similar_books = 'here are some similar books: \n'
                for i in range(len(book['similar_books']['book'])):
                    title = str(i+1)+':'+book['similar_books']['book'][i]['title']
                    similar_books = similar_books + title + '\n'
                    if i == 3:
                        break

                return {'fulfillment_text':similar_books}

        except:
            temp_data['fulfillment_text'] = "Could not get details at the moment, please try again"

        return temp_data



