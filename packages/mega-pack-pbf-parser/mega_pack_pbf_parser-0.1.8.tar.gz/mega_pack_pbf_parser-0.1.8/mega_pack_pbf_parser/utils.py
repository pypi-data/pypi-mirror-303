"""
Misc project utilities

Functions:
- get_combined_dict(results: List[Tuple]) -> Dict
- write_csv_file(filepath, data, header=None)
"""
from typing import Dict, Iterable, List, Tuple
import csv
import sqlite3
from pkg_resources import resource_filename

def get_combined_dict(results: List[Tuple]) -> Dict[str, str]:
    """Returns a dictionary from a list of 2 item tuples"""
    d = dict(sections='Song Sections', OPP='One Press Play') 
    pbf_dict = dict()
    for result in results:
        song_type = d.get(result[2])
        pbf_dict.update({result[0]: [result[1], song_type]})    
        
    return pbf_dict


def write_csv_file(filepath: str, data: Iterable, header=None):      
    """Writes an iterable to a csv file."""
    with open(filepath, 'w', newline='', encoding='utf8') as f:
        writer = csv.writer(f)
        if header:
            writer.writerow(header)
        writer.writerows(data)


def initialize_database(db_path: str):
    """
    Creates the project database using: create_database.sql file
    Relies on pkg_resources.resource_filename method to find the script.

    Args:
        db_path (str): full path to the database to create.
    """
    # Locate the SQL script within the package
    sql_script_path = resource_filename('mega_pack_pbf_parser', 'data/create_database.sql')

    with sqlite3.connect(db_path) as conn:
        with open(sql_script_path, 'r') as f:
            sql_script = f.read()
        conn.executescript(sql_script)

    print(f"Database initialized at {db_path}")
