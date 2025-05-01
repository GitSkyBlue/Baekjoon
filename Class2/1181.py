n = int(input())

word_dict = {}
for _ in range(n):
    word = input()
    if word_dict.get(len(word)) == None:
        word_dict[len(word)] = set()
        word_dict[len(word)].add(word)
    else:
        word_dict[len(word)].add(word)

for word in sorted(word_dict):
    for w in sorted(word_dict[word]):
        print(w)