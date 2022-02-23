import os

if __name__ == "__main__":
    dirs = ['settings', 'mainapp', 'adminapp', 'authapp']
    for i in dirs:
        dir_path = os.path.join('my_project2', i)
        os.makedirs(name=dir_path, exist_ok=True)
