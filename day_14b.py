class QuickFindUF:

    def __init__(self, n):
        """Constructor"""
        self.id = [index for index in range(n)]

    def connected(self, p: int, q: int):
        return self.id[p] == self.id[q]

    def union(self, p: int, q: int):
        pid = self.id[p]
        qid = self.id[q]

        for index in range(len(self.id)):
            if self.id[index] == pid:
                self.id[index] = qid


def get_data():
    with open('./input/day_14.txt', 'rt') as handle:
        lines = handle.readlines()
        lines = [line.zfill(128).strip() for line in lines]
    return lines


def main():
    lines = get_data()

    x = len(lines[0])
    y = len(lines)

    qf = QuickFindUF(x*y)
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
    print("Part Two: ", len(set(qf.id))-1)