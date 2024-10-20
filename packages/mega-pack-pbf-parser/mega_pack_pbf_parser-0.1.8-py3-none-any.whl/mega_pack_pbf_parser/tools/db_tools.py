from pprint import pprint
import sqlite3
from contextlib import contextmanager
from typing import Dict, Iterable, List, Tuple

from tools.constants import PROJECT_DB_PATH
from tools.queries import song_count_by_product

def dict_factory(cursor, row):
    """A SQLite3 Row factory that returns a dictionary"""
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}


@contextmanager
def get_connection(db_path: str, row_factory=False):
    """Returns a sqlite3 connection."""
    try:
        conn = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        if row_factory:
            conn.row_factory = dict_factory         
        yield conn
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.commit()
        conn.close()


def fetch_all(db_path: str, query: str, data: Iterable=tuple()) -> list:
    """Returns a list of query results"""
    with get_connection(db_path=db_path, row_factory=None) as conn:
        return conn.execute(query, data).fetchall()
    
def fetch_one(db_path: str, query: str, data: Iterable=tuple()) -> tuple:
    """
    Returns one result as a tuple
    """
    with get_connection(db_path=db_path, row_factory=None) as conn:
        result = conn.execute(query, data).fetchone()
        return result
    
def insert(db_path: str, query: str, data: Iterable[Iterable]) -> int:
    """
    Insert data into the specified database and return the number of records added.
    WARNING: You must pass an interable of iterables, not a single iterable.
    """
    with get_connection(db_path=db_path, row_factory=None) as conn:
        cursor = conn.executemany(query, data)
        return cursor.rowcount

    
def main(): 
    db_path = PROJECT_DB_PATH 
    data = [['GM_Ballads','068 Money Stick Brushes','Ballads']]
    query = """INSERT INTO songs (pbf_name, song_name, product_name) VALUES(?,?,?);"""
    records_inserted = insert(db_path=db_path, query=query, data=data)
    print(records_inserted)
    

if __name__ == '__main__':
    main()