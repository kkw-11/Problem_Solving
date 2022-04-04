
a = [["a","?","c"],["?","a","c"],["a","?","c"]]

for i in range(3):
    for j in range(3):
        if a[i][j] == "?":
            for k in range(3):
                a[i][j] = "a"
                


