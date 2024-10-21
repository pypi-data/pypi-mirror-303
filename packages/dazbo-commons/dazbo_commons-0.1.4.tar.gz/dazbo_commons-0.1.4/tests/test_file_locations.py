""" 
Test for file_locations.py.
Author: Darren
"""
from os import path
from pathlib import Path
import unittest
import dazbo_commons as dc

class TestFileLocations(unittest.TestCase):
    """ Tests that logging is emitted based on logging threshold, 
    and that it contains the right prefix text. """
    
    def setUp(self):
        self.script_name = "dazbo_commons"
        self.locations = dc.get_locations(self.script_name)

    def test_locations(self): 
        """ Test that the locations and script name are set properly """

        script_path = Path(__file__).resolve() # Full path of this test py
        
        # Assuming /dazbo_commons/tests/my_test.py -> /dazbo_commons
        parent_directory = script_path.parent.parent
        
        # Construct a script dir from parent + supplied script name
        # E.g. /dazbo-commons/dazbo-commons
        script_directory = parent_directory / self.script_name
        
        # use normcase to un-escape and ignore case differences in the paths
        self.assertEqual(path.normcase(self.locations.script_dir), 
                         path.normcase(str(script_directory)))
        
        self.assertEqual(self.locations.script_name, self.script_name)  
                    
if __name__ == '__main__':
    unittest.main()
