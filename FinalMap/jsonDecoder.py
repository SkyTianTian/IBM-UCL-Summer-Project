def getClass(result):
    classes = (result["images"][0]['classifiers'][0]['classes'][0]["class"])
    return classes

def getScore(result):
    score = (result["images"][0]['classifiers'][0]['classes'][0]["score"])
    return score