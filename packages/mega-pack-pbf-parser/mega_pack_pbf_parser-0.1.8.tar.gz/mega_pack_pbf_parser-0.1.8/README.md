# mega-pack-pbf-parser
Parse the content (songs and PBFs) of a BB project w/Mega Pack and add that data to the project database. 
- To write the required html file install this package: bb-pbf-html-writer
- pip install bb-pbf-html-writer

## Warnings
- Verify that the "packs_pbf_type" table is up-to-date. Be certain that ALL products are included in this table (i.e. check for new product releases)
- BEFORE ANYTHING ELSE the full path to the project db must be set the first time you try to run the code. This is handled by the ConfigManager class. 

## ConfigManager

An instance of ConfigManager runs automtically from the package __init__.py file. 
The instance is created before any imports are called:
```python
from .config_manager import ConfigManager
config = ConfigManager()

PROJECT_DB_PATH = config.get_variable("PROJECT_DB_PATH")
BONUS_PBF_FILES = config.get_variable("BONUS_PBF_FILES")
OPP_PBF_FILES = config.get_variable("OPP_PBF_FILES")
```
You'll be asked to provide the full path to the project database. Nothing will work without this.

Some project values ("BONUS_PBF_FILES" and "OPP_PBF_FILES") are stored inside the package (default_config.json) but everything will be writen to a LOCAL mega_pack_pbf_parser_config.json file in the USER's HOME directory. This happens the first time you run any of the code. See the package __init__.py file

## Database Tables
- packs_pbf_type: contains a listing of all PBF names, the associated productand the type (OPP, sections)
- songs: lists all songs, the associated PBF and product name and the type (OPP, sections)

## Usage (NEEDS UPDATING)

```python
from typing import List
from mega_pack_pbf_parser import Project_Parser
from mega_pack_pbf_parser import create_db, insert
from mega_pack_pbf_parser import insert_songs_query
from mega_pack_pbf_parser import initialize_database

from mega_pack_pbf_parser import config as config_manager

def insert_song_data(db_path: str, data: List):
    """
    Inserts song data into the project database. Prints the number of rows inserted.

    Parameters:
    data(List): a list of song info: PBF name, song name, product name, song type
    """
    query = insert_songs_query    
    row_count = insert(db_path=db_path, query=query, data=data)
    print(f"Inserted {row_count} rows into the database.")


def main():    
    bb_project_folder = r"C:\Users\RC\Documents\BBWorkspace\GM_Mega_Pack_Project"
    project_data = config_manager.config_data
    db_path = project_data.get('PROJECT_DB_PATH')
    initialize_database(db_path=db_path)
    parser = Project_Parser(project_folder=bb_project_folder) 
    song_list = parser.run()
    # example only. The database is initialized with data up to October 2024
    insert_song_data(db_path=db_path, data=song_list)
 

if __name__ == '__main__':
    main()
```

