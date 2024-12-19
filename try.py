import requests
import urllib.parse


class Request:
    def __init__(self,method,args):
        self.args=args
        self.method=method
    
request=Request('GET',{'search':"Galvin"})

if request.method == 'GET':
    search=urllib.parse.quote(request.args.get('search',''))
    url=f"https://www.googleapis.com/books/v1/volumes?q={search}&maxResults=5"
    response=requests.get(url)
    #print(response.json())

    if response.status_code==200:
        data=response.json()
        for item in data.get('items',[]):
            volumn_info=item.get('volumeInfo',{})
            title=volumn_info.get('title','N/A')
            publisher=volumn_info.get('publisher','N/A')
            published_date=volumn_info.get('publishedDate','N/A')
            author=volumn_info.get('authors',['N/A'])
            rating=volumn_info.get('averageRating',['N/A'])
            image_links=volumn_info.get('imageLinks',{})
            image=image_links.get('thumbnail') if 'thumbnail' in image_links else 'N/A'

            print(title)
            print(publisher)
            print(published_date)
            print(author)
            print(rating)
            print(image)