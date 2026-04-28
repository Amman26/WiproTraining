import re

'''txt = input('Enter a text') # india is my country
bpat = input('Enter beginning pattern') #india
bpat = '^' + bpat #^India
epat = '$' + epat #try$

if re.search(pattern=bpat,string=txt):
    print('Beginning pat available')
else:
    print('Beginning pat not available')'''

#digit
'''txt = input('Enter a text ')'''
'''mbno = input('Enter a text ')
pat = '[0-9]'

if re.search(pattern = pat, string=mbno):
    print('Only digits')
else:
    print('Only chars available')'''

#username
'''un = input('Enter UN ')
pat = r"[a-z_]{8}$"

if re.match(pattern=pat, string=un):
    print('Valid')
else:
    print('Invalid')'''

#email
emailadd = input('Email ')
pat = r"^[a-zA-z0-9_]+@[a-z]+\.[a-z]+$"
if re.match(pattern=pat, string=emailadd):
    print('Valid')
else:
    print('Invalid')
#pwd
'''pwdtxt = input('pwd : ')
pat = (r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])"
       r"(?=.*[@_-]).{8,}$")

if re.match(pattern=pat, string=pwdtxt):
    print('Valid')
else:
    print('Invalid')'''

txt = input('Text')
pat = r"\s+"

print(re.split(pattern=pat, string=txt))