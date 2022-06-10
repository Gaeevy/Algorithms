import random
from helpers import timeit
from math import log2


class BasicDC:
    def __init__(self, n):
        self.n = n
        self.roots = list(range(n))
        self.unions = 0
        self.operations = 0
        self.already_connected = 0

    @timeit
    def make_unions(self, unions):
        for left, right in unions:
            self.union(left, right)
        self.unions = len(unions)

    def union(self, left, right):
        pass

    def find_root(self, elem):
        pass

    def is_connected(self, left, right):
        return self.find_root(left) == self.find_root(right)

    def __repr__(self):
        return f'Size: {self.n}, unions: {self.unions}, operations: {self.operations}, ' \
               f'share: {self.operations / (log2(self.n) * self.unions)}' \
               f' already connected: {self.already_connected}'


class QuickFind(BasicDC):
    def find_root(self, elem):
        self.operations += 1
        return self.roots[elem]

    def union(self, left, right):
        left_root = self.find_root(left)
        right_root = self.find_root(right)
        if left_root != right_root:
            for i in range(self.n):
                self.operations += 1
                if self.roots[i] == left_root:
                    self.operations += 1
                    self.roots[i] = right_root
        else:
            self.already_connected += 1


class QuickUnion(BasicDC):
    def find_root(self, elem: int) -> int:
        cur, parent = elem, self.roots[elem]
        self.operations += 1
        while parent != cur:
            self.operations += 1
            cur = parent
            parent = self.roots[cur]
        return parent

    def union(self, left, right):
        left_root = self.find_root(left)
        right_root = self.find_root(right)
        if left_root != right_root:
            self.roots[left_root] = right_root
        else:
            self.already_connected += 1


class WeightedQuickUnion(QuickUnion):
    def __init__(self, n):
        super().__init__(n)
        self.sizes = [1 for _ in range(n)]

    def union(self, left, right):
        left_root = self.find_root(left)
        right_root = self.find_root(right)
        if left_root != right_root:
            if self.sizes[left_root] > self.sizes[right_root]:
                self.roots[right_root] = left_root
                self.sizes[left_root] += self.sizes[right_root]
            else:
                self.roots[left_root] = right_root
                self.sizes[right_root] += self.sizes[left_root]
        else:
            self.already_connected += 1


class FlattenWeightedQuickUnion(WeightedQuickUnion):
    def find_root(self, elem: int) -> int:
        cur, parent = elem, self.roots[elem]
        self.operations += 1
        while parent != cur:
            self.operations += 1
            cur = parent
            parent = self.roots[cur]
        self.roots[elem] = parent
        self.operations += 1
        return parent


@timeit
def create_unions(n, m):
    return [(random.randint(0, n-1), random.randint(0, n-1)) for _ in range(m)]


if __name__ == '__main__':
    n = 1 * int(1e3)
    m = 100 * int(n)
    # unions = [(9, 0), (4, 5), (7, 4), (1, 8), (3, 1), (1, 2), (6, 2), (6, 2), (3, 9), (9, 5), (5, 5)]
    unions = create_unions(n, m)
    print(n, m, end='\n\n')

    # qf = QuickFind(n)
    # qf.make_unions(unions)
    # print(qf)
    #
    # qu = QuickUnion(n) # O(n*m)
    # qu.make_unions(unions)
    # print(qu)
    # print()

    wqu = WeightedQuickUnion(n)  # O(log(n)*m)
    wqu.make_unions(unions)
    print(wqu)
    print()

    fwqu = FlattenWeightedQuickUnion(n)  # O(log*(n)*m)
    fwqu.make_unions(unions)
    print(fwqu)
    print()