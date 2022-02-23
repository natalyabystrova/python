import os
import shutil

if __name__ == '__main__':
    for root, dirs, files in os.walk('./my_project'):
        for d in dirs:
            if d == 'templates':
                shutil.copytree(os.path.join(root, d), './templates', dirs_exist_ok=True)
