import sys
from collections import deque

n = int(sys.stdin.readline())
length = int(sys.stdin.readline())
ioi_list = deque(sys.stdin.readline().strip())
answer = 0

while ioi_list:
    count = 0
    c = ioi_list.popleft()
    if c == 'I':
        while ioi_list:
            left = ioi_list.popleft()
            if left == 'O':
                if ioi_list:
                    if ioi_list.popleft() == 'I':
                        count += 1
                    else:
                        break
                else:
                    break
            else:
                ioi_list.appendleft(left)
                break
        answer += count + 1 - n if count + 1 - n > 0 else 0
    else:
        pass   
            
sys.stdout.write(str(answer) + '\n')