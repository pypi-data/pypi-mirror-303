"""
Code for 


Regex required to parse PBF and song names: r"^\d+\.\s(?P<name>[\w+\d+\s\-\/?\&\)\(]+)$" 
see: https://regex101.com/r/6sfkQs/1
"""
import csv
import re
from pathlib import Path
from typing import Dict, Generator, List

from . import PROJECT_DB_PATH
from mega_pack_pbf_parser.db_tools import fetch_all
from mega_pack_pbf_parser.utils import get_combined_dict
from mega_pack_pbf_parser.queries import get_song_detail_query

class Project_Parser:
    """
    Gets all song names from a Beat Buddy project folder.
    Requires full path to the top level of the BB project directory.
    run() method returns a list of info on each song (PBF name, song name, product name, song type)
    """
    def __init__(self, project_folder: str) -> None:
        self.songs_folder = Path(project_folder).joinpath("SONGS")
        self.pbf_list = []

    def build_pbf_list(self, pbf_folders: List) -> None:
        """Builds a list of lists containing the PBF name and song name for each PBF file in a project."""
        for folder_name, pbf_name in pbf_folders:
            temp = []
            pbf_folder = self.songs_folder.joinpath(folder_name)
            rows = self.csv_config_reader(pbf_folder)
            for row in rows:
                cleaned_row = self.list_cleaner(row)
                temp.append([pbf_name, cleaned_row[1]])
            self.pbf_list.extend(temp)
            
    def list_cleaner(self, item: List, regex: str = r"^\d+\.\s(?P<name>[\w+\d+\s\-\/?\&\)\(]+)$"):
        """
        Retuns a list with the 2nd item cleaned up. Used for both PBF and song names.
        example input: ['0B587BA5', '1. Brazilian']
        example output: ['0B587BA5', 'Brazilian']
        """
        _regex = re.compile(regex)
        match = re.match(_regex, item[1])
        if match:
            item[1] = match.groupdict().get('name', 'regex issue in list_cleaner method!')
        else: 
            raise ValueError(f"This list could not be properly parsed: {item}")
        return item

    def csv_config_reader(self, folder_path: Path) -> Generator[List, None, None]:
        """Yields lines as dictionaries from a csv file."""
        with open(folder_path.joinpath("config.csv"), newline='') as f:
            reader = csv.reader(f)
            yield from reader

    def get_pbf_folders_list(self) -> List:
        """returns a list of lists with folder names and PBF names."""
        folders = []
        for row in self.csv_config_reader(self.songs_folder):            
            folders.append(self.list_cleaner(row))        
        return folders
    
    def get_product_pbf_name_dict(self, query: str) -> Dict[str, str]:
        """
        Returns a dictionary with PBF names for the keys and a list [product name, song type] for values.        
        """        
        result = fetch_all(db_path=PROJECT_DB_PATH, query=query)    
        return get_combined_dict(result)    
    
    def update_song_list(self, product_name_dict: Dict) -> List:
        """
        Adds the product name and song type to each item in self.song_list
        
        Parameters:
        product_name_dict (Dict): has PBF names for keys and lists as values. Example: pbf_name: [product name, song type]
        """
        for song in self.pbf_list:
            pbf_name = song[0]
            song.extend(product_name_dict.get(pbf_name))
                
    def run(self) -> List:
        """
        Manager method that runs the entire process.
        Returns a list of lists of strings with PBF name, song name, product name and song type
        """        
        pbf_folders: list = self.get_pbf_folders_list()
        self.build_pbf_list(pbf_folders=pbf_folders)
        product_name_dict = self.get_product_pbf_name_dict(query=get_song_detail_query)
        self.update_song_list(product_name_dict=product_name_dict)
        return self.pbf_list