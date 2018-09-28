# Automation-Testing-Demo

#INTRODUCTION

This file contains information on how to set up and run tests on your machine
for toolium Web Testing and Mobile Testing.
In order for the tests to run on your local machine please follow the steps below.

#STEPS FOR SETTING UP YOUR MACHINE
*STEPS TO INSTALL APPIUM*
=========================
 Install node.js without using sudo-

Download latest nodejs https://nodejs.org/download/release/latest/

Install it under/usr/local

    *cd /usr/local tar --strip-components 1 -xzf /home/username/Downloads/node-v8.2.1-linux-x64.tar.gz

    
Check the installation using:

    * node -v

Install Java, jdk and jre-

    * sudo apt-get update
    * sudo apt-get install default-jre
    * sudo apt-get install default-jdk
    //to install oracle jdk
    * sudo add-apt-repository ppa:webupd8team/java
    * sudo apt-get update
    * sudo apt-get install oracle-java8-installer

 Set JAVA HOME path
 
    //open bashrc file 
    * gedit ~/.bashrc
    * export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
    * export PATH=${PATH}:${JAVA_HOME}/bin
     //run following command to verify the path
    * echo $JAVA_HOME
    * echo $PATH
 Command to check if java is installed:

 	  * which java 

 Download android studio and set the ANDROID HOME path
 
 To open android studio open terminal and install android android sdk
 
    * cd android-studio/bin ./studio.sh
   
  Once android sdk is installed, Set ANDROID HOME path using:
     
    * gedit /.bashrc
    * //add following lines at the end of the file and then save
    * export ANDROID_HOME=/home/user_name/Android/Sdk
    * export PATH=$PATH:/home/user_name/Android/Sdk/tools
    * export PATH=$PATH:/home/user_name/Android/Sdk/platform-tools
  
 Install appium globally
 
    * npm install -g appium
     
 Install appium-doctor to troubleshoot errors
 
    * npm install -g appium-doctor
 

# Install Selenium   

# Install Python Pip


    * sudo apt-get install python-pip python-dev build-essential
    * sudo -H pip install --upgrade pip

# Install Python  Virtualenv

     * sudo -H pip install --upgrade virtualenv

# Install toolium

     * sudo -H pip install toolium
     * sudo -H pip install git+https://github.com/behave/behave


# Install chromedriver 

Your current directory should be "$HOME" as illustrated below:

cd "$HOME"
wget -O "chromedriver_linux64.zip" "https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip"
unzip -o "chromedriver_linux64.zip"
sudo cp "chromedriver" "/usr/local/bin/chromedriver"
sudo chmod +x "/usr/local/bin/chromedriver"
rm -f "chromedriver"
rm -f "chromedriver_linux64.zip"

To ensure chromedriver is successfully installed check on the terminal wih the below command:

    *which chromedriver


# Install Genymotion (Android Emulator)
   
Step 1. Download Genymotion (Android Emulator) link:https://www.genymotion.com/fun-zone/

Step 2. Open terminal (ctrl+alt+t) and type below command to install virtualbox 

sudo apt-get install virtualbox

Step 3. Now go to location where you downloaded Genymotion and run below command

chmod +x genymotion-2.2.2_x64.bin(check the version of genymotion you downloaded and replace 
"genymotion-2.2.2_x64.bin" with it.)

and after this

./genymotion-2.2.2_x64.bin(your downloaded version)

Step 4. Open Genymotion and create virtual device first

Step 5. Select Android virtual device available to install from the list

Step 6. Install virtual device you want, but recommended is Samsung Galaxy S5 -4.4.4 for this test.


STEPS TO RUN THE TEST ON UBUNTU
================================

# Create a directory on your machine that you will be working from

Clone the github repository into your working directory

      * git clone https://github.com/Xolani-Mxoxozi/Automation-Testing-Demo.git

TO RUN THE DEMO
================

# open the demo in terminal

      * Working directory

# Run the command

The tests will run from the parent folder.

Web Testing:
      *behave Web\ Testing/

Second_web_demo:
      *behave Second_web_demo/*

android_behave
      *behave android_behave/*
To be able to run the demos, you must open the project folders and read the *README* files 
