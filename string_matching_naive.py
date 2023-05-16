def naive_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            matches.append(i)

    return matches


text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

matches = naive_string_match(text, pattern)
print("Naive String Matching:")
if matches:
    print("Pattern found at indices:", matches)
else:
    print("Pattern not found.")
