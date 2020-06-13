import wikipedia
def findTitles(query):
    return wikipedia.search(query, results = 5)

def articleSummary(query):
    try:
        return wikipedia.summary(query)
    except wikipedia.exceptions.DisambiguationError:
        return "Be more specific!!!"

