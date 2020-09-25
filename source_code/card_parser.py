import re

# The files containing the list of first and last names, as well as
# the following two instructions for reading those files are taken
# from the source code for the names_dataset library, available at

# https://github.com/philipperemy/name-dataset

# All credit for these assets go to the repository's owner
with open('first_names.txt', 'r', errors='ignore', encoding='utf8') as r:
            first_names = set(r.read().strip().split('\n'))
with open('last_names.txt', 'r', errors='ignore', encoding='utf8') as r:
            last_names = set(r.read().strip().split('\n'))

def parseName(text):
    '''
    Function to pull the name of the business card owner
    Argument text (string) = multiline text containing the business card information
    Returns the line of text in which every word is a name
    If no such line is found, returns all lines which contain any words with names in them,
    otherwise returns a blank string
    '''
    
    name = ''
    name_lines = ''
    
    # Split text by line breaks
    lines = text.split('\n')
    for line in lines:
        # Check each line of text for non-alphabetical characters, skips the line if any are found
        if not line == '' and len(re.findall(r'^(a-zA-Z\s:)', line))==0:
            # Tokenize line into individual words
            words = line.lower().split()
            # added boolean denotes if the line has been added to name_lines
            added = False
            # all_names boolean denotes if every checked word is a name
            all_names = True
            for word in words:
                # Check each word if they are in the first/last_names list
                is_first = word in first_names
                is_last = word in last_names
                # If it is, add the line to name_lines, set added to True to prevent adding the same line again for a different word
                if (is_first or is_last) and not added:
                    name_lines += line
                    added = True
                # If the word is not a name, all_names = False, the line is not all name words
                if not is_first and not is_last:
                    all_names = False
            if all_names:
                name = line
    # If no lines are all name words, return name_lines instead
    if name == '':
        name = name_lines
    return name

def parsePhone(text):
    '''
    Function to pull the telephone number of the business card owner
    Argument text (string) = multiline text containing the business card information
    Returns the match to the regex expression searching for sequences of at least seven digits,
    grouped in 3 and 4, separated by no more than 3 characters. Optional regex matches for area
    code and country code
    If multiple matches are found, returns the match in the line containing at least one of the
    following key words: tel, telephone, phone, and cell
    '''    
    numbers = ''
    # Find matches to the regex for phone numbers
    matches = re.findall(r'(?:\d\D{0,4})?(?:\d{3}\D{0,4})?\d{3}\D{0,3}\d{4}', text)
    if len(matches) == 1:
        numbers = matches[0]
    # If more than one match is found, checks each line for the presence of words indicating phone and returns the corresponding match
    elif len(matches) > 1:
        lines = [line.lower() for line in text.split('\n')]
        for line in lines:
            if any(tel_words in line for tel_words in ['tel','telephone','phone','cell']):
                numbers = re.findall(r'(?:\d\D{0,4})?(?:\d{3}\D{0,4})?\d{3}\D{0,3}\d{4}', line)[0]
    # Remove non-numerical characters before returning phone number
    return re.sub('[^\d]', '', numbers)

def parseEmail(text):
    '''
    Function to pull the email address of the business card owner
    Argument text (string) = multiline text containing the business card information
    Returns the match to the regex for <text>@<text>.<text> if any, otherwise returns blank string
    '''
    email = ''
    matches = re.findall(r'\S+@\S+\.\S+', text)
    if len(matches) > 0:
        email = matches[0]
    return email

class BusinessCardParser:
    '''
    The card parser class. At present implementation, no class variables are necessary. This may change
    in the future as we continue to develop the parser to incorporate more sophisticated functions
    '''
    
    def __init__(self): 
        pass
    
    def getContactInfo(self, card_text):
        '''
        Function which creates a ContactInfo object from the business card text
        Argument card_text (string) = multiline text containing the business card information
        '''

        return ContactInfo(parseName(card_text), parsePhone(card_text), parseEmail(card_text))

class ContactInfo:
    '''
    Contact information class. Stores the name, phone number, and email for each card in one object.
    Currently only contains those class variables and methods for retrieving those values. Additional
    functionalities may be added as we continue to develop the parser
    '''
    
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def getName(self):
        return self.name

    def getPhoneNumber(self):
        return self.phone

    def getEmailAddress(self):
        return self.email
