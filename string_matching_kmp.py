def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []

    lps = compute_lps(pattern)
    i = j = 0

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

            if j == m:
                matches.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches


text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

matches = kmp_string_match(text, pattern)
print("Knuth-Morris-Pratt (KMP) Algorithm:")
if matches:
    print("Pattern found at indices:", matches)
else:
    print("Pattern not found.")
