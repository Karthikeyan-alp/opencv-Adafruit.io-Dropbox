# opencv-Adafruit.io-Dropbox



## GETTING STARTED
        
   <br>In this project we can see how to install an Adafruit and Dropbox for image procesing in the ubuntu 18.04 and it can also be installed in pi3.</br>
   
   
   ## PREREQUISITES
 
   - Raspberry pi 3/3B+/4
   - Ubuntu os
   - Proper Internet connections
   - Raspbian stretch os
   - Opencv Installed
   
   If opencv not installed you can use this link to find the Opencv installation instruction : https://github.com/Karthikeyan-alp/OpenCV-PI-Installation
   
   ## INSTALLING
   
   <br> open the terminal and type the foolowing code.
   
             sudo apt-get update
      
             sudo apt-get upgrade
             
If you are using an Raspberry pi then, use the following command.

              source ~/.profile
              
              workon cv
      
If you are using an Ubuntu then, use the following command.    

              workon cv
              
Adafruit.io is used to visualize the data in the dashboard.where the dropbox is used to store the data from the camera.Here we are using a Hikvision camera to monitor the people.

For raspberry pi to install adafruit
             
              curl https://raw.githubusercontent.com/adafruit/Adafruit-WebIDE/master/scripts/install.sh | sudo sh
              
For  ubuntu
              
              sudo pip3 install adafruit-io
              
Next step is to install the Dropbox on this platform.

              sudo pip install dropbox
              
              
 Next step is to create a dropbox and adafruit account to access the token for using in a program. The below link is used to create a new account
 
 ## Creating Account
 
For Adafruit.io: https://io.adafruit.com/
 <br> you can create a new account and copy the AIO key and create a new feed.
 
For Dropbox : https://www.dropbox.com/logincont=https%3A%2F%2Fwww.dropbox.com%2Fdevelopers%2Fapps%3F_tk%3Dpilot_lp%26_ad%3Dtopbar4%26_camp%3Dmyapps
 
 Using this link to create dropbox account and copy the secret key.
 
 Run the following program in Terminal to execute the image processing : Image.py
 
 ## IMPORTANT LINK
 
 - https://stackoverflow.com/questions/41285969/dropbox-api-v2-trying-to-upload-file-with-files-upload-throws-typeerror
 
 - https://github.com/adafruit/Adafruit_IO_Python/blob/master/examples/basics/pi_camera.py
 
 ## CONCLUSION

That's all we wrap up the things.we sucesfully installed the Adafruit.io and dropbox .
 
              
