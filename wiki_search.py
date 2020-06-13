import wikipedia
def findTitles(query):
    return wikipedia.search(query, results = 5)

def articleSummary(query):
    try:
        return wikipedia.summary(query)
    except wikipedia.exceptions.DisambiguationError:
        return "Be more specific!!!"
    except wikipedia.exceptions.PageError:
        return query + " does not match any pages"

def getLink(query):
    try:
        return wikipedia.page(query).url
    except wikipedia.exceptions.PageError:
        return query + " does not match any wiki pages"

