import pickle

f = open('donotshare.p')
o = pickle.load(f)

outstr = ''
for line in o:
    for char, n in line:
        outstr += char * n
    outstr += '\n'
print outstr
