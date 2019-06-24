import json
from ibm_watson import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='-GYYjUi0YB3uN4F6RyjfIyd4et1ZvRCpwECnxeBlad94')

with open('res/beagle.zip', 'rb') as beagle, open(
        'res/golden-retriever.zip', 'rb') as goldenretriever, open(
            'res/husky.zip', 'rb') as husky, open(
                'res/cats.zip', 'rb') as cats:
    model = visual_recognition.create_classifier(
        'dogs',
        positive_examples={'beagle': beagle},
        negative_examples=cats).get_result()
print(json.dumps(model, indent=2))