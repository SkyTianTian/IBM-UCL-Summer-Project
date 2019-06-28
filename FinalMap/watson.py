from watson_developer_cloud import VisualRecognitionV3
from getImage import *
from jsonDecoder import *

def train(long,lati,fileName):
    visual_recognition = VisualRecognitionV3(
        version='2018-03-19',
        iam_apikey='En8MaCZbEtnirUlnbkZncKBm2RqecjwClCzLOVK8WcYN'
    )
    image = imageGet(long,lati)
    image.convert('RGB').save("res/"+fileName+".jpg")
    with open('res/1.jpg', 'rb') as image_file:
        classes = visual_recognition.classify(
            image_file,
            threshold= '0.6',
            classifier_ids='Test2_1388944331').get_result()
        result = getClass(classes)
        print("Class Result = ", result)
        return getClass(result)