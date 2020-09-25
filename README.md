# Business Card Parser Application

- [Description](#Description)
- [Using the App](#Using-the-App)
- [Python Module](#Python-Module)
- [Acknowledgements](#Acknowledgements)

---

### Description

The business card parser is a tool developed using the Python programming language to quickly pull key information from a document containing business card information. Specifically, the parser will identify the card owner's name, telephone number, and email address, in order to quickly record contact information for future use. This repository contains a stand-alone executable which can be used out of the box and will launch a GUI interface for users to enter text data, as well as a python module that can be directly incorporated into an existing python project.

### Using the App

To use the card parser application, simply run the executable file. Enter the business card information into the text field and hit the get information button to get the resulting name, phone number, and email address displayed on the right side of the GUI. 

__IMPORTANT NOTES__

1. The input text should be line separated, similar to how it would appear on the actual business card (top). Adding the text as a single line separated only by spaces will lead to errors, chiefly in parsing the card owner's name (bottom) due to the implementation of the parse method.

![](images/card_parser.png)

2. The first_name and last_name text files must be kept in the same directory as the executable file. Separating the files will lead to errors in the application and will cause it to crash.

Once the information has been parsed and displayed, users can save the data to a csv file by using the save file button. This will create a saved_cards directory in the application root directory, with the data saved under headers in the following order: Last name, first name, phone number, and email address.

### Python Module

To add the card parser functionality to another python project, simply copy the card_parser.py file and both name text files into the project directory. Import the BusinessCardParser class from the module and instantiate the class. Once created, call the BusinessCardParser.getContactInfo(text) function, where text is the string containing the business card information. This will create a ContactInfo object with attributes name, phone, and email. For more detail, please read the comments in the code files.

__IMPORTANT NOTES__

The same conditions for using the application apply for using the module as well. The getContactInfo function expects a string that is separated by the newline character \n, so when passing arguments to the function it is important to ensure that it is formatted correctly, or similar errors as described above will occur. Similarly, if the module and the name text files are separated, the file path must be changed accordingly in card_parser.py to point it to the correct location.

### Acknowledgments

The text files containing the list of first and last names were taken from the names_dataset repository, which can be found [__here__](https://github.com/philipperemy/name-dataset).

All credit for those assets go to the repository's owner.