"""Practical 10: test suite for course_module.py using four testing techniques."""
from course_module import course_fee as fee, enrollment_status as status
V, T = "ValueError", "TypeError"
# each case: (description, function, arguments, expected result or error name)
EP = [  # equivalence partitioning: one value from every valid / invalid class
    ("valid price, valid coupon", fee, (2000, 10), 1800.0),
    ("valid price, no coupon", fee, (2000,), 2000.0),
    ("price below range", fee, (-500, 10), V),
    ("price above range", fee, (90000, 10), V),
    ("coupon below range", fee, (2000, -5), V),
    ("coupon above range", fee, (2000, 80), V),
]
BVA = [  # boundary value analysis: price 1 and 50000, coupon 0 and 50
    ("price 0 (below min)", fee, (0, 10), V),
    ("price 1 (min)", fee, (1, 0), 1.0),
    ("price 2 (above min)", fee, (2, 0), 2.0),
    ("price 49999 (below max)", fee, (49999, 0), 49999.0),
    ("price 50000 (max)", fee, (50000, 0), 50000.0),
    ("price 50001 (above max)", fee, (50001, 0), V),
    ("coupon -1 (below min)", fee, (1000, -1), V),
    ("coupon 0 (min)", fee, (1000, 0), 1000.0),
    ("coupon 1 (above min)", fee, (1000, 1), 990.0),
    ("coupon 49 (below max)", fee, (1000, 49), 510.0),
    ("coupon 50 (max)", fee, (1000, 50), 500.0),
    ("coupon 51 (above max)", fee, (1000, 51), V),
]
DT = [  # decision table: logged in / payment done / seats available
    ("R1 not logged in", status, (False, True, 5), "Login Required"),
    ("R1 not logged in, full", status, (False, False, 0), "Login Required"),
    ("R2 payment pending", status, (True, False, 5), "Payment Pending"),
    ("R2 payment pending, full", status, (True, False, 0), "Payment Pending"),
    ("R3 paid, seats available", status, (True, True, 5), "Enrolled"),
    ("R4 paid, no seats", status, (True, True, 0), "Waitlisted"),
]
EG = [  # error guessing: inputs a developer may forget
    ("price as string", fee, ("2000", 10), T),
    ("price is None", fee, (None, 10), T),
    ("price is True", fee, (True, 0), T),
    ("coupon as string", fee, (2000, "10"), T),
    ("decimal price and coupon", fee, (999.99, 33.5), 664.99),
    ("negative seats", status, (True, True, -1), V),
    ("seats as string", status, (True, True, "5"), T),
    ("seats as float", status, (True, True, 2.5), T),
]
def execute(func, args):
    try:
        return func(*args)
    except Exception as error:
        return type(error).__name__
total = passed = 0
summary = []
for title, prefix, cases in [("EQUIVALENCE PARTITIONING", "EP", EP),
                             ("BOUNDARY VALUE ANALYSIS", "BVA", BVA),
                             ("DECISION TABLE TESTING", "DT", DT),
                             ("ERROR GUESSING", "EG", EG)]:
    print(f"\n{title}")
    print(f"{'ID':<8}{'Description':<28}{'Expected':<17}{'Actual':<17}Result")
    ok_count = 0
    for no, (desc, func, args, expected) in enumerate(cases, 1):
        actual = execute(func, args)
        ok_count += actual == expected
        print(f"{prefix}-{no:02d}".ljust(8) + f"{desc:<28}{str(expected):<17}"
              f"{str(actual):<17}{'PASS' if actual == expected else 'FAIL'}")
    summary.append((title, len(cases), ok_count))
print(f"\n{'Technique':<30}{'Total':>6}{'Passed':>8}{'Failed':>8}")
for title, count, ok in summary:
    print(f"{title:<30}{count:>6}{ok:>8}{count - ok:>8}")
total, passed = sum(s[1] for s in summary), sum(s[2] for s in summary)
print(f"{'TOTAL':<30}{total:>6}{passed:>8}{total - passed:>8}")
print("RESULT:", "ALL TESTS PASSED" if total == passed else "SOME TESTS FAILED")
