"""
Development script # 1. DEPRECATED
"""
from pprint import pprint
from typing import List
from parsers.project_parser import Project_Parser
from tools.db_tools import fetch_all, insert
from tools.utils import get_combined_dict, write_csv_file
from tools.queries import insert_songs_query
from tools.constants import PROJECT_DB_PATH


def get_product_pbf_names():
    """
    Returns a dictionary with PBF names for the keys and product names for values.
    We need this info in order to add the actual product name to our database.    
    """
    db_path = PROJECT_DB_PATH
    query = """select pbf_name, product from packs_pbf_type where pbf_name IS NOT NULL;"""
    result = fetch_all(db_path=db_path, query=query)
    return get_combined_dict(result)


def get_song_count_for_all():
    """
    
    """
    from tasks import get_total_song_count
    return get_total_song_count()


def insert_song_data():
    project_folder = r"C:\Users\RC\Documents\BBWorkspace\GM_Mega_Pack_Project"
    parser = Project_Parser(project_folder=project_folder)  
    # Get a dictionary of {PBF name: product name}
    product_pbf_dict = get_product_pbf_names()    
    # get a list of lists like [PBF name, song name]  
    pbf_list: List = parser.run()
    # add product name to the end of each pbf list item
    for item in pbf_list:
        pbf_name: str = item[0]
        product_name = product_pbf_dict.get(pbf_name)
        item.append(product_name)
        pbf_type = "One Press Play" if pbf_name.endswith("_OPP") else "Song Sections"
        item.append(pbf_type)

    # write to csv
    # header = ["pbf_name", "song_name", "product_name"]
    # write_csv_file(r"D:\Python\scripts\rc\mega-pack-pbf-parser\mega-pack-pbf-parser\output\pbf_songs.csv", pbf_list, header=header)

    # insert into the db
    db_path = r"D:\Python\scripts\rc\mega-pack-pbf-parser\db\pbf.db"
    rows_inserted = insert(db_path=db_path, query=insert_songs_query, data=pbf_list)
    print(f"Inserted {rows_inserted} records...")


def main():
    get_song_count_for_all()

if __name__ == '__main__':
    main()