import os

n = 29
i = 3
while i <= n :
    path_dir = 'C:\\Users\\wushuang\\Desktop\\baby\\mk watch II\\' + str(i) + '\\'

    if os.path.exists(path_dir):
        pass
    else:
        os.mkdir(path_dir)
    i = i + 1