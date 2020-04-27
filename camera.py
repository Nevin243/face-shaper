import numpy as np
import cv2
from recognise import detect_faces

ESC = 27
SPACE = 32

def capture_face():
    data = {}
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("Face Capture")

    while True:
        ret, frame = cam.read()
        cv2.imshow("Face", frame)

        if not ret:
            break

        k = cv2.waitKey(1)

        if k%256 == ESC:
            # ESC pressed
            print("Escape hit, closing...")
            break

        elif k%256 == SPACE:
            # SPACE pressed
            response=detect_faces(cv2.imencode('.jpg', frame)[1].tostring())

            # TODO Fix to handle one face only in frame
            for faceDetail in response['FaceDetails']:
                # print('Emotions: \t Confidence\n')
                for landmark in faceDetail['Landmarks']:                    
                    data[str(landmark['Type'])] = {
                        "X":landmark['X'],  
                        "Y": landmark['Y']
                        }

                # for box in faceDetail['BoundingBox']: 
                data['Length'] = faceDetail['BoundingBox']['Height']
                data['Width'] = faceDetail['BoundingBox']['Width']
            
            print("Processing...")
            break
                
    # Clean up resources
    cam.release()
    cv2.destroyAllWindows()

    # Return Json object
    return data
