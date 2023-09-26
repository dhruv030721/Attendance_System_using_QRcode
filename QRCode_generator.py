import qrcode 
import json


student_data = {
    "name" : "Aryan",
    "enrollment_no" : "211240107027",
    "branch" : "Computer"
}

json_data = json.dumps(student_data)

qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_L, box_size = 3, border = 4)

qr.add_data(json_data)

qr.make(fit = True)

qr_img = qr.make_image(fill_color = "black", back_color = "white")

qr_img.save("27.png")