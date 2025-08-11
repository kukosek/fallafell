from string import Template 
import os
from datetime import datetime
import sys

SHOWS_DIR = 'content/shows/'
shows_done = sorted(os.listdir(SHOWS_DIR), reverse=True)
newest_show_done = ""
newest_show_number = 0

for show_done in shows_done:
    if '_' in show_done:
        show_number_str, show_title = show_done.split('_', 1)
        try:
            show_number = int(show_number_str)
        except Exception:
            continue
        if show_number > newest_show_number:
            newest_show_done = show_title
            newest_show_number = show_number

if len(sys.argv) > 1:
    shows_filename = sys.argv[1]
else:
    print("Please enter an input file as argument.")
    exit()

with open(shows_filename, 'r') as f:
    shows_text = f.readlines()

with open('scripts/template.md', 'r') as f:
    template_string = f.read()

t = Template(template_string)

for show_text in shows_text:
    date, title = show_text.split(' ', 1)
    datetime_object = datetime.strptime(date, '%d.%m.%Y')
    date = datetime_object.strftime('%Y-%m-%d')
    output = t.substitute(title=title, date=date)

    newest_show_number += 1
    
    if ',' in title:
        town = title.split(',', 1)[0]
    else:
        town = title

    new_filename = str(newest_show_number)+"_"+town+'.md'
    
    with open(SHOWS_DIR+new_filename, 'w+') as f:
        f.write(output)
    print('Created file:',new_filename)
