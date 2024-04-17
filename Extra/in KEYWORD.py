names: list[str] = ["bob","tom","janems"]
#consise
if "bob" in names:
    print("yes")

#long
for name in names:
    if name == "bob":
        print("yes")
        break