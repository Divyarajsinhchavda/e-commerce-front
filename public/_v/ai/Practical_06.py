# Propositional and predicate logic for a college domain
from itertools import product
print("Name: Chavda Divyaraj S. | Enrollment: 240905040018 | Batch: ____\n")
# Propositional: KB = (Study -> Pass), (Pass -> Degree), Study
# Query: does KB entail Degree?  (check every model)
imp = lambda a, b: (not a) or b
entails = True
print("Study Pass Degree | KB    Degree")
for s, p, d in product([True, False], repeat=3):
    kb = imp(s, p) and imp(p, d) and s
    print(f"{s!s:<5} {p!s:<5} {d!s:<6} | {kb!s:<5} {d}")
    if kb and not d:
        entails = False
print("KB |= Degree :", entails)

# Predicate logic: Prereq(x, y), Passed(s, x)
# Rule: forall s,y  CanTake(s, y) <- forall x (Prereq(x, y) -> Passed(s, x))
prereq = {("Python", "AI"), ("Maths", "AI"), ("DBMS", "DataMining")}
passed = {("Riya", "Python"), ("Riya", "Maths"), ("Aman", "Python")}
def can_take(s, course):
    return all((s, x) in passed for x, y in prereq if y == course)
print()
for s in ("Riya", "Aman"):
    print(f"CanTake({s}, AI) :", can_take(s, "AI"))
print("Exists s Passed(s, Maths):",
      any(c == "Maths" for _, c in passed))
