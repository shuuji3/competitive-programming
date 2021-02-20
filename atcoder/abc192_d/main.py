#!/usr/bin/env python3
# from typing import *

# def solve(X: str, M: int) -> int:
def solve(X, M):
    base = int(max(list(X))) + 1
    count = 0

    while base <= 36 and int(X, base=base) <= M:
        count += 1
        base += 1

    return count

# generated by oj-template v4.7.2 (https://github.com/online-judge-tools/template-generator)
def main():
    X = input()
    M = int(input())
    a = solve(X, M)
    print(a)

if __name__ == '__main__':
    main()
