# Frame-based knowledge with inheritance and forward chaining
print("Name: Chavda Divyaraj S. | Enrollment: 240905040018 | Batch: ____\n")
frames = {
    "Vehicle": {"is_a": None, "wheels": 4, "uses": "road"},
    "Car":     {"is_a": "Vehicle", "seats": 5},
    "Bike":    {"is_a": "Vehicle", "wheels": 2, "seats": 2},
    "EV":      {"is_a": "Car", "fuel": "electric"},
}

def get(frame, slot):                       # inherit slot from parent
    while frame:
        if slot in frames[frame]:
            return frames[frame][slot]
        frame = frames[frame]["is_a"]
    return "unknown"

for f in ("EV", "Bike"):
    print(f"{f}: wheels={get(f, 'wheels')}, seats={get(f, 'seats')}, "
          f"uses={get(f, 'uses')}, fuel={get(f, 'fuel')}")

rules = [({"electric"}, "zero_tailpipe_emission"),
         ({"zero_tailpipe_emission"}, "eco_friendly"),
         ({"eco_friendly", "4_wheels"}, "green_family_car")]
facts = {"electric", "4_wheels"}
print("\nForward chaining from", sorted(facts))
added = True
while added:
    added = False
    for cond, result in rules:
        if cond <= facts and result not in facts:
            facts.add(result)
            added = True
            print(f"  {sorted(cond)} => {result}")
print("Final facts:", sorted(facts))
