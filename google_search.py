def searchGoogle(q, searchnum = 5):
    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module named 'google' found") 
    
    # to search 
    query = q
    replies =[]
    s = 1
    for j in search(query, tld="com",lang = 'en', num=searchnum, stop=searchnum, pause=1): 
        replies.append("Search #" + str(s) + ": " +j)
        s = s+1
    return replies
   