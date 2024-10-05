import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-4cb46-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data  ={
    "12345":
        {
            "name": "Naman Bansal",
            "major": "AI&ML",
            "starting_year": 2021,
            "total_attandance": 6,
            "standing": "G",
            "year": 4,
            "last_attandance_time": "2024-10-03 21:59:23"
        },
    "12354":
        {
            "name": "Elon Musk",
            "major": "CSE",
            "starting_year": 2020,
            "total_attandance": 8,
            "standing": "B",
            "year": 4,
            "last_attandance_time": "2022-10-03 21:59:23"
        },
    "12435":
        {
            "name": "Naman Bansal",
            "major": "AI&ML",
            "starting_year": 2021,
            "total_attandance": 6,
            "standing": "G",
            "year": 4,
            "last_attandance_time": "2024-10-03 21:59:23"
        },
    "21345":
        {
            "name": "Naman Bansal",
            "major": "AI&ML",
            "starting_year": 2021,
            "total_attandance": 6,
            "standing": "G",
            "year": 4,
            "last_attandance_time": "2024-10-03 21:59:23"
        }
}

for key, value in data.items():
    ref.child(key).set(value)