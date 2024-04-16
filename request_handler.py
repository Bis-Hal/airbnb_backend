import pickle
def getPrompt(url):
    
    return url.replace('%20'," ")
   

def getResponse(url):
    response = "";
    data = {'key': 'value'} 
    with open('rating.pkl', 'wb') as f:
        pickle.dump(data, f)

    return str(response)
