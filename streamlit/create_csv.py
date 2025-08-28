import csv

data = [
    ['category', 'sales'],
    ['A', 20], ['B', 60], ['C', 40], ['D', 90], ['E', 80],
    ['F', 50], ['G', 20], ['H', 90], ['I', 50]
]

with open('my_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)