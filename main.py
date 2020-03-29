from file_rename import FileRename


def main():
    rename = FileRename('./TestFiles', r'[e]', r'.[w]')
    rename.rename_files_in_directory()


if __name__ == '__main__':
    main()
