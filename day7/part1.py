f = open("day7/input.txt")

class Directory:
    def __init__(self, name : str, parent):
        self.name = name
        self.parent = parent
        self.childern = {}
        self.files = {}
        self.size = 0

root = Directory("/", None)
cur = None
for line in f:
    line = line.strip()
    line = line.split(" ")
    if line[0] == '$':
        if line[1] == "cd":
            if line[2] == "/":
                cur = root
            elif line[2] == "..":
                cur = cur.parent
            else:
                if line[2] in cur.childern:
                    cur = cur.childern[ line[2] ] 

        elif line[1] == "ls":
            continue
    else:
        if line[0] == "dir":
            cur.childern[line[1]] = Directory(line[1], cur)
        else:
            cur.files[line[1]] = int(line[0])

def dfs_print(dir: Directory, indent: int):
    startln =  " " * indent + "- "
    print(startln + dir.name + "(dir, size =" + str(dir.size) + ")")
    for child in dir.childern:
        dfs_print(dir.childern[child], indent+1)
    for file in dir.files.keys():
        print(startln + "|" + file + "(size=" + str(dir.files[file]) + ")" )
    
def dfs_size(dir: Directory) -> int:
    for file_size in dir.files.values():
        dir.size += file_size
    for child in dir.childern.values():
        dir.size += dfs_size(child)
    return dir.size

def dfs_res(dir: Directory, res:list[int])->None:
    if dir.size <= 100000:
        res.append(dir.size)
    for child in dir.childern.values():
        dfs_res(child, res)

res = []
dfs_size(root)
dfs_print(root, 0)
dfs_res(root, res)
print( sum(res) )

f.close()