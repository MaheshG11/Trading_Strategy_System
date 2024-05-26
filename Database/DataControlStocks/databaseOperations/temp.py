l = set()
with open("../listOfStocksAll", "r") as f:
    while True:
        a = f.readline()
        if len(a) == 0:
            break
        a = a[:-1]
        l.add(a[-2:])
f.close()
print(l)
exit()
with open("listOfStocks", "w") as f:
    for i in l:
        if i[-2:] == "BO":
            f.write(i + "\n")
f.close()
