from watson_developer_cloud import VisualRecognitionV3
from getImage import *
from jsonDecoder import *
import json


def train(long, lati, fileName):
    visual_recognition = VisualRecognitionV3(
        version='2018-03-19',
        iam_apikey='OBBkqDog2EksEcC5rcq2P3qGEpA4Hv8qsnCjL0zi6KAn'
    )
    image = imageGet(long, lati)
    image.convert('RGB').save("res/" + fileName + ".jpg")
    with open('res/1.jpg', 'rb') as image_file:
        classes = visual_recognition.classify(
            image_file,
            threshold='0.6',
            classifier_ids='Test4_1195462511').get_result()
        result = getClass(classes)
        print("Class Result = ", result)
        return getClass(result)


def trainWithFile(file):
    visual_recognition = VisualRecognitionV3(
        version='2018-03-19',
        iam_apikey='OBBkqDog2EksEcC5rcq2P3qGEpA4Hv8qsnCjL0zi6KAn'
    )
    fileName = "res/" + file + ".jpg"
    with open(fileName, 'rb') as image_file:
        classes = visual_recognition.classify(
            image_file,
            #threshold= '0.6',
            classifier_ids='Test4_1195462511').get_result()
    print(classes)
    #print(json.dumps(classes, indent=2))
    result = getScore(classes)
    print("Class Result = ", result)
    return result


if __name__ == "__main__":
    result = trainWithFile("0_1_4")
    print(result)
