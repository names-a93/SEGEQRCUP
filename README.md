# SEGEQRCUP

Securely Generate QR Codes Using Python

Given: Python & a desktop with no camera & no safe extremely local data transfer.

Required: A secure/private/quick method to exchange short amounts of text.

 - requires pip installation of Pillow and qrcode packages
 - pip is a python package manager
 - this is a script and is not beautiful or easy to use for non-programmers

$ pip install Pillow
$ pip install qrcode

$ python gen_qrcode.py

Explanation
  - run program
  - input or paste secret text into terminal when prompted
  - program will try to open common image viewer within desktop
  - point your capture device at the QR code
  - copy/use your text
  - end program by pressing enter
  - ^C or CMD/CONTROL+C will keep the image
  - it's recommend to delete images after use

NOTES:
If you think this is stupid I think you're stupid.
If you don't like the code, make it better.
I understand the insecure argument about this, however if you have any sort of screen logger or key logger. Your security is pretty much cooked anyways.
