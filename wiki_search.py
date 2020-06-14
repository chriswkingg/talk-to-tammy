import wikipedia
import discord
def findTitles(query):
    return wikipedia.search(query, results = 5)

def articleSummary(query):
    try:
        return wikipedia.summary(query,chars=2000, auto_suggest=True, redirect=True)
    except wikipedia.exceptions.DisambiguationError:
        return "Be more specific!!!"
    except wikipedia.exceptions.PageError:
        return query + " does not match any pages"
    except discord.errors.HTTPException:
        return "The summary cant be loaded, check out the link: " + getLink(query)

def getLink(query):
    try:
        return wikipedia.page(query).url
    except wikipedia.exceptions.PageError:
        return query + " does not match any wiki pages"

