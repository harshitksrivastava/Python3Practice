import re

patterns = ['term1','term2']

text = 'This is a string with term1, not not the other!'

for pattern in patterns:
    print("I'm searching for: "+pattern)
# pattern in re.search(what_we_are_looking_for, in_what_we_are_looking_for)
    if( re.search(pattern,text)):
        print('Match!')
    else:
        print("No Match!")
    # match = re.search('term1',text)
    # print(match.start())
#========================================================
print(re.findall('match','test phrase match in match midle'))
