"""
pip install -i https://test.pypi.org/simple/ mega-pack-pbf-parser
"""
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
