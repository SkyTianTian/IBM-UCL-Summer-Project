def getClass(result):
    try:
        classes = (result["images"][0]['classifiers'][0]['classes'][0]["class"])
        return classes
    except:
        a= "None"
        return a

def getScore(result):
    try:
        score = (result["images"][0]['classifiers'][0]['classes'][0]["score"])
        return score
    except:
        a = 0
        return a