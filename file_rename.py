from typing import List
import re
from os import chdir, rename, listdir
from os.path import isfile, join


class FileRename:
    def __init__(self, dir_path: str, original_format: str, new_format: str):
        self.dir_path = dir_path
        self.original_format = original_format
        self.new_format = new_format

    def rename_files_in_directory(self, assign_numbering: bool = False):
        """
        Rename files in specified directory based on given regex
        :param assign_numbering: If true, numbering will be added to the new file name (eg. test_1.txt)
        """
        try:
            files: List[str] = self.get_files_in_directory()
            chdir(self.dir_path)

            if files:
                current_number: int = 1
                for file in files:
                    new_name: str = re.sub(self.original_format, self.new_format, file)

                    if assign_numbering:
                        rename(file, f'{new_name}_{current_number}')
                    else:
                        rename(file, new_name)
                print('Done!')

        except Exception as ex:
            print(ex)

    def get_files_in_directory(self) -> List[str]:
        """
        Gets all files in specified directory
        :return: List of files
        """
        files: List[str] = [f for f in listdir(self.dir_path) if isfile(join(self.dir_path, f))]
        return files
