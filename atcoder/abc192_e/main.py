#!/usr/bin/env python3
# from typing import *



# def solve(N: str, M: str, X: str, Y: str, A: List[str], B: List[str], T: List[str], K: List[str]) -> int:
def solve(N, M, X, Y, A, B, T, K):
    pass  # TODO: edit here

# generated by oj-template v4.7.2 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M, X, Y = input().split()
    A = [None for _ in range(M)]
    B = [None for _ in range(M)]
    T = [None for _ in range(M)]
    K = [None for _ in range(M)]
    for i in range(M):
        A[i], B[i], T[i], K[i] = input().split()
    a = solve(N, M, X, Y, A, B, T, K)
    print(a)

if __name__ == '__main__':
    main()
