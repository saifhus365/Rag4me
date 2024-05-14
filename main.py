import wikipediaapi
import requests

entity = "Donald Trump"
wiki_wiki = wikipediaapi.Wikipedia('RagProj', 'en')
page_py = wiki_wiki.page(entity)


response = requests.get("https://en.wikipedia.org/w/api.php?action=query&format=json&formatversion=2&prop=pageimages|pageterms&piprop=thumbnail&pithumbsize=600&titles=" + entity)
req = response.json()
print(req["query"]["pages"][0]["thumbnail"]["source"])
