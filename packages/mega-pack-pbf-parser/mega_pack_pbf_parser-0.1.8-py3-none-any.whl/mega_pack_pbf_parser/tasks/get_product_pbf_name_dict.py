from typing import Dict
from .. tools.db_tools import fetch_all
from .. tools.utils import get_combined_dict


def get_product_pbf_name_dict(db_path: str, query: str) -> Dict[str, str]:
    """
    Returns a dictionary with PBF names for the keys and product names for values.
    We need this info in order to add the actual product name to our database. 
    Example: {'GM_Blues_OPP': 'Blues', 'GM_Blues_Rock': 'Blues Rock',...}   
    """ 
    result = fetch_all(db_path=db_path, query=query)
    return get_combined_dict(result)


def main():
    print(get_product_pbf_name_dict())


if __name__ == '__main__':
    main()