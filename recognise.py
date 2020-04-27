import boto3
import cv2
import json

def detect_faces(photo):

    client=boto3.client('rekognition')

    response = client.detect_faces(
        Image={
            'Bytes': photo
        }, 
        Attributes=[
            'ALL'
        ]
    )

    # print('Detected faces for photo')    

    # for faceDetail in response['FaceDetails']:
        # print('Emotion ' + str(faceDetail['Emotions'])) 
    # #           + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
    # #     print('Here are the other attributes:')
    #     print(json.dumps(faceDetail, indent=4, sort_keys=True))
    # return len(response['FaceDetails'])
    return response


 

