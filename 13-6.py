for hod in range(100, 1000):
    mat = 3 * hod
    if mat >= 1000:
        continue

    x = hod // 100
    o = (hod // 10) % 10
    d = hod % 10

    m = mat // 100
    a = (mat // 10) % 10
    t = mat % 10

    if len({x, o, d, m, a, t}) == 6:
        if x != 0 and m != 0:
            print(f"{hod}+{hod}+{hod}={mat}")

