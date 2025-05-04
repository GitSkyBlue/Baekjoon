import sys

sys.stdin.readline()
answer_list = set(sys.stdin.readline().split())
sys.stdin.readline()
for i in sys.stdin.readline().split():
    print(1 if i in answer_list else 0)