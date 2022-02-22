import os


def init_project(project_name: str):
    if not project_name:
        return


if __name__ == "__main__":
    dirs = ['settings', 'mainapp', 'adminapp', 'authapp']
    for i in dirs:
        dir_path = os.path.join('my_project', i)
        os.makedirs(name=dir_path, exist_ok=True)
