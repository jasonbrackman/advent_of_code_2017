class QuickUnionUF:

    def __init__(self, n: int):
        self.id = [index for index in range(n)]

    def root(self, i: int):
        while i != self.id[i]:
            i = self.id[i]
        return i

    def connected(self, p: int, q: int):
        return self.root(p) == self.root(q)

    def union(self, p: int, q: int):
        i = self.root(p)
        j = self.root(q)
        self.id[i] = j


def get_data():
    with open('./input/day_14.txt', 'rt') as handle:
        lines = handle.readlines()
        lines = [line.zfill(128).strip() for line in lines]
    return lines


def main():
    lines = get_data()

    x = len(lines[0])
    y = len(lines)

    qf = QuickUnionUF(x*y)
    for idx in range(x):
        for idy in range(y):
            id_ = idx * x + idy

            current = lines[idx][idy]
            if current == '1':
                up    = lines[idx][idy-1] if idy-1 >= 0 else None
                down  = lines[idx][idy+1] if idy+1 < y else None
                left  = lines[idx-1][idy] if idx-1 >= 0 else None
                right = lines[idx+1][idy] if idx+1 < x else None
                if up == '1':
                    qf.union(idx*x+idy-1, id_)
                if down == '1':
                    qf.union(id_, idx*x+idy+1)
                if left == '1':
                    qf.union((idx-1)*x+idy, id_)
                if right == '1':
                    qf.union(id_, (idx+1)*x+idy)
            else:
                qf.union(id_, 0)

    return qf


if __name__ == "__main__":
    qf = main()
    print("Part Two: ", len(set([qf.root(index) for index in range(128*128)])) - 1)