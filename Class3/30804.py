import sys
from collections import deque

n = int(sys.stdin.readline())

class_list = deque(map(int, sys.stdin.readline().strip().split()))

print(class_list)