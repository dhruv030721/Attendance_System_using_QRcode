import cv2
import numpy as np
from pyzbar.pyzbar import decode
import requests
import winsound  # Import the winsound library for Windows

# Define the URL where you want to send the POST request
post_url = "http://localhost:3001/api/v1/Attendance"  # Replace with your actual API endpoint

while True:
    cap = cv2.VideoCapture(0)
    qr_code_scanned = False

    while cap.isOpened() and not qr_code_scanned:
        _, img = cap.read()
        for qrcode in decode(img):
            codeData = qrcode.data.decode('utf-8')
            print(codeData)
            qr_code_scanned = True

            # Send an HTTP POST request with the QR code data
            payload = {'data': codeData}  # You can customize the payload as needed
            headers = {'Content-Type': 'application/json'}
            response = requests.post(post_url, json=payload, headers=headers)

            if response.status_code == 200:
                winsound.Beep(1000, 1000)  # Beep at 1000 Hz for 200 milliseconds
                print("POST request successful")
            else:
                print(f"POST request failed with status code: {response.status_code}")
                for i in range(0,5):
                    winsound.Beep(500, 500)

            # Continue with the rest of your code
            points = np.array([qrcode.polygon], np.int32).reshape((-1, 1, 2))
            points2 = qrcode.rect
            cv2.polylines(img, [points], True, (0, 255, 0), 5)
            cv2.putText(img, codeData, (points2[0], points2[1] - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2)

        cv2.imshow('image', img)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
