import pandas as pd
import numpy as np
from gsheets import Sheets

class Inventory:
    """Object representing inventory of toolbox. Can be updated by modifying
    origin gsheets and calling updateCSV function.

    Attributes:
        url (str): URL of gsheets
        filename (str):  File location for saving csv of inventory
        inventory (pandas dataframe): Pandas representation of inventory
        selection (list): List of items selected by user
    """
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename
        self.inventory = None
        self.selection = []
        self.update()

    def updateCSV(self):
        """Re-create inventory csv file by pulling new data in from gsheets"""

        sheets = Sheets.from_files('keys/client_secrets.json', 'keys/storage.json')
        s = sheets.get(self.url)
        s.sheets[1].to_csv(self.filename, encoding='utf-8', dialect='excel')

    def update(self):
        """Update inventory object by calling updateCSV() then updating pandas
        representation of inventory"""

        self.updateCSV()
        self.inventory = pd.read_csv(self.filename)

    def printOrder(self):
        """Returns a list containing each line of the McMaster order formatted
        as if it were a CSV
        (example output: ["92949A112,1.0", "92196A110,1.0"])"""

        part_numbers = self.getPartNumbers()
        quantity = np.ones(len(part_numbers)) # Defaults to 1 for all parts

        output = map(str, zip(part_numbers, quantity)) # Convert to string
        output = list(map(lambda x: x.strip('()'), output)) # Remove ( and )
        return output

    def getPartNumbers(self):
        """Returns a list of part numbers for a list of part names"""
        clean_inventory = self.inventory["Name"].apply(lambda x: x.strip())
        subset = self.inventory[clean_inventory.isin(self.selection)]
        part_numbers = subset["McMaster #"]
        return part_numbers
