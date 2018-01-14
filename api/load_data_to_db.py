import csv, sqlite3, os
from os import listdir
from os.path import isfile, join

DB_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/db.sqlite3'
FOLDER_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/data_dump"
csv_files = [f for f in listdir(FOLDER_PATH) if isfile(join(FOLDER_PATH, f))]

conn = sqlite3.connect(DB_PATH)
conn.text_factory = str
cur = conn.cursor()
curr_dict = {'btc': 'Bitcoin', 'doge': 'Dogecoin', 'eth': 'Ethereum', 'ltc': 'Litecoin'}
table_name = 'api_cryptocurrency'
for csv_file in csv_files:
    print('Inserting data from file: %s' % csv_file)
    csv_path = FOLDER_PATH + '/' + csv_file

    reader = csv.reader(open(csv_path, "rt"))
    currency_symbol = csv_file.split('.')[0].strip()
    currency_name = curr_dict[currency_symbol]
    counter = 0
    for i in reader:
        if counter != 0:
            cur.execute(
                'INSERT INTO ' + table_name + ' (date, txVolume, price, currency_symbol, currency_name) VALUES (?,?,?,?,?)',
                (i[0], i[1], i[4], currency_symbol, currency_name))
        else:
            counter = counter + 1

    print('Inserted from: %s' % csv_file)

conn.commit()
conn.close()
