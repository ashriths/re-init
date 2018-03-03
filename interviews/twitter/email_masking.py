# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import sys

# ! # $ % & ' * + - / = ? ^ _ ` { | } ~
input = [
    'E: jackAndJill@twitter.com',
    'P: +13334445678'
]


#for inp in sys.stdin:
for inp in input:
    match = re.match(r'E: *([a-zA-Z0-9\!\#\$\%\&\'\*\+-\/\=\?\^\_\`\{\|\}\~]+)@(.+\..+)', inp)
    if match:
        groups = match.groups()
        print 'E:' + groups[0][0] + '*' * 5 + groups[0][-1] + '@' + groups[1]

    match = re.match(r'P: *(\+?) *([0-9]*)[ -]*[ \(-]*([0-9]{3})[ \)-]*([0-9]{3})[- ]*([0-9][0-9][0-9][0-9])', inp)
    # print match
    if match:
        g = match.groups()
        print g
        _g= []
        for k,v in enumerate(g):
            s = ('*' * len(v)) if (k in [1,2,3]) else v
            _g.append(s)
        print _g
        #k = ['*' * len(v) for k,v in enumerate(g) if k in [1,2,3] else v]
        print "%s%s-%s-%s-%s" % tuple(_g)
        # for p in g:
        #     if p == '+':
        #         print p,
        #     else:
        #         print '-' + p,

        #print 'P: ' + g[]
        #print 'P:' + scan2 + inp_2




