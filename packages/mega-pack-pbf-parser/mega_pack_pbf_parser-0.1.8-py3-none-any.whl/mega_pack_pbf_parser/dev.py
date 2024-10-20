"""

"""
from pprint import pprint
from typing import Dict
from parsers.project_parser import Project_Parser
from tools.constants import PROJECT_DB_PATH
from tools.db_tools import fetch_all
from tools.utils import get_combined_dict

#1 Parse Project folder


#2 Insert Data into database

def get_product_pbf_name_dict(db_path: str, query: str) -> Dict[str, str]:
    """
    Returns a dictionary with PBF names for the keys and product names for values.
    We need this info in order to add the actual product name to our database. 
    Example: {'GM_Blues_OPP': 'Blues', 'GM_Blues_Rock': 'Blues Rock',...}   
    """ 
    result = fetch_all(db_path=db_path, query=query)
    return get_combined_dict(result)



def main():
    project_folder = r"C:\Users\RC\Documents\BBWorkspace\GM_Mega_Pack_Project"
    parser = Project_Parser(project_folder=project_folder) 
    product_pbf_dict = get_product_pbf_name_dict()
    pprint(product_pbf_dict)

if __name__ == '__main__':
    main()
