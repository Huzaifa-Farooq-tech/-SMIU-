while True:
    s = input("Enter Char/Num: ")
    # print(chr(int(s)) if s.isdigit() else ord(s))
    if s.isdigit():
        c = int(s)
        print(f"{c} -> {repr(chr(c))}")
    else:
        print(f"{s} -> {ord(s)}")

        