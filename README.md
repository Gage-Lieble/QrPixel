# Qr Pixel
[Visit the final product! >](https://qrpixel-gage.herokuapp.com/)
#### Qrcode generator and manager
> Create custom qr codes and save them to your online profile
## Project Outline
Qr Pixel is a QRcode generator/management webapp. By using [Go QR API](https://goqr.me/api/) I'm able to create a functional app that allows the user to create custom Qr Codes. The results generate a scanable code that will redirct to the intended destination. Utilizing the profile system, you can save each and every QRcode to your online list to be scanned later. 
## Features
Qr Pixel gives three options of customization. First you can chose the label you'd like your code to be called, Then you can select the link you'd like it to redirect to, and finally you can chose any color you'd like the Qrcode to be!
#### Base/Crucial Features:
- Qrcode label
- Qrcode link
- Qrcode color
#### Additional/Extra Features:
- Profile creation
- Save Qrcodes to profile
- Instruction page
## Data Model
Stored data that the app will require
- Qrcode label
- Qrcode link
- Qrcode color
- Username
- Password
## Schedule
#### Session 1:
MVP
- [x] Create the Qrcode generator (lable, color, link)
- [x] Use backend to generate Qrcode img
- [x] Display the Qrcode with basic details (lable)
#### Session 2:
Extra
- [x] Create login & register system
- [x] Create function to save Qrcodes to profile
- [x] Allow user to remove Qrcodes from list
- [ ] Create 'cool' javascript animations
#### Session 3:
Finalizations
- [x] Begin styling 
- [x] Create app logo and image assests
- [x] Desktop responsive
- [x] Deploy app
