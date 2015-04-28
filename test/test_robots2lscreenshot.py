# -*- coding: utf-8 -*-
'''
Nose wrapper that runs the test files using robot and then compare the 
screenshots using perceptualdiff.
'''
import glob
import os
import subprocess
import string
import sys
import unittest

from robot.running.builder import TestSuiteBuilder


class TestRobotS2LScreenshot(unittest.TestCase):
  def robot_launcher(self, test_file, test_case):
    # run robot test
    p = subprocess.Popen(['pybot', '-t', test_case, test_file],
                         close_fds=True,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    sys.stdout.write(p.communicate()[0])
    self.assertEqual(
      p.returncode, 0, 
      msg='Robot test case failed to complete successfully: %r' % p.returncode)

    # diff screenshots with baseline
    curr_img = test_case + '.png'
    base_img = 'baseline-' + curr_img
    diff_img = 'diff-' + curr_img
    d = subprocess.Popen(['perceptualdiff', base_img, curr_img, 
                          '-output', diff_img],
                         close_fds=True,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    sys.stdout.write(d.communicate()[0])
    self.assertEqual(
      d.returncode, 0, 
      msg='Screenshots are different: %r' % d.returncode)
                          
                          

robot_files = glob.glob(os.path.join(os.path.dirname(__file__), 'test*.txt'))
for robot_file in robot_files:
  robot_suite = TestSuiteBuilder().build(robot_file)
  for robot_case in robot_suite.tests:
    def maker(tf, tc):
      def test_run(self):
        self.robot_launcher(tf, tc)
      return test_run
    test_name = string.replace(robot_suite.name + '.' + robot_case.name, ' ', '_')
    setattr(TestRobotS2LScreenshot, test_name, maker(robot_file, robot_case.name))
