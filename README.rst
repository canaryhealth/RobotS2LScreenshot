==================
RobotS2LScreenshot
==================

Provides additional keywords to augment screenshots capabilities of 
RobotFramework's Selenium2Library, namely cropping and masking to help with 
perceptual diff testing.


Usage
=====

.. code::

  Capture main area only
    Capture And Crop Page Screenshot  example1.png  css=div.main

  Capture and mask logo and submit button
    ${locators}  Create List  xpath=//span[@class='logo']  xpath=//button[text()='Save']
    Capture and Mask Page Screenshot  example2.png  locators=${locators}

  Capture and mask areas
    # areas are specified as x,y,w,h
    ${rects}  Create List  10,20,25,25  30,40,50,50
    Capture and Mask Page Screenshot  example2.png  rects=${rects}


Dependencies
============

- Selenuim2
- RobotFramework
- Selenium2Library (Robot Library)
- Pillow
- PerceptualDiff **(you will need to install this separately)**
