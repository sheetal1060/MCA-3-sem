def evenString(s):
    for i in range(len(s)):
        if i % 2 == 0:
            print(s[i], end='')
    print()  

evenString("aligarh")
