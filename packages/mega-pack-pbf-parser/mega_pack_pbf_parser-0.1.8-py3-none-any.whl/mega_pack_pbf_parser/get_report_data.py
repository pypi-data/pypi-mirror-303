"""
Generates the data needed for the BB PBF HTML Report
Functions:
get_report_data() - this is the primary function that creates the report data.
get_product_dict() - Returns a dictionary of PBF song info for one product.
get_songs_by_pbf_dict - Returns a list of product dictionaries with all songs for all PBFs.
write_json() - writes report data to a json file
2024-10-01
"""
import json
from pprint import pprint
from typing import Dict
from .db_tools import fetch_all, fetch_one
from . import PROJECT_DB_PATH, BONUS_PBF_FILES
from .queries import get_total_song_count, songs_per_pbf_query_no_bonus, song_names_query, songs_product_pbf_query

TITLE = 'Groove Monkee Mega Pack'
PAGE_HEADER = 'Mega Pack for Beat Buddy'
SONG_COUNT_HEADERS = ['Product', 'PBF name', 'Song Count']
PRODUCT_DETAILS_HEADER = 'Product Details'


def get_product_dict(product_name: str, results: list) -> Dict:
    """Returns a dictionary of PBF song info for one product."""
    result = {
            'name': None,
            'songs': None
        }
    
    result['name'] = product_name
    filtered = (result[1:] for result in results if result[0] == product_name)
    songs = [dict(pbf_name=pbf, song_name=song) for pbf, song in filtered]
    result['songs'] = songs
    return result


def get_songs_by_pbf_dict() -> Dict:
    """Returns a list of dictionaries. Each dictionary has two keys: 'name' and 'songs'. 
    'name' is the product name and 'songs' is a list of dictionaries.
    The 'songs' dictionaries have two keys each: 'pbf_name' and 'song_name'.
    """
    data = []
    results = fetch_all(db_path=PROJECT_DB_PATH, query=songs_product_pbf_query) 
    product_names = {result[0] for result in results}
    for pn in product_names:
        product_dict = get_product_dict(pn, results)
        data.append(product_dict)
    return data
    

def get_report_data():
    """
    Construct the dictionary needed to populate the HTML report template.
    Queries Needed
    - total song count (int) (get_total_song_count query)
    - song count by PBF (do not include 'bonus' PBF) (songs_per_pbf_query_no_bonus)
    - song names in each PBF with product name (song_names_query)

    Order of operations to construct the dictionary:
    'title': TITLE,
    'page_header': PAGE_HEADER,
    'total_songs': get_total_song_count,
    'song_count_headers': SONG_COUNT_HEADERS,
    'song_count_rows': songs_per_pbf_query_no_bonus,
    'product_details_header': PRODUCT_DETAILS_HEADER,
    'products': [{}, {}...]: 
    create using: song_names_query
    see: mega_pack_pbf_parser\docs\product_pbf_song_name.csv
    """
    data = {'title': TITLE, 
            'page_header': PAGE_HEADER, 
            'total_songs': 0,
            'song_count_headers': SONG_COUNT_HEADERS,
            'song_count_rows': None,
            'product_details_header': PRODUCT_DETAILS_HEADER,
            'products': None
    }
   
    total_songs, = fetch_one(db_path=PROJECT_DB_PATH, query=get_total_song_count, data=BONUS_PBF_FILES)
    data['total_songs'] = total_songs

    data['song_count_rows'] = fetch_all(db_path=PROJECT_DB_PATH, query=songs_per_pbf_query_no_bonus)
    products = get_songs_by_pbf_dict()
    data['products'] = sorted(products, key=lambda d: d['name'])
    return data


def write_json(filepath: str, data: Dict):
    """Writes a dictionary as json to specified filepath."""
    with open(filepath, 'w') as f:
        f.write(json.dumps(data, indent=4))
    

def main():
    """"""
    output_file_path = ""
    result = get_report_data()
    write_json(filepath=output_file_path, data=result)
    


if __name__ == '__main__':
    main()