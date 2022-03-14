'''
Created on 
Course work: 
@author: raja
Source:
    
    https://stackoverflow.com/questions/36641755/kafka-python-retrieve-the-list-of-topics

    https://pypi.org/project/kafka-python/

    https://stackoverflow.com/questions/40059654/python-convert-a-bytes-array-into-json-format

    https://www.easytweaks.com/add-rows-list-dict-pandas-dataframes/

pip:
    pip install kafka-python
    
'''

# Import necessary modules
from kafka import KafkaConsumer
import random
import json
import pandas as pd

city_id_dict = {
    'Toronto'   : 1,
    'Montreal'  : 2,
    'Waterloo'  : 3
}

paydayloan_dict = {            
    'cityid': [1],
    'paydayloan_count': [2]
}
# Build the Pandas DataFrame
paydayloan_df = pd.DataFrame(paydayloan_dict)

def collect_data(cityname):

    global paydayloan_df

    # collect data by city and store data
    city_id = city_id_dict[cityname]

    # dump them into CSV
    r_number = random.randint(100, 200)

    # print(city_id, r_number)

    new_dict = {'cityid': city_id, 'paydayloan_count': r_number}
    paydayloan_df = paydayloan_df.append(new_dict, ignore_index = True)

    print(f"adding : {new_dict}")

    paydayloan_df.to_csv('paydayloan.csv')

    pass

def startpy():
    
    # consumer = KafkaConsumer('ttwo')
    consumer = KafkaConsumer(
        "tone",
        bootstrap_server = '18.221.155.99:9092',

    )

    print(consumer)

    for msg in consumer:
        msg_value = msg.value
        
        print(msg_value)

        c_json = msg_value.decode('utf8').replace("'", '"')

        print(c_json)
        print(type(c_json))

        c_city_dict = json.loads(c_json)

        city = c_city_dict['city']

        collect_data(city)



if __name__ == '__main__':
    startpy()

'''
Sample:
ConsumerRecord(topic='tone', partition=0, offset=11, timestamp=1647230389976, timestamp_type=0, key=None, value=b'{"city" : "Toronto"}', headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=20, serialized_header_size=-1)
'''