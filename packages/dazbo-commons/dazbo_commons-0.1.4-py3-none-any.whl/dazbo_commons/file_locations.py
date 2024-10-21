""" 
Author: Darren
Date: 11/01/2022

Obtain a Locations class, which stores directory paths 
based on the location of a specified script. 
This makes it convenient to manage and access different file and directory paths 
relative to a given script's location.

To use in your code:
script_name = "my_script"
locations = get_locations(script_name)
"""
from dataclasses import dataclass
from pathlib import Path

@dataclass
class Locations:
    """ Dataclass for storing various location properties """
    script_name: str # The name of this script
    script_dir: Path # The path where this script is hosted
    input_dir: Path  # A directory called "input", under the script_dir
    output_dir: Path # A directory called "output", under the script_dir
    input_file: Path # A file called input.txt, under the script_dir

def get_locations(script_name="__file__", folder="") -> Locations:
    """ Set various paths, based on the location of the calling script. """
    
    script_dir = Path(Path().resolve(), folder, script_name)
    input_dir = Path(script_dir, "input")
    output_dir = Path(script_dir, "output")
    input_file = Path(input_dir, "input.txt")

    return Locations(script_name, script_dir,
                     input_dir,
                     output_dir,
                     input_file)
