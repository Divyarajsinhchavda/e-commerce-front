# Semantic network with is-a inheritance and property lookup
print("Name: Chavda Divyaraj S. | Enrollment: 240905040018 | Batch: ____\n")
is_a = {"Canary": "Bird", "Penguin": "Bird", "Bird": "Animal", "Dog": "Mammal", "Mammal": "Animal"}
props = {"Animal": {"alive": True},
         "Bird": {"can_fly": True, "has_wings": True},
         "Penguin": {"can_fly": False},
         "Canary": {"colour": "yellow"},
         "Mammal": {"has_fur": True}}

def lookup(node, prop):
    path = []
    while node:
        path.append(node)
        if prop in props.get(node, {}):
            return props[node][prop], path
        node = is_a.get(node)
    return "unknown", path

print("Links:")
for child, parent in is_a.items():
    print(f"  {child} --is-a--> {parent}")
print("\nQueries (property inherited from the nearest parent):")
for node, prop in [("Canary", "can_fly"), ("Penguin", "can_fly"), ("Canary", "alive"),
                   ("Dog", "has_fur"), ("Dog", "can_fly")]:
    value, path = lookup(node, prop)
    print(f"  {node}.{prop} = {value}   (searched: {' -> '.join(path)})")
