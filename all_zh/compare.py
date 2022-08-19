

def lines(fi):
    tmp = set()
    print(f"Read {fi}")
    with open(fi, "r") as rf:
        for li in rf:
            line = li.rstrip()
            if line in tmp:
                print(f"Found extra {line}")
            tmp |= set((line))
            yield line

def line_set(fi):
    return set(lines(fi))


if __name__ == "__main__":

    files = ["kx.txt", "ix.txt"]

    sets = [line_set(fi) for fi in files]

    print([len(s) for s in sets])

    comparisons = [(0,1)]
    for comp in comparisons:
        s_a = sets[comp[0]]
        s_b = sets[comp[1]]
        f_a = files[comp[0]]
        f_b = files[comp[1]]

        print(f"Comparing {f_a} and {f_b}")

        a_no_b = s_a - s_b
        b_no_a = s_b - s_a
        a_has = len(a_no_b)
        b_has = len(b_no_a)

        print(f"\tJust {f_a} has {a_has} lines.")
        print(", ".join(list(a_no_b)))
        print(f"\tJust {f_b} has {b_has} lines.")
        print(", ".join(list(b_no_a)))
