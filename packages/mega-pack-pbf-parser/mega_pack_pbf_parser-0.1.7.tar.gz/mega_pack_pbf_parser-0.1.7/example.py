"""
pip install -i https://test.pypi.org/simple/ mega-pack-pbf-parser
"""
from typing import List
from mega_pack_pbf_parser import Project_Parser
from mega_pack_pbf_parser import create_db, insert
from mega_pack_pbf_parser import insert_songs_query
from mega_pack_pbf_parser import initialize_database

project_database = r"D:\Python\scripts\rc\mega_pack_pbf_parser\db\pbf.db"


def insert_song_data(data: List):
    """
    Inserts song data into the project database. Prints the number of rows inserted.

    Parameters:
    data(List): a list of song info: PBF name, song name, product name, song type
    """
    query = insert_songs_query
    db_path = project_database
    row_count = insert(db_path=db_path, query=query, data=data)
    print(f"Inserted {row_count} rows into the database.")


def main():    
    bb_project_folder = r"C:\Users\RC\Documents\BBWorkspace\GM_Mega_Pack_Project"
    # db_path = project_database
    # initialize_database(db_path=db_path)
    # parser = Project_Parser(project_folder=bb_project_folder) 
    # song_list = parser.run()
    # # example only. The database is initialized with data up to October 2024
    # insert_song_data(song_list)
    # print(locals())
    print("-----")
    print(globals())


if __name__ == '__main__':
    main()
