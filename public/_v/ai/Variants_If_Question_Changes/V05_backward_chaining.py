# Backward chaining: start from the goal and work back to known facts
print("Name: Chavda Divyaraj S. | Enrollment: 240905040018 | Batch: ____\n")
rules = {                                # goal : [list of alternatives (each a list of conditions)]
    "can_fly":   [["is_bird", "has_wings"]],
    "is_bird":   [["has_feathers", "lays_eggs"]],
    "has_wings": [["is_bird"]],
}
facts = {"has_feathers", "lays_eggs"}

def prove(goal, depth=0):
    pad = "  " * depth
    if goal in facts:
        print(f"{pad}{goal}: known fact -> True")
        return True
    for conds in rules.get(goal, []):
        print(f"{pad}{goal}: try rule {conds}")
        if all(prove(c, depth + 1) for c in conds):
            print(f"{pad}{goal}: proved -> True")
            return True
    print(f"{pad}{goal}: cannot be proved -> False")
    return False

print("Facts:", sorted(facts))
print("\nGoal: can_fly")
print("Result:", prove("can_fly"))
print("\nGoal: can_swim")
print("Result:", prove("can_swim"))
