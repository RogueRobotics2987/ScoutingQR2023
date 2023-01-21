from flask import Flask
import cv2
import numpy as np
# import pyzbar
import pyzbar.pyzbar as pyzbar

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    #return 'Hello World!'
    cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_PLAIN

    while True:
        _, frame = cap.read()

        decodedObjects = pyzbar.decode(frame)
        for obj in decodedObjects:
            print("Data", obj.data)
            with open("C:\\Users\\Rogue\\PycharmProjects\\ScoutingQR2023\\AllData.csv", "a") as allData:
                allData.write(str(obj.data)+"\n")
            return obj.data
            #cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                        #(255, 0, 0), 3)

if __name__ == '__main__':
    app.run()
