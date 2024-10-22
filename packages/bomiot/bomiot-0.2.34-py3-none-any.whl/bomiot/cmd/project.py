from os.path import join, exists
from os import makedirs, getcwd
import sys
import shutil
from pathlib import Path
from .create import create_file
import pkg_resources


def project(folder: str):
    """
    project workspace
    :param folder:
    :return:
    """
    if len(sys.argv) < 3:
        print('Please enter your project name')
    else:
        project_path = join(getcwd(), sys.argv[2])
        if exists(project_path):
            print('Project directory already exists')
        else:
            if sys.argv[2] in [pkg.key for pkg in pkg_resources.working_set]:
                print('Plugins directory already exists')
            else:
                makedirs(project_path)
                current_path = Path(__file__).resolve()
                file_path = join(current_path.parent, 'file')

                shutil.copy2(join(file_path, '__version__.py'), project_path)

                with open(join(project_path, '__init__.py'), "w") as f:
                    f.write("def version():\n")
                    f.write(f"    from {sys.argv[2]} import __version__\n")
                    f.write("    return __version__.version()\n")
                f.close()

                shutil.copy2(join(file_path, 'config.ini'), project_path)
                shutil.copy2(join(file_path, 'bomiotconf.py'), project_path)

                create_file(str(sys.argv[2]))

                print('Initialized project workspace %s' % sys.argv[2])
