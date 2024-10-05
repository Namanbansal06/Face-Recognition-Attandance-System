import cv2
import face_recognition
import pickle
import os
from PIL import Image
import numpy as np
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-4cb46-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattendancerealtime-4cb46.appspot.com"
})


# Importing the student images
folderPath = 'Images'
PathList = os.listdir(folderPath)
imgList = []
studentIds = []
for path in PathList:
    img = cv2.imread(os.path.join(folderPath,path))
    img_pil = Image.fromarray(img)
    img_8bit = img_pil.convert('L')  # For 8-bit grayscale
    img_rgb = img_pil.convert('RGB')
    img_np = np.array(img_8bit)
    imgList.append(img_np)
    studentIds.append(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'  # adding images to database
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

    # print(path)
    # print(os.path.splitext(path)[0])
print(len(imgList))

def findEncodings(imagesList):
    encodeList = []
    for imgi in imagesList:
        imgi = cv2.cvtColor(imgi, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(imgi)[0]
        encodeList.append(encode)

    return encodeList

print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
print(encodeListKnown)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds,file)
file.close()
print("File Save")