# mega-pack-pbf-parser
Parse the content (songs and PBFs) of a BB project w/Mega Pack and add that data to the project database. 
- To write the required html file install this package: bb-pbf-html-writer
- pip install bb-pbf-html-writer

## Warnings
- Verify that the "packs_pbf_type" table is up-to-date. Be certain that ALL products are included in this table (i.e. check for new product releases)
- BEFORE ANYTHING ELSE the full path to the project db must be set the first time you try to run the code. This is handled by the ConfigManager class. 

## ConfigManager
status: currently, I am not finished implementing a change in the way the project config files are handled. 
At this time, the path to the project database is not written to config.json inside the package so it is not available the next time the example code is written.
At this time, the path to the project database is not written to the 's internat config.json so it is not available the next time the example code is executed. See below for more details.

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

Note: I'm currently reworking the project instantiation process. Some values ("BONUS_PBF_FILES" and "OPP_PBF_FILES") are stored inside the package (config.json currently)but everything will then be writen to a LOCAL config.json file in the USER's HOME directory.
The package's config.json needs to be renamed as 'default_config.json'.
Suggested name for USER 'config.json': mega_pack_pbf_parser_config.json OR create a project folder in USER/HOME for the project and use 'config.json'

## Constants
The project uses several constants defined in a config.json file handled by ConfigManager
- PROJECT_DB_PATH  - path to the project's database
- BONUS_PBF_FILES - PBFs we don't want to include because they are essentialy duplicates
- OPP_PBF_FILES - PBFs with one press play songs

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
from mega_pack_pbf_parser import get_report_data, write_json

project_database = r"D:\Python\scripts\rc\mega_pack_pbf_parser\db\pbf.db"

def insert_song_data(data: List):
    """
    Inserts song data into the project database. Prints the number of rows inserted.    
    """
    query = insert_songs_query
    db_path = project_database
    row_count = insert(db_path=db_path, query=query, data=data)
    print(f"Inserted {row_count} rows into the database.")


def main():    
    bb_project_folder = r"C:\Users\RC\Documents\BBWorkspace\GM_Mega_Pack_Project"
    db_path = project_database
    initialize_database(db_path=db_path)
    parser = Project_Parser(project_folder=bb_project_folder) 
    song_list = parser.run()
     # insert data into the database but note that the database is initialized with data up to October 2024
    insert_song_data(song_list)
    # write report data as json for later use in html files
    output_file_path = r"some/path/to/data/bb_pbf_report_data.py"
    result = get_report_data()
    write_json(filepath=output_file_path, data=result)


if __name__ == '__main__':
    main()
```

