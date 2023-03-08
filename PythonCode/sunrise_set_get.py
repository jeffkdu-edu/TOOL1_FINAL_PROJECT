#%% Python Requests Module
import requests
import re
import csv

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

# create a list of regex to filter and remove unwanted data
REGEX_REPLACEMENTS = [
    (r"Sunrise", ''),
    (r"Sunset", ''),
    (r"Dawn", ''),
    (r"Day Length", ''),
    (r"<th>", ''),
    (r"</th>", ''),
    (r"<td>", ''),
    (r"</td>", ''),
    (r"<span class.*</span>", '')
]

outList = []

# deal with the pagination for 2023. Cycle through all the months and get url data
for month in months:
    url = f'https://www.sunrisesunsettime.org/north-america/united-states/las-cruces-{month}.htm'
    #print(url)
    r = requests.get(url)
    print(r.status_code)
    print(r.encoding)
    html = r.text

    for line in html.split('\n'):
        if '<th>' in line or ('<td>' and '<span>' and '</span></td>') in line or ('<td>' and '<span>' and '</span></td>') in line:
            for old, new in REGEX_REPLACEMENTS:
                line = re.sub(old, new, line, flags=re.IGNORECASE)
            newline = re.sub(r"[\n\t]*", "", line)
            outList.append(newline)

#print(outList)

# %% Process the scraped data 
goutlist = []
tupList = []
outList2 = []
outList3 = []

while("" in outList): #remove blank lines
    outList.remove("")

for element in outList: # create a clean list of values
    goutlist.append(element)

#print(goutlist)
for i in range(3, len(goutlist), 3): #don't need Dec 31 last year start at record 3
    tupList.append((goutlist[i].split(','), goutlist[i + 1], goutlist[i + 2]))

#print(tupList)

for i in range(len(tupList)):
    date = tupList[i][0][1].strip().split(' ')
    sunrise = tupList[i][1].strip()
    sunset = tupList[i][2].strip()
    outList2.append([date, sunrise, sunset])

# use list comprehension to remove duplicate values
[outList3.append(x) for x in outList2 if x not in outList3]
print(outList3)
# %% Write data to a text file
with open('sunrise_set_2023.csv', mode='w', newline='') as suntimes:
    writer = csv.writer(suntimes)
    for i in range(len(outList3)):
        writer.writerow([outList3[i][0][1], outList3[i][0][0], outList3[i][1], outList3[i][2]])
# %%
