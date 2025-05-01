import sys

sentences = sys.stdin.read().splitlines()
filtered_sentences = []
for sen in sentences[:-1]:
    filtered_string = ''
    for s in sen:
        if s in ['(', ')', '[', ']']:
            filtered_string += s
    
    filtered_sentences.append(filtered_string)

for sen in filtered_sentences:
    for i in range(len(sen) // 2 + 1):
        sen = sen.replace('()', '')
        sen = sen.replace('[]', '')
        if len(sen) == 0:
            print('yes')
            break
    else:
        print('no')