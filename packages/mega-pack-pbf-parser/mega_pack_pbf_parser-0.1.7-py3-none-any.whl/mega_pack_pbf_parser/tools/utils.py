"""
Misc utilities
"""
from typing import Dict, Iterable, List, Tuple
import csv

def get_combined_dict(results: List[Tuple]) -> Dict[str, str]:
    """Returns a dictionary from a list of 2 item tuples"""  
    pbf_dict = dict()
    for result in results:
        pbf_dict.update({result[0]: result[1]})    
        
    return pbf_dict


def write_csv_file(filepath: str, data: Iterable, header=None):
    """Writes an iterable to a csv file."""
    with open(filepath, 'w', newline='', encoding='utf8') as f:
        writer = csv.writer(f)
        if header:
            writer.writerow(header)
        writer.writerows(data)