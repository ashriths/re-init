from collections import defaultdict

def find_ancestors(node, parents):
    _parents = []
    if node in parents:
        for n in parents[node]:
            _parents.extend([n] + find_ancestors(n, parents))
    return _parents

def have_shared_ancestor(pairs, node_a, node_b):
    # IMPLEMENTATION GOES HERE
    parents = defaultdict(list)
    covered_a = []
    for pair in pairs:
        parents[pair[1]].append(pair[0])
    an_a = set(find_ancestors(node_a, parents))
    an_b = set(find_ancestors(node_b, parents))
    if len(an_a.intersection(an_b)) > 0:
        return True
    return False




# START TEST CASES
#
# You can add test cases below. Each test case should be a dict of the format:
#
# {
#     "name": "my custom test",
#     "pairs": ...,
#     "node_a": ...,
#     "node_b": ...,
#     "expected_output": ...
# }


tests = [
    {
        "name": "sample input #1",
        "pairs": [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [8, 9]],
        "node_a": 3,
        "node_b": 8,
        "expected_output": False,
    },
    {
        "name": "sample input #2",
        "pairs": [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [8, 9]],
        "node_a": 5,
        "node_b": 8,
        "expected_output": True,
    },
    {
        "name": "sample input #3",
        "pairs": [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [8, 9]],
        "node_a": 6,
        "node_b": 8,
        "expected_output": True,
    }
];

# END TEST CASES
# DO NOT MODIFY BELOW THIS LINE

def main():
    def equal_outputs(a, b):
        return a == b

    passed = 0

    for test in tests:
        try:
            print("==> Testing {}...".format(test['name']))
            actual_output = have_shared_ancestor(test['pairs'], test['node_a'], test['node_b'])
            if equal_outputs(actual_output, test['expected_output']):
                print("PASS")
                passed += 1
            else:
                print("FAIL")
                print("Expected output: {}".format(test['expected_output']))
                print("Actual output: {}".format(actual_output))
        except Exception as e:
            print("FAIL")
            print(e)

    print("==> Passed {} of {} tests".format(passed, len(tests)))

if __name__ == '__main__':
    main()

