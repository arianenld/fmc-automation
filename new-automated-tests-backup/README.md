# fmc-automation

Splinter Setup on Mac

1. install python3
brew install python3

2. install splinter, see https://splinter.readthedocs.io/en/latest/install.html
python3 -m pip install splinter

IF you encounter this error: ModuleNotFoundError: No module named 'six'
run $ python3 -m pip install six

3. install requests library 
sudo pip3 install requests

Test Execution: On target directory, run $ python3 testFile.py