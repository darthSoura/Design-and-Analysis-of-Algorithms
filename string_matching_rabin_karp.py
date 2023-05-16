def rabin_karp_string_match(text, pattern, prime=101):
    n = len(text)
    m = len(pattern)
    matches = []
    d = 256
    h = pow(d, m - 1) % prime

    p = 0
    t = 0

    for i in range(m):
        p = (d * p + ord(pattern[i])) % prime
        t = (d * t + ord(text[i])) % prime

    for i in range(n - m + 1):
        if p == t:
            if pattern == text[i:i + m]:
                matches.append(i)
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % prime
            if t < 0:
                t += prime

    return matches


text = "ABABDABACDABABCABAB"
pattern = "DABABCABA"

matches = rabin_karp_string_match(text, pattern)
print("Rabin-Karp Algorithm:")
if matches:
    print("Pattern found at indices:", matches)
else:
    print("Pattern not found.")
