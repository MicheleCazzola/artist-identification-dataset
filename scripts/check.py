LEN = 21220

ft = open("train.txt", "r")
fv = open("test.txt", "r")

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

sample = tr[0]

tr = set(tr)
tst = set(tst)

assert not tr.intersection(tst)

assert len(tst) + len(tr) == LEN

check_read(sample)

ft.close()
fv.close()
