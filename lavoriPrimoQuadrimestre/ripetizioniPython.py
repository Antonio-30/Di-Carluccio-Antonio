s=str(input("Inserisci una stringa: "))
ripetizioni=0
for i in range(0, len(s)):
    r=1
    x=s[i]
    for j in range(i+1, len(s)):
        if s[i] == s[j]:
            r = r + 1
    if r > ripetizioni:
        carattere = x
        ripetizioni = r
print(carattere)
print(ripetizioni)
