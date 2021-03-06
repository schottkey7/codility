"""https://codility.com/demo/take-sample-test/frog_river_one/."""


def solution(X, A):
    """Get to position X in A in as little time as possible."""
    unvisited = set([x for x in range(1, X + 1)])
    for i, n in enumerate(A):
        unvisited.discard(n)
        if len(unvisited) == 0:
            return i
    return -1
