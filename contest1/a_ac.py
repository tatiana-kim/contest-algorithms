troom, tcond = map(int, input().split())
mode = input()

if mode == "heat":
    if troom < tcond:
        print(tcond)
    else:
        print(troom)
elif mode == "freeze":
    if troom <= tcond:
        print(troom)
    else:
        print(tcond)
elif mode == "auto":
    print(tcond)
else:  # mode == "fun"
    print(troom)
    