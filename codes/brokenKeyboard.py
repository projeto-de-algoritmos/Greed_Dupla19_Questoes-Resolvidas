for _ in range(int(input())):
    n = int(input())
    s = input()
    print('YES' if n % 3 != 2 and not False in [s[i * 3 + 1] == s[i * 3 + 2] for i in range(n // 3)] else 'NO')