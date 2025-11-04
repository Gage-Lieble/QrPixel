# Qr Pixel

## Manual QA Test Cases

| Case ID | Test Scenario | Steps to Reproduce | Expected Result | Actual Result | Status | Notes |
|---------------|----------------|--------------------|-----------------|----------------|--------|----------------|
| TC-01 | Create QR code without link input | 1. Enter the label for QR code 2. Leave link field blank 3. Choose the QR code color 4. Click 'Create Code' | The QR code should fail to generate and the page should display a validation error to the user | Works as expected | <span style="color: green;">Passed</span> | - |
| TC-02 | Interrupt QR code creation | 1. Fill out the QR code creation form 2. Select "Instructions" 3. Select "Back" 4. Continue QR code creation process | After interrupting the QR code creation process by viewing the "Instructions" page, the previously entered information should repopulate the form, saving the user's progress | After clicking the back arrow, the form resets | <span style="color: red;">Failed</span> | Instead of resetting the form, the fields should be repopulated with the information already entered by the user. |
| TC-03 | Saving QR code to list | 1. Log into a valid account 2. Create a QR code 3. Select "Save" | After saving a QR code, the page should redirect to the "Saved Codes" page displaying a list of the user's QR codes with custom labels and colors | Works as expected | <span style="color: green;">Passed</span> | Functions properly and is intuitive to the user. |
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
