import errno
import os


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        elif exc.errno in [errno.EPERM, errno.EACCES]:
            print(f"Permission error on {path}")
        else:
            raise


def create_parent_dir(path):
    mkdir_p(os.path.dirname(path))


def delete_all_symlink_in_path(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.islink(file_path):
                os.unlink(file_path)
        for dir in dirs:
            folder_path = os.path.join(root, dir)
            if os.path.islink(folder_path):
                os.unlink(folder_path)


def recreate_symlinks(download_folder, symlinks):
    for symlink in symlinks:
        link_path = os.path.join(download_folder, symlink["path"], symlink["name"])
        os.symlink(symlink["destination"], link_path)


def get_config_path(env_variables):
    path = env_variables.get("XDG_CONFIG_HOME", os.path.expanduser("~/.config"))
    return os.path.join(path, "rhdl")
