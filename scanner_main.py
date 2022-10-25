import cv2
import pyzbar.pyzbar as pz

image=cv2.imread("jpg") #works for a given image
cap=cv2.VideoCapture(0) #webcam

decoded=pz.decode(image)

print(decoded)

while True:
    _, frame = cap.read()
    cv2.imshow("Frame",frame)
    decoded=pz.decode(frame)
    for obj in decoded:

        if len(obj)>=1:
            import webbrowser
            webbrowser.open(obj.data.decode('utf-8'))
            break

    key=cv2.waitKey(1)
    if key==27:
        break

class user:
    def __init__(self,firstname,lastname,address,zipcode,password):
        self.firstname=firstname
        self.lastname=lastname
        self.address=address
        self.zipcode=zipcode
        self.password=password
    def registration(self):
        self.firstname=input("First name")
        self.lastname=input("Last name")
        self.address=input("Address")
        self.zipcode=input("Zipcode")
        self.password=input("Password")