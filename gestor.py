import cmd
from dataclasses import field
from fileinput import filename
import shutil
import os


def open_file(file_name):
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    path = os.path.join(script_dir, file_name)

    if os.path.exists(path):
        file = open(path, "r")

        print(file.read())
    else:
        print("Este archivo no existe")


def delete_file(file_name):
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    path = os.path.join(script_dir, file_name)

    if os.path.exists(path):
        os.remove(path)
    else:
        print("Este archivo no existe")


def create_file(file_name):
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    path = os.path.join(script_dir, file_name)
    f = open(path, 'a')


def move_file(file_name, dest_file_name):

    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    path = os.path.join(script_dir, file_name)
    dest_path = os.path.join(script_dir, dest_file_name)
    shutil.move(path, dest_path)


def modify_file(file_name, content):
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    path = os.path.join(script_dir, file_name)

    if os.path.exists(path):
        file = open(path, "w")
        file.write(content)
        file.close()
    else:
        print("Este archivo no existe")


def overwrite_file(file_name, content):
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    path = os.path.join(script_dir, file_name)

    if os.path.exists(path):
        file = open(path, 'w')
        file.write(content)
        file.close
    else:
        print("Este archivo no existe")


def create_directory(file_name):
    # Path
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    path = os.path.join(script_dir, file_name)

    # Create the dir_name
    try:
        os.makedirs(path)
        print("Directory '%s' created successfully" % script_dir)
    except OSError as error:
        print("Directory '%s' can not be created" % script_dir)


class Shell(cmd.Cmd):
    intro = "Bienvenido a tu gestor de archivo \n Escribe ? o Ayuda para ver todos los comandos.\n Escribe bye para abandonar"
    prompt = "Gestor ->"
    file = None

    # Basic file management system commands
    def do_CREATE_FILE(self, arg):
        print(arg)
        create_file(str(arg))

    def do_DELETE_FILE(self, arg):
        delete_file(str(arg))

    def do_OPEN_FILE(self, arg):
        open_file(str(arg))

    def do_MODIFY_FILE(self, arg):
        split_args = arg.split('"')
        modify_file(split_args[0], split_args[1])

    def do_OVERWRITE_FILE(self, arg):
        split_args = arg.split()
        overwrite_file(split_args[0], split_args[1])

    def do_CREATE_DIR(self, arg):
        create_directory(str(arg))

    def do_bye(self, arg):
        'Stop recording, close the turtle window, and exit:  BYE'
        print('Bye bye!')
        self.close()
        return True

    def do_MOVE_FILE(self, arg):
        split_args = arg.split()
        print(split_args[0], split_args[1])
        move_file(str(split_args[0]), str(split_args[1]))

    def close(self):
        if self.file:
            self.file.close()
            self.file = None


def main():
    shell = Shell()

    try:
        shell.cmdloop()
    except Exception as e:
        print(f"Perdon, no estabamos esperando eso. {e}")


if __name__ == "__main__":
    main()
