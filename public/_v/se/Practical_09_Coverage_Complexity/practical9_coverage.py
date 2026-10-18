"""Practical 9: cyclomatic complexity and test coverage of certificate_status()."""
import ast, inspect, sys
def certificate_status(progress, quiz_score, assignments_done):
    if progress >= 80:
        if quiz_score >= 50:
            if assignments_done:
                status = "Certificate Issued"
            else:
                status = "Submit Assignments"
        else:
            status = "Retake Quiz"
    else:
        status = "Course Incomplete"
    return status
TESTS = [  # name, (progress, quiz score, assignments done), expected result
    ("TC1", (90, 70, True), "Certificate Issued"),
    ("TC2", (90, 70, False), "Submit Assignments"),
    ("TC3", (90, 30, True), "Retake Quiz"),
    ("TC4", (50, 70, True), "Course Incomplete"),
]
func = ast.parse(inspect.getsource(certificate_status)).body[0]
base = certificate_status.__code__.co_firstlineno - 1     # source line -> file line
statements = {n.lineno + base for n in ast.walk(func) if isinstance(n, ast.stmt)}
statements -= {func.lineno + base}                           # ignore the def line
ifs = [n for n in ast.walk(func) if isinstance(n, ast.If)]
vg = len(ifs) + 1                                            # V(G) = P + 1
def run(args):
    lines = []
    def tracer(frame, event, arg):
        if frame.f_code is certificate_status.__code__:
            if event == "line":
                lines.append(frame.f_lineno)
            return tracer
    sys.settrace(tracer)
    result = certificate_status(*args)
    sys.settrace(None)
    return result, tuple(lines)
def report(tests, rows=True):
    hit, paths = set(), set()
    for name, args, expected in tests:
        result, lines = run(args)
        hit.update(lines)
        paths.add(lines)
        if rows:
            print(f"{name:<5}{str(args):<19}{expected:<20}{result:<20}"
                  f"{'PASS' if result == expected else 'FAIL'}")
    branches = sum((n.body[0].lineno + base in hit)
                   + (n.orelse[0].lineno + base in hit) for n in ifs)
    for name, done, total in [("Statement", len(statements & hit), len(statements)),
                              ("Branch", branches, 2 * len(ifs)),
                              ("Path", len(paths), vg)]:
        pct = 100 * done / total
        print(f"  {name + ' coverage':<20}{done}/{total} = {pct:.1f}%")
print(f"CYCLOMATIC COMPLEXITY: P = {len(ifs)}, V(G) = P + 1 = {vg}\n")
print("All 4 test cases")
print(f"{'TC':<5}{'Input':<19}{'Expected':<20}{'Actual':<20}Result")
report(TESTS)
print("\nOnly TC1 and TC2")
report(TESTS[:2], rows=False)
