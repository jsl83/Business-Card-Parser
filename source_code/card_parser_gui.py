import tkinter as tk
import tkinter.font as tf
import re
import os
from csv import writer
from card_parser import BusinessCardParser

bcp = BusinessCardParser()

def get_info():
    '''
    Function called with the get info button
    Reads in text from the text input field and calls the getContactInfo method from
    the BusinessCardParser to get the information of interest. Modifies output label
    text to display the results
    '''
    info = bcp.getContactInfo(in_text.get('1.0', tk.END))

    out_label['text'] = 'Name:\n' + info.getName() + '\n\nPhone:\n' + info.getPhoneNumber() + '\n\nEmail:\n' + info.getEmailAddress()
    # Show the save to file button, erase file saved message if present
    message_label['text']=''
    save_button.pack()

def save_to_file():
    '''
    Function called to save the displayed results in a csv file for future use
    Information is saved as [last name, first name, phone number, email address]
    '''
    # Gets results from the output label text and splits it by line, pulling out the information by line number
    if out_label['text'] != '':
        lines = out_label['text'].split('\n')
        name = lines[1].split()
        info = [name[1], name[0], lines[4], lines[7]]
        # Check to see if save folder exists - if it doesn't creates the save folder and the save file with appropriate headers
        if not os.path.exists('saved_cards'):
            os.makedirs('saved_cards')
            with open('saved_cards/saved_cards.csv', 'w+') as file:
                csv_writer = writer(file, lineterminator='\n')
                csv_writer.writerow(['Last Name', 'First Name','Phone Number','Email Address'])
        # Write the results to the csv file
        with open('saved_cards/saved_cards.csv', 'a') as file:
            csv_writer = writer(file, lineterminator='\n')
            csv_writer.writerow(info)
        # Hide the save file button to prevent creating duplicate entries
        save_button.pack_forget()
        message_label['text']='Card saved'

        
# Create tkinter root window
window = tk.Tk()
window.configure(bg='grey30')
window.title('Card Parser')

# App title
big_font = tf.Font(size=18)
title_label = tk.Label(text='Business Card Parser GUI', font=big_font, fg='ghost white', bg='grey30', height=2, width=35)


bottom_frame = tk.Frame(master=window, bg='grey30', height=10, width=400)

# Left frame contains the input text field and get info button
left_frame = tk.Frame(master=bottom_frame, relief=tk.RIDGE, borderwidth=5, bg='grey30', width=300, height=230)
in_label = tk.Label(text="Input business card information", master=left_frame, bg='grey30', fg='ghost white')
in_text = tk.Text(master=left_frame, height=10, width=35)
parse_button = tk.Button(text='Get info', command=get_info, master=left_frame)

# Right frame contains the results (out) label and save button
right_frame = tk.Frame(master=bottom_frame, relief=tk.RIDGE, borderwidth=5, bg='grey30', width=300, height=230)
out_label = tk.Label(text='', master=right_frame, width=35, bg='grey30', fg='ghost white', height=10)
message_label = tk.Label(text='', master=right_frame, bg='grey30', fg='red')
save_button = tk.Button(text='Save to file', master=right_frame, command=save_to_file)

# Add all widgets to the GUI
for x in [in_label, in_text, parse_button, out_label, message_label, save_button]:
    x.pack()

for x in [left_frame, right_frame]:
    x.pack(fill=tk.X, side=tk.LEFT)
    x.pack_propagate(0)

for x in [title_label, bottom_frame]:
    x.pack()

# Hide save button until the app has been used at least once
save_button.pack_forget()

# Show the GUI    
window.mainloop()
