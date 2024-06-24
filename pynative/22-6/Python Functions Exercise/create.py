import os

path = "F:/pycharm/pynative/22-6/Python Functions Exercise"
if not os.path.exists(path):
    os.mkdir(path)

# so luong can tao file
amount = 9
for i in range(1,amount + 1 ):
    file_path = os.path.join(path, f"{i}.py")
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"{file_path} deleted")
    with(open(file_path,"w")) as file:
        pass
    print(f"{i}.py done")
