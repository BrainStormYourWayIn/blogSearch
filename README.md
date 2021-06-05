# blogSearch

![logo](https://github.com/BrainStormYourWayIn/blogSearch/blob/main/blogSearch-removebg-preview.png)

A web-based blog searcher.

__________________

## 1. Package installation

Once you have downloaded the package and unzipped it in a directory, open a console window, go to the directory and run:

`pip freeze > requirements.txt`

This should create the requirements.txt file in the correct format. Then try installing using the command.

`pip install -r requirements.txt`

Make sure you're in the same folder as the file when running this command.
If you get some path name instead of the version number in the requirements.txt file, use this pip command to work around it.

`pip list --format=freeze > requirements.txt`

This will install the requirements in the Python distribution.

__________________

## 2. Run main.py to start the Blog Search Engine

__________________

## Optional use

Start the built-in server

To start the server, type:

`streamlit run test_streamlit.py`

This will execute the program on Streamlit.

**Note:** Initial search runtime on startup may take ~30 secs depending on the machine.

__________________

## Note for Users

We will be adding a file called test_streamlit.py, which the users can modify, if they want to contribute to the project. Due to issues with page redirection, this 

will be updated as part of a later release. Users, however, can freely modify this if they want to contribute to the project. Issues will be prioritized for main.py

in the current status.
