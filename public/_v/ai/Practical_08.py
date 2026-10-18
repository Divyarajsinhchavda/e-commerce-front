# Blocks world planning with STRIPS operators (goal stack style)
print("Name: Chavda Divyaraj S. | Enrollment: 240905040018 | Batch: ____\n")
state = {"on(A,B)", "on(B,table)", "on(C,table)", "clear(A)", "clear(C)"}
goal = ["on(B,C)", "on(A,B)"]                     # build A on B on C

def blocks():
    return ["A", "B", "C"]

def move(x, frm, to):
    pre = {f"on({x},{frm})", f"clear({x})"}
    if to != "table":
        pre.add(f"clear({to})")
    add, dele = {f"on({x},{to})"}, {f"on({x},{frm})"}
    if frm != "table":
        add.add(f"clear({frm})")
    if to != "table":
        dele.add(f"clear({to})")
    return pre, add, dele

def achieve(fact, plan):
    global state
    if fact in state:
        return
    x, to = fact[3:-1].split(",")
    frm = next(f[3:-1].split(",")[1] for f in state
               if f.startswith(f"on({x},"))
    # sub-goals: clear x and clear destination (stack them first)
    for y in blocks():
        if f"on({y},{x})" in state:
            achieve(f"on({y},table)", plan)
        if to != "table" and f"on({y},{to})" in state:
            achieve(f"on({y},table)", plan)
    pre, add, dele = move(x, frm, to)
    if pre <= state:
        state = (state - dele) | add
        plan.append(f"MOVE({x}, {frm} -> {to})")

plan = []
for g in goal:
    achieve(g, plan)
print("Plan:")
for i, step in enumerate(plan, 1):
    print(f"  {i}. {step}")
print("Goal reached:", all(g in state for g in goal))
