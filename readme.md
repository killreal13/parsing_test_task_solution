EnRuParser

#### This module is designed to parse .txt and .csv files containing columns with English and Russian words into separate files containing columns for each language.

    *.txt (Astur-Leonese ; Asturian ; Asturian-Leonese ; Astur	астурийский ; астурлеонский) ->  

    English.txt         Russian.txt		

    Astur-Leonese       астурийский
    Astur-Leonese       астурлеонский
    Asturian            астурийский
    Asturian            астурлеонский
    Asturian-Leonese    астурийский
    Asturian-Leonese    астурлеонский

### HOW TO RUN:

*Run the following commands:*
    
    1. pip install -r requirements.txt
    2. create a parser object in 'main.py' file and pass optional parameters if necessary:
        'if __name__ == '__main__':
            test_parser = EnRuParser()
            test_parser.process()'
    3*. you can provide optional parameters for the object:
        - 'path_to_file' containing the path to the raw data '*.txt' or '*.csv 'file; 
        - 'delimiter' table column separator;
        - 'skip_row' number of lines from the first line of the file to the beginning of the table;
        - 'headlines' table field names.
    

*USED PACKAGES AND MODULES:*

- Python 3.10
- Pandas 1.4.3
- Itertools
- Typing