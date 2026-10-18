# Simple reflex vacuum agent showing AI components, AI types and uses
print("Name: Chavda Divyaraj S. | Enrollment: 240905040018 | Batch: ____\n")
world = {"A": "Dirty", "B": "Dirty"}       # environment
location = "A"                               # agent position

def perceive():                              # perception
    return location, world[location]

def decide(percept):                         # reasoning (condition-action)
    loc, status = percept
    if status == "Dirty":
        return "Suck"
    return "Right" if loc == "A" else "Left"

print("Agent run (Perceive -> Decide -> Act):")
for step in range(1, 5):
    percept = perceive()
    action = decide(percept)
    print(f"  Step {step}: percept={percept} action={action}")
    if action == "Suck":                     # action changes environment
        world[location] = "Clean"
    else:
        location = "B" if action == "Right" else "A"
print("  Final world:", world)

ai_types = [("Reactive machine", "Deep Blue chess computer"),
            ("Limited memory", "Self-driving car"),
            ("Theory of mind", "Social robots (research)"),
            ("Self-aware", "Not yet built")]
print("\nCategories of intelligent systems:")
for kind, example in ai_types:
    print(f"  {kind:<17}-> {example}")

uses = {"Agriculture": "Crop disease detection",
        "Education": "Personalised tutoring",
        "Retail": "Demand forecasting"}
print("\nReal-world case studies:")
for area, use in uses.items():
    print(f"  {area:<12}: {use}")
