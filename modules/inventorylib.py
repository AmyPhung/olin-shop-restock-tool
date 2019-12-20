import pandas as pd
from gsheets import Sheets

class Inventory:
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename
        self.inventory = None
        self.selection = []
        self.update()

    def updateCSV(self):
        sheets = Sheets.from_files('keys/client_secrets.json', 'keys/storage.json')
        s = sheets.get(self.url)
        s.sheets[1].to_csv(self.filename, encoding='utf-8', dialect='excel')

    def update(self):
        self.updateCSV()
        self.inventory = pd.read_csv(self.filename)
