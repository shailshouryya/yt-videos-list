import os


def delete_schafer5_file_if_exists():
    schafer5 = 'schafer5VideosList'
    if os.path.exists(f'{schafer5}.txt'):
        os.remove(f'{schafer5}.txt')
    if os.path.exists(f'{schafer5}.csv'):
        os.remove(f'{schafer5}.csv')
