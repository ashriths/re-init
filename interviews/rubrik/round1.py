#
# recurring division, given two integar a, b => "a/b"
# 1/3 = "0.(3)"
# 7/6 = "1.1(6)"
# 4/ 2 = "2" 1/4 = "0.25"
# 1/900 0.(001)
# 2/11
#
#
#
# 1/ 3

def check_repeat(rs):
    if len(rs) < 2:
        return False
    k = set()
    for key, r in enumerate(rs):
        if r in k:
            return True
        k.add(r)


def get_answer(qs, rs):
    start = None
    end = None

    k = set()
    for key, r in enumerate(rs):
        if r in k:
            end = key
            start = rs.index(r)
        k.add(r)
    qs = [str(q) for q in qs]
    print qs
    print start, end
    if start == end:
        start += 1
    if 0 not in rs:
        return qs[0] + '.' + ''.join(qs[1:start]) + '(' + ''.join(qs[start:end + 1]) + ')'
    else:
        return qs[0] + '.' + ''.join(qs[1:])


def div(a, b):
    q, r = divmod(a, b)
    rs = []
    qs = []
    i = 0
    while r != 0 and not check_repeat(rs):
        q, r = divmod(a, b)
        rs.append(r)
        qs.append(q)
        a = 10 * r

    # print qs
    # print rs
    print get_answer(qs, rs)


if __name__ == "__main__":
    # div(7, 6)
    div(7, 6)










