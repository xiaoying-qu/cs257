# This program was written by Ruben Boero and Xiaoying Qu
# This code was revised by Alex Falk, Carl Zhang, Aldo Polanco, and Yiming Xia
# The code revision is done individually by Xiaoying Qu

import booksdatasource
import argparse

def get_parsed_arguments():
    parser = argparse.ArgumentParser(description='Book search program that prints out a list of books or authors.')
    parser.add_argument('search_term1',choices =['title','author','year'],help= 'Choose to specify the search term')
    parser.add_argument('search_term2', nargs="*", help='Optional, only when there is a or multiple second serach term(s)')
    parsed_arguments = parser.parse_args()
    return parsed_arguments

def get_command_line(arguments,data_source):
    if arguments.search_term1.lower() == 'title':
        if arguments.search_term2:
            return data_source.books(arguments.search_term2)
        return data_source.books()
    elif arguments.search_term1.lower() == 'author':
        if arguments.search_term2:
            return data_source.authors(arguments.search_term2)
        return data_source.authors()
    elif arguments.search_term1.lower() == 'year':
        if arguments.search_term2 == None:
            return data_source.books_between_years()
        elif len(arguments.search_term2) ==1:
            return data_source.books_between_years(int(arguments.search_term2[0]))
        else:
            return data_source.books_between_years(int(arguments.search_term2[0]),int(arguments.search_term2[1]))

def main():
    arguments = get_parsed_arguments()
    data_source = booksdatasource.BooksDataSource('books1.csv')

    for i in get_command_line(arguments,data_source):
        print(i)
  
if __name__ == '__main__':
    main()