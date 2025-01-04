LEN = 21220

ft = open("train.txt", "r")
fv = open("test.txt", "r")
fg = open("validation.txt", "r")

def read(file) -> set[str]:
    names = []
    for line in file:
        names.append(line.strip())

    assert sorted(names) == sorted(set(names))
    return names


def check_read(name):
    with open(name, "rb") as f:
        print(name)

tr = read(ft)
tst = read(fv)
val = read(fg)

sample = tr[0]

tr = set(tr)
tst = set(tst)
val = set(val)

assert not tr.intersection(tst)
assert not tr.intersection(val)
assert not tst.intersection(val)

assert len(tst) + len(tr) + len(val) == LEN


check_read(sample)

ft.close()
fv.close()
fg.close()
