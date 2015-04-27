==================
RobotS2LScreenshot
==================

Provides additional keywords to augment screenshots capabilities of 
RobotFramework's Selenium2Library, namely cropping and masking to help with 
perceptual diff testing.


Usage
=====

.. code-block::

Capture main area only
  Capture And Crop Page Screenshot  example1.png  css=div.main

Capture and mask logo and submit button
  ${locators}  Create List  xpath=//span[@class='logo']  xpath=//button[text()='Save']
  Capture and Mask Page Screenshot  example2.png  ${locators}


Dependencies
============

- RobotFramework
- Selenium2Library
- PIL and Pillow
