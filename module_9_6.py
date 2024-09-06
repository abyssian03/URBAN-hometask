def all_variants(text):
    i = 0
    while i != len(text):
        k = i
        while k != len(text):
            yield text[i: k]
            k += 1
        i += 1

for str in all_variants("белиберда"):
    print(str)