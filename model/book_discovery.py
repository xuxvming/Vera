from model.goodreads_clien_stub import GoodReadsClientStub
import settings
import logging

repository = GoodReadsClientStub(settings.GOOD_READS_API, settings.GOOD_READS_SECRET)


def search_book_info(book_title, author=None):
    book = repository.retrieve_book(book_title, author)
    logging.info(book)
    return book._book_dict



def search_for_top_books(query_text, num_page=1, search_field="all"):
    logging.info('Searching books with query text: {}'.format(query_text))
    books = repository.search_books(q=query_text, page=num_page,search_field =search_field)
    book_list = []
    for book in books:
        book_list.append(book._book_dict)
    return book_list

