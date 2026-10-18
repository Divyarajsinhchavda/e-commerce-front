# Expert system prototype: plant disease diagnosis with certainty factors
print("Name: Chavda Divyaraj S. | Enrollment: 240905040018 | Batch: ____\n")
rules = [
    ({"yellow_leaves", "wet_soil"}, "Root rot", 0.8,
     "Reduce watering, improve drainage"),
    ({"white_powder"}, "Powdery mildew", 0.9, "Spray neem oil"),
    ({"brown_spots", "yellow_leaves"}, "Leaf blight", 0.7,
     "Remove infected leaves, apply fungicide"),
    ({"holes_in_leaves"}, "Pest attack", 0.6, "Use organic pesticide"),
]

def diagnose(symptoms):
    results = []
    for cond, disease, cf, advice in rules:
        matched = len(cond & symptoms) / len(cond)
        if matched == 1:
            results.append((cf, disease, advice))
    return sorted(results, reverse=True)

cases = [{"yellow_leaves", "wet_soil"},
         {"brown_spots", "yellow_leaves", "holes_in_leaves"},
         {"dry_soil"}]
for s in cases:
    print("Symptoms :", sorted(s))
    found = diagnose(s)
    if not found:
        print("  Result : No rule matched - consult an expert")
    for cf, disease, advice in found:
        print(f"  Result : {disease} (CF {cf}) -> {advice}")
    print()
