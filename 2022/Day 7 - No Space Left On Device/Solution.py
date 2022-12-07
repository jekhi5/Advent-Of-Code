#!/usr/bin/env python3

file = open("input.txt")
loi = file.read()
dirs = loi.split("$ cd ")
del dirs[0]
file.close()

def get_dir_size(d, parent):

    total = 0
    subd = []
    d = d.split("\n")
    del d[0]
    for elem in d:
        if not elem.startswith("$") and elem != "":
            if elem.startswith("dir "):
                subd_name = parent + elem[4:]
                subd.append(subd_name)
            else:
                total += int(elem[0:elem.find(" ")])

    return [total, subd]

def dive_deep(dirs, key):
    subd = dirs[key][1]

    for d in subd:
        if len(dirs[d][1]) > 0:
            dirs = dive_deep(dirs, d)
        
        dirs[key][0] += dirs[d][0]
    
    dirs[key][1] = []
    return dirs

def Solution(inpt):
    
    directories = {}

    result = 0
    history = []
    parent = ""
    for d in dirs:
        if d.find("..") > -1:
            former = history.pop()
            parent = parent[0:len(parent) - len(former)]
            continue
        
        history.append(d[0:d.find("\n")])
        parent += history[len(history) - 1]

        name = parent
        result_pair = get_dir_size(d, parent)
        directories[name] = result_pair
    keys = list(directories.keys())
    for key in keys:
        directories = dive_deep(directories, key)
        
    for entry in directories:
        if directories[entry][0] <= 100000:
            result += directories[entry][0]


    #print(directories)   
    return [result, directories]

print(Solution(dirs)[0])

def Solution2(inpt):
    prior_result = Solution(inpt)
    calced = prior_result[1]
    req = 30000000 - (70000000 - calced["/"][0])
    sorted_keys = sorted(calced.items(), key=lambda x: x[1][0], reverse=True)


    prev = sorted_keys[1][0]
    for key in sorted_keys:
        if key[0] == "/":
            continue
        elif key[1][0] < req:
            return prev
        else:
            prev = key[1][0]

print(Solution2(dirs))
