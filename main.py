"""
Parsing a file with English and Russian words into separate files.

This module is designed to parse .txt and .csv files containing columns
with English and Russian words into separate files containing columns for each language.

The module contains 2 classes:
    - A class that implements the context manager protocol for creating recursive files.
    - A class that implements DataFrame creation and text parsing operations
      using a third-party Pandas library and standard Itertools.

Usage example is following:
    Input data:
        *.txt or *.csv file containing strings with translations of English words into Russian in the format:
            <Astur-Leonese ; Asturian; Asturian-Leonese; Astur    астурийский ; астурлеонский>
    Result data:
        created English.txt and Russian.txt files (default names, can be changed), where each line in English will
        correspond to a translation line in Russian in another file in all possible variants,
        created on the basisof the input file.
"""
import pandas as pd
from itertools import zip_longest
from typing import TextIO


class ResultFilesCreator:
    """
    The class implements the context manager protocol, designed to create two resulting files.
    """
    first_file: TextIO
    second_file: TextIO

    def __init__(self, first_file_path: str, second_file_path: str, method: str):
        """
        :param first_file_path: the path to the file that will contain the column with words in English.
        :type first_file_path: TextIO

        :param second_file_path: the path to the file that will contain the column with words in Russian.
        :type second_file_path: TextIO
        """
        self.first_file = open(first_file_path, method)
        self.second_file = open(second_file_path, method)

    def __enter__(self):
        """
        :return: generated files with given names
        :rtype tuple
        """
        return self.first_file, self.second_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ Сloses both files

        :return: None
        """
        self.first_file.close()
        self.second_file.close()


class EnRuParser:
    """
    The class creates a dataframe based on the path, delimiter, number of skipped lines in the input file
    and field names, after which it is possible to separate and write columns with data in different languages
    into separate files using the process method.
    """
    path_to_file: str
    delimiter: str
    skip_row: int
    headlines: tuple = ('en', 'ru')
    dataframe: pd.DataFrame

    def __init__(self,
                 path_to_file: str = 'PythonTest.txt',
                 delimiter: str = '\t',
                 skip_row: int = 0):
        """
        :param path_to_file: path to *.txt or *.csv file containing a table with raw data for parsing
        :type path_to_file: str

        :param delimiter: separator located between columns with English and Russian words
        :type delimiter: str

        :param skip_row: number of lines from the first line of the file to the beginning of the table
        :type skip_row: int
        """
        self.path_to_file = path_to_file
        self.delimiter = delimiter
        self.skip_row = skip_row
        self.dataframe = pd.read_csv(self.path_to_file,
                                     delimiter=self.delimiter,
                                     skiprows=self.skip_row,
                                     names=self.headlines)

    def process(self, first_file_path: str = 'English.txt', second_file_path: str = 'Russian.txt', method: str = 'w'):
        """
        Parses the source file data and writes to new files obtained from the 'ResultFilesCreator' class.

        :param first_file_path: path to a file containing data in English
        :type first_file_path: str

        :param second_file_path: path to a file containing data in Russian
        :type second_file_path: str

        :param method: one of the following methods for opening python files ('r', 'w', 'x', 'a', 'b', 't', '+')
        :type method: str

        :return: None
        :rtype: None
        """
        with ResultFilesCreator(first_file_path, second_file_path, method) as result_files:
            en_file, ru_file = result_files
            for _, row in self.dataframe.iterrows():
                result = zip_longest(row[0].split(' ; '), row[1].split(' ; '), fillvalue=row[1].split(' ; ')[0])
                for i in result:
                    en_file.write(i[0] + '\n')
                    ru_file.write(i[1] + '\n')


if __name__ == '__main__':
    test_parser = EnRuParser(skip_row=33)
    test_parser.process()
