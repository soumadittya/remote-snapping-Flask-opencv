# remote-snapping-Flask-opencv

Description -  

A web server (made in Flask) runs on a remote computer ( can be a raspberry pi) and using a web browser 
a picture can be taken and seen from other computer on the same network.

Frameworks used - 

1. Flask
2. OpenCV

There are two files - 

1. web_file.py - this is basically a Flask server file which responds to the user when a user 
enters the ip address of the server by accessing capture_file.py.

2. capture_file.py - this file when accessed takes a image using a webcam (using OpenCV) and returns that to web_file.py.
