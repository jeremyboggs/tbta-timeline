#!/usr/bin/env python

import csv

TIMELINE_CSV = 'administrative-response-timeline.csv'

def entry(date,headline,text):
    args = {'arg1':headline, 'arg2':text, 'arg3':date}
    return '''<div class="entry">
    <div class="icon">
        <img src="img/rotunda.png" alt="">
    </div>
    <h2>{arg1}</h2>
    <p>{arg2}</p>
    <div class="date">{arg3}</div>
</div>\n'''.format(**args)


with open(TIMELINE_CSV, 'rU') as file_in:
    with open('timeline.html', 'w') as file_out:
        reader = csv.reader(file_in)
        reader.next()
        for row in reader:
            date = row[0]
            headline = row[3]
            text = row[4]
            entry_content = entry(date,headline,text)
            file_out.write(entry_content)

