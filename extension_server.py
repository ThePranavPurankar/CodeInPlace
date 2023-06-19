"""
File: extension_server.py
---------------------
This starts a server! Go to http://localhost:8000 to enjoy it. Currently
the server only serves up the HTML. It does not search. Implement code in
the "TODO" parts of this file to make it work.
"""

# This imports the SimpleServer library
import SimpleServer

# This imports the functions you defined in searchengine.py
from searchengine import create_index, search, textfiles_in_dir

# To get the json.dumps function.
import json


# the directory of files to search over
DIRECTORY = 'bbcnews'
# perhaps you want to limit to only 10 responses per search.
MAX_RESPONSES_PER_REQUEST = 10


class SearchServer:
    def __init__(self):
        """
        load the data that we need to run the search engine. This happens
        once when the server is first created.
        """
        self.html = open('extension_client.html').read()

        # TODO: Your code here. Change this code to load any data you want to use!
        self.index = {}
        self.file_titles = {}
        self.filenames = textfiles_in_dir(DIRECTORY)
        create_index(self.filenames, self.index, self.file_titles)

    # this is the server request callback function. You can't change its name or params!!!
    def handle_request(self, request):
        """
        This function gets called every time someone makes a request to our
        server. To handle a search, look for the query parameter with key "query"
        """
        # it is helpful to print out each request you receive!
        print(request)

        # if the command is empty, return the html for the search page
        if request.command == '':
            return self.html

        # if the command is search, the client wants you to perform a search!
        if request.command == 'search':
            # right now we respond to a search request with an empty string.
            # TODO: Your code here. change this code to return the string version
            params = request.get_params()
            term = params ['query']
            print('term is' + str(term))
            file_names = search(self.index, term)
            titles = []
            for file_name in file_names:
                temp_dict = {}
                temp_dict['title'] = self.file_titles[file_name]
                titles.append(temp_dict)
            # of a list of dicts. Use json.dumps(collection) to turn a list into a string
            return_list_str = json.dumps(titles)
            return return_list_str


def main():
    # Make an instance of your Server
    handler = SearchServer()

    # Start the server to handle internet requests at http://localhost:8000
    SimpleServer.run_server(handler, 8000)


if __name__ == '__main__':
    main()
