import csv
from bird_tower import BirdTower


class CsvLoader:
    
    def __init__(self, csv_file_str):
        self.csv_file_str = csv_file_str
        
    def load(self):
        towers = list()
        csv_file = open(self.csv_file_str, 'r')
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            tower = BirdTower(row[0], float(row[1]), float(row[2]))
            towers.append(tower)
        csv_file.close()
        return towers
                 


