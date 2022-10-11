def spisok(names):
    folders = dict()
    for x in names:
        i = 0
        while i < len(x) and x[i].isalpha():
            i += 1
        if x[:i] == "Семинар":
            folders["Семинары"] += [x]
        elif folders.get(x[:i]):
            folders[x[:i]] += [x]
        else:
            folders[x[:i]] = [x]
    return folders


names = ["Лист 1", "Лист 2", "Лист 3", "Листок 2","Семинары 2", "Семинар 1", "Семинар 2", "Семинары 4"]
print(spisok(names))

