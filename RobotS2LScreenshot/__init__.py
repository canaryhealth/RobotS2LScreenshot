# -*- coding: utf-8 -*-
import os
                                                    
from robot.libraries.BuiltIn import BuiltIn
from PIL import Image, ImageDraw


class RobotS2LScreenshot:
  '''
  Provides additional keywords to augment screenshots capabilities of 
  RobotFramework's Selenium2Library, namely cropping and masking to help with 
  perceptual diff testing.
  '''

  def capture_and_crop_page_screenshot(self, filename, locator=None):
    '''
    Captures page screenshot and crops to specified element.
    '''
    s2l = BuiltIn().get_library_instance('Selenium2Library')
    # note: filename is required because otherwise we don't have reference to 
    #       auto-generated filename
    s2l.capture_page_screenshot(filename)

    element = s2l._element_find(locator, True, False)
    if element is None:
      raise AssertionError("Could not locate element for '%s'" % (locator))
    x, y = element.location['x'], element.location['y']
    w, h = element.size['width'], element.size['height']

    self.crop_image(filename, [x, y, x+w, y+h])


  def capture_and_mask_page_screenshot(self, filename, locators=None):
    '''
    Captures page screenshot and masks specified element.
    '''
    s2l = BuiltIn().get_library_instance('Selenium2Library')
    # note: filename is required because otherwise we don't have reference to 
    #       auto-generated filename
    s2l.capture_page_screenshot(filename)

    rectangles = []

    for locator in locators:
      element = s2l._element_find(locator, True, False)
      if element is None:
        raise AssertionError("Could not locate element for '%s'" % (locator))
      x, y = element.location['x'], element.location['y']
      w, h = element.size['width'], element.size['height']
      rectangles.append([x, y, x+w, y+h])

    self.mask_image(filename, rectangles)


  def crop_image(self, screenshot, rectangle):
    '''
    Crops image to defined rectangle (in [x0, y0, x1, y1] format).
    '''
    variables = BuiltIn().get_variables()
    outputdir = variables['${OUTPUTDIR}']
    screenshot = os.path.join(outputdir, screenshot)

    img = Image.open(screenshot)
    area = img.crop(tuple(rectangle))
    area.save(screenshot, 'png')


  def mask_image(self, screenshot, rectangles):
    '''
    Masks areas defined by rectangles (in [x0, y0, x1, y1] format) with 
    transparency.
    '''
    variables = BuiltIn().get_variables()
    outputdir = variables['${OUTPUTDIR}']
    screenshot = os.path.join(outputdir, screenshot)

    img = Image.open(screenshot)
    draw = ImageDraw.Draw(img)
    for rectangle in rectangles:
      # "delete" specified rectangle area
      draw.rectangle(rectangle, fill=(255,255,255,0))
    img.save(screenshot, 'PNG')
