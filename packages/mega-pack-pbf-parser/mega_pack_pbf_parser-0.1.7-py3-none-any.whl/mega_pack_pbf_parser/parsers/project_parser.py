"""
2024-09-27

Notes:
First we read the config.csv file in the "SONGS" directory to get the PBF names and hash for each PBF file
- EXAMPLE LINE: "0B587BA5	1. Brazilian"        (this is raw PBF name before we remove the numbers)
Then parse each PBF folder. Be sure to reference the folder name (hash - see step 1) to get the actual PBF name.
- EXAMPLE LINE: "7CB9720D.BBS	1. Bossa Nova"   (this is the song name)
REGEX
Regex required to parse PBF and song names: r"^\d+\.\s(?P<name>[\w+\d+\s\-\/?\&\)\(]+)$" 
see: https://regex101.com/r/6sfkQs/1
"""
import csv
import re
from pathlib import Path
from typing import Dict, Generator, List

class Project_Parser:
    """
    Gets all song names from a Beat Buddy project folder.
    Requires full path to the top level of the BB project directory.
    run() method returns a dictionary of all PBF files with info on each song (PBF name, song name)
    """
    def __init__(self, project_folder: str) -> None:
        self.songs_folder = Path(project_folder).joinpath("SONGS")
        self.pbf_list = []

    def build_pbf_list(self, pbf_folders: List) -> None:
        """Builds a list of lsits containing the PBF name and song name for each PBF file in a project."""
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


    def run(self) -> List:
        """Manager method that runs the entire process.
        Returns a list of lists of strings like this [['PBF name', 'Song name']...]
        """        
        pbf_folders: list = self.get_pbf_folders_list()
        self.build_pbf_list(pbf_folders=pbf_folders)
        return self.pbf_list


def main():
    # pass the folder containing your BB project
    project_folder = r"C:\Users\RC\Documents\BBWorkspace\GM_Mega_Pack_Project"
    parser = Project_Parser(project_folder=project_folder)
    pbf_list = parser.run()


if __name__ == '__main__':
    main()