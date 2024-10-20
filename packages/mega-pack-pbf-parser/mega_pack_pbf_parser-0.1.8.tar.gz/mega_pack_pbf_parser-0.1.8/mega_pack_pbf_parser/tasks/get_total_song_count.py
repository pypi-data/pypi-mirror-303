"""
Relies on the database path defined in tools/constants.py
"""
from tools.queries import get_total_song_count as song_count
from tools.db_tools import fetch_one
from tools.constants import BONUS_PBF_FILES, PROJECT_DB_PATH


def get_total_song_count() -> int:
    """
    Returns the total songs as an int for all PBF files EXCEPT the "bonus" PBF files for Ballads and Funk/HH/RB

    Note: you may have to update the query "get_total_song_count" if more bonus PBFs are added in the future.

    Warning: relies on the database path defined in tools/constants.py
    """
    result = fetch_one(db_path=PROJECT_DB_PATH, query=song_count, data=BONUS_PBF_FILES)    
    if not result:
        return 0
    return int(result[0])


