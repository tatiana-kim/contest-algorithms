# troom, tcond = input().split()
# troom, tcond = int(troom), int(tcond)
# while (troom < -50 or troom > 50) and (tcond < -50 or tcond > 50):
#     troom, tcond = input().split()
#     troom, tcond = int(troom), int(tcond)

# mode = input()
# while mode not in ("heat", "freeze", "auto", "fun"):
#     print('Available options are: "heat", "freeze", "auto", "fun"')
#     mode = input()
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
    