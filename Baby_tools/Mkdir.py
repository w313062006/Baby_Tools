import os

n = 24
i = 3
while i <= n :
    path_dir = 'C:\\Users\\wushuang\\Desktop\\baby\\9.18\\longchamp\\' + str(i) + '\\'

    if os.path.exists(path_dir):
        pass
    else:
        os.mkdir(path_dir)
    i = i + 1