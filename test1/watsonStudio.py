import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='-GYYjUi0YB3uN4F6RyjfIyd4et1ZvRCpwECnxeBlad94')

with open('res/1.jpg', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        threshold='0.6',
	classifier_ids='TestModel1_82373101').get_result()
print(json.dumps(classes, indent=2))