
from typing import List

from mega_pack_pbf_parser.project_parser import Project_Parser


def parse_pbf_folder(project_folder: str) -> List[List[str]]:
    """    
    Parses a Beat Buddy project folder

    This function creates a list of song information: PBF name and song name.
     Hint: Pass the top-level folder of the Beat Buddy project
    
    Parameters:
    project_folder (str): the full path to the Beat Buddy project
  

    Returns:
    List: a list of lists of strings ike this [['PBF name', 'song name'],...]
    """
    # pass the folder containing your BB project  
    parser = Project_Parser(project_folder=project_folder)
    return parser.run()



def main():
    pass


if __name__ == '__main__':
    main()