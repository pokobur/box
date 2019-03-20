import pathlib as pa
import pprint


basket = []


def master_data():
    y_file = pa.Path('yasai.txt')
    with y_file.open(mode='r', encoding='utf-8') as yasai:
        for line in yasai:
            if line.strip().endswith('ン'):
                continue
            basket.append(line.strip())
          #  print(line)
        print(len(basket))
# master_data()