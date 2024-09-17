# make a call to an external API endpoint to retrieve structured data
import requests # NB we need to pip install requests

def fetchData():
    '''make a request to a URL and return the retrieved data structure'''
    url = 'https://jsonplaceholder.typicode.com/photos'
    try:
        response = requests.get(url) # we make a request to the url using 'get'
        # this particular API endpoint returns JSON
        data = response.json() # here we retrieve the returned JSON from the response
        return data
    except Exception as err:
        print(err)

def retrieveOnePhoto(n=1): # we may choose to set defaults for the function arguments
    '''use n to retrieve just a single photo from the API endpoint'''
    url = f'https://jsonplaceholder.typicode.com/photos/{n}'
    try:
        response = requests.get(url) # we make a request to the url using 'get'
        # this particular API endpoint returns JSON
        data = response.json() # here we retrieve the returned JSON from the response
        return data # this time it will be a single Photo
    except Exception as err:
        print(err)

if __name__ == '__main__':
    result = retrieveOnePhoto(42)
    print(result)