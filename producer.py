'''
Created on 
Course work: 
@author: raja
Source:
    https://stackoverflow.com/questions/36641755/kafka-python-retrieve-the-list-of-topics

    https://pypi.org/project/kafka-python/

    https://pypi.org/project/confluent-kafka/

    https://flexiple.com/python-string-to-bytes/
    
'''

# Import necessary modules
from kafka import KafkaProducer
import time
import json

def startpy():

    city_list = [
        "Toronto",
        "Montreal",
        "Waterloo"
    ]
    
    producer = KafkaProducer(bootstrap_servers = '0.0.0.0:9092')

    for i in range(3):
        
        result_dict = {
            "city" : city_list[i]
        }
        json_dump = json.dumps(result_dict)

        print(type(json_dump))

        str_1_encoded = bytes(json_dump, 'UTF-8')

        producer.send('tone', str_1_encoded)

        time.sleep(5)

if __name__ == '__main__':
    startpy()