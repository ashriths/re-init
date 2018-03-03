# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import re
import shlex
import datetime


def _print_lines(eps, time):
    for k, v in eps.iteritems():
        p = [c > 499 for c in v]
        p = 100 - (sum(p) * 1.0 / len(v)) * 100
        print time, k, p


eps = {}
time = None
for line in sys.stdin:
    _line = shlex.split(line)
    e = _line[5].split()[1].split('?')[0]
    code = int(_line[6])
    t = datetime.datetime.strptime(_line[3][1:], "%d/%b/%Y:%H:%M:%S").isoformat()[:-3]
    # print t,time, e, code, eps
    if t != time and time is not None:
        # print it out
        _print_lines(eps, time)
        eps = {}
        time = t
    if e in eps:
        eps[e].append(code)
    else:
        eps[e] = [code]
    time = t
if eps:
    _print_lines(eps, time)
    # print t, time, eps


