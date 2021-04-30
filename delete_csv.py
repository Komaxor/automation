import os.path


def delete_csv(file_name):
    path = 'imdbcast/' + file_name
    if os.path.exists(path):
        os.remove(path)  # NOTE maybe overwrite to empty instead of deleting
