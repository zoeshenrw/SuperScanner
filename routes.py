from config import app, conn, distance, get_station_info, loc, URL_info 
from flask import Flask, render_template, redirect, url_for, flash, request, Response, make_response, send_from_directory,session, Markup
from pywebpush import webpush, WebPushException
import json
from forms import LoginForm
#import cv2
#import pyzbar.pyzbar as pyzbar
import webbrowser
import requests
import math

#Getting location
global nearby_stations
nearby_stations = get_station_info(URL_info, loc)

# #Notification
# VAPID_SUBJECT = "mailto:aml9186@nyu.edu"
# with open('private_key.json') as pk:
#     data = json.load(pk)
# VAPID_PRIVATE = data["public"]
# from register import register_bp
# app.register_blueprint(register_bp, url_prefix="/register")

# #Scanner
# camera=cv2.VideoCapture(0)
# global value 
# def read_qr_code(frame):
#     # Use cv2 to detect the QR code
#     try:
#         detect = cv2.QRCodeDetector()
#         value, points, straight_qrcode = detect.detectAndDecode(frame)
#         return value
#     except:
#         return None

# #Read the camera frame
# def generate_frames():
#     while True:
#         success,frame=camera.read()
#         decoded=pyzbar.decode(frame)
#         if not success:
#             break
#         else:
#             value = read_qr_code(frame)
#             #Open web browser
#             if value:
#                 webbrowser.open(value)
#                 break
#             ret,buffer=cv2.imencode('.jpg',frame)
#             frame=buffer.tobytes()
#         yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

#Home page
@app.route('/')
@app.route('/home')
def home_page():    
    return render_template('home/home.html')

# Sending notifications on nearby stations with link to google map.
@app.route('/notif')
def notif_page():
    nearby_stations = get_station_info(URL_info, loc)
    if len(nearby_stations) == 0:
        loc = ['40.7309', '73.9973']
        nearby_stations = get_station_info(URL_info, loc)
        #flash(Markup(f'No stations nearby. Please try again later at location {loc}.'), category='danger')
    for station in nearby_stations:
        name  = station['station_name']
        capacity = station['station_capacity']
        lat, lon = station['station_lat'], station['station_lon']
        print(station)
        flash(Markup(f'Station nearby detected: location --> {name}. There are {capacity} bikes remaining at the station. For Directions click <a href="https://www.google.com/maps/search/?api=1&query={lat},{lon}" class="alert-link">here</a>'), category='success')
    return render_template('notif.html')

# #call this from a route when a nearby bike is found, and return the data to user as a push notification in json format
# @app.route("/push", methods=["POST"])
# def push():
#   sub = json.loads(request.form["sub"])
#   result = "OK"s
#   try:
#     webpush(
#       subscription_info = sub,
#       data = json.dumps({
#         "title" : "Welcome!",
#         "body" : "Yes, it works!",
#         "icon" : "static/bikes.png",
#         "image" : "static/card.png"
#       }),
#       vapid_private_key = VAPID_PRIVATE,
#       vapid_claims = { "sub": VAPID_SUBJECT }
#     )
#   except WebPushException as ex:
#     print(ex)
#     result = "FAILED"
#   return result

#About page
@app.route('/about')
def about_page():
    return render_template('about.html')

#Information page on clickable maps
@app.route('/information')
def information_page():
    return render_template('information.html')

#Market page under information drop down bar
@app.route('/market')
def market_page():
    return render_template('market.html')

#Map page with connected API
@app.route('/map')
def map_page():
    return render_template('map.html')

# #Scanner page
# @app.route('/scanner')
# def scanner_page():
#     return render_template('scanner.html')

# @app.route('/scanned')
# def scanned_page():  
#     try:  
#         return redirect(value)
#     except:
#         return redirect(url_for("video"))

# @app.route('/video',methods=['GET'])
# def video():
#     try: 
#         return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')
#     except:
#         return redirect(url_for("scanned_page"))

#Login page
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    #If the user is already loggin in
    if session.get('apple_id'):
        flash('Already logged in!', category='danger')
        return redirect(url_for("home_page"))
    form = LoginForm()
    #Collecting information for user login
    if form.validate_on_submit():
        apple_id = form['apple_id'].data
        password = form['password'].data
        q = 'SELECT * FROM User WHERE appleID = %s and password = md5(%s)'
        cursor = conn.cursor()
        cursor.execute(q, (apple_id, password))
        res = cursor.fetchone()
        cursor.close()
        if res:
            flash(f'Success! You are logged in as: {apple_id}', category='success')
            session['apple_id'] = apple_id
            return redirect(url_for('home_page'))
        else:
            flash(f'AppleID and password are not a match! Please try again', category='danger')

    return render_template('login.html', form=form)

#Logout page
@app.route('/logout')
def logout_page():
    if session:
        session.clear()
        flash("You have been logged out!", category='info')
        return redirect(url_for("home_page"))
    else:
        session.clear()
        flash("You have not logged in yet!", category='info')
        return redirect(url_for("home_page"))

