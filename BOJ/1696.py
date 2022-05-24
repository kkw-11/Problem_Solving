from itertools import product
import sys

input = sys.stdin.readline

n,m = map(int,input().split())
DNAs = []
for _ in range(n):
    DNAs.append(input().rstrip())

nucleotides = ["A","C","G","T"] #알파벳 순서로
DNA = ""
# DNA의 각 위치별로 가장 빈도수 높은 Nucleotide를 체크
for i in range(m):
    nucleotide_cnt = {"A":0,"C":0,"G":0,"T":0}
    for j in range(n):
        nucleotide_cnt[DNAs[j][i]] += 1

    nucleotide = max(nucleotide_cnt.values())

    for key in nucleotides:
        if nucleotide_cnt[key] == nucleotide:
            DNA += key
            break
cnt = 0
for i in range(n):
    for j in range(m):
        if DNA[j] != DNAs[i][j]:
            cnt += 1
print(DNA)
print(cnt)