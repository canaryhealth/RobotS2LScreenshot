============
Instructions
============

All commands and files assumes you are in the ``/tests`` directory.


Generate baseline images
========================

1. Run the robot test natively

.. code:: bash

  pybot test_robots2lscreenshot.txt


2. Inspect the output images
3. Rename them as baseline images

.. code:: bash

  mv 'Screenshot cropped to myform.png' 'baseline-Screenshot cropped to myform.png'
  mv 'Screenshot with header and footer masked.png' 'baseline-Screenshot with header and footer masked.png'


Run unit tests
==============

.. code:: bash

  nosetests -v test_robots2lscreenshot.txt


If the screenshots populated by the test cases are different from the baselines', differential images will be generated with the ``diff-`` prefix.
