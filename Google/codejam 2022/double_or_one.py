t =  int(input())

def duplicate(word):
    new_word = []
    i = 1
    while i < len(word):
        if word[i-1] < word[i]:
            l = 2*word[i-1]
            new_word.append(l)
            i += 1
        elif word[i-1] == word[i]:
            count = 0
            for j in range(i-1,len(word)):
                if word[j] != word[i-1]: 
                    break
                else:
                    count +=1
                new_position = j
            try:
                if word[new_position] < word[new_position + 1]:
                    new_word.append(word[i-1]*2*count)
                else:
                    new_word.append(word[i-1]*count)
            except:
                new_word.append(word[i-1]*(count-1))
            i += count  + 1
        else:
            new_word.append(word[i-1])
            i += 1

    new_word.append(word[len(word)-1])
    print(*new_word, sep='')

for i  in range (t):
    word = input()
    word_members = []
    for letter in word:
        word_members.append(letter)

    print(f"Case #{i+1}: " , end = ''),
    duplicate(word_members)