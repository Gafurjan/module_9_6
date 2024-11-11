def all_variants(text):
    j = 0
    # for i in text:
    #     yield i
    for i in range (len(text)*2):
        if i < len(text):
            yield text[i]
            i += 1
        elif j < len(text) - 1:
            yield text[j] + text[j + 1]
            j += 1
        else:
            yield text

a = all_variants("abc")
for i in a:
    print(i)