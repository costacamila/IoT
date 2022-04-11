from multiprocessing import connection
from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder
from csv import reader
from time import sleep
import json
import random 
import numpy as np
import pandas as pd
import time

url_inside = '/app/Data/Processed/inside.csv'

ENDPOINT = "ar95nzm5vzl5q-ats.iot.us-east-1.amazonaws.com"
CLIENT_ID = "ar_condicionado"
# PASTA DOS ARQUIVOS AWS DEVEM ESTAR NA PASTA DO PROJETO
PATH_TO_CERTIFICATE = "/app/Code/Operationalization/certificates/ar_condicionado.cert.pem"
# PASTA DOS ARQUIVOS AWS DEVEM ESTAR NA PASTA DO PROJETO
PATH_TO_PRIVATE_KEY = "/app/Code/Operationalization/certificates/ar_condicionado.private.key"
# PASTA DOS ARQUIVOS AWS DEVEM ESTAR NA PASTA DO PROJETO
PATH_TO_AMAZON_ROOT_CA_1 = "/app/Code/Operationalization/certificates/root-CA-ar.crt"

TOPIC = "$aws/things/ar_condicionado/shadow/update"

df = pd.read_csv('Data/Processed/inside.csv')

def randomChoose(df):
    df = pd.DataFrame(df)
    return df.sample()
    

def DataAnalyse(dataframe):
    payload = {"state": {"desired": {"estado_ar": ""}}}
    x= dataframe['temp']
    
    if x > 27:
        payload['state']['desired']['estado_ar'] = "Ligar Ar."
        print("MAIOR QUE 27")
    else:
        payload['state']['desired']['estado_ar'] = "Desligar Ar"
        print("MENOR QUE 27")
        
    return payload 

if __name__ == "__main__":
    stop = True
    for i, row in df.iterrows():
        payload = DataAnalyse(row)
        time.sleep(1)
        event_loop_group = io.EventLoopGroup(1)
        host_resolver = io.DefaultHostResolver(event_loop_group)
        client_bootstrap = io.ClientBootstrap(event_loop_group,  host_resolver)
        mqtt_connection = mqtt_connection_builder.mtls_from_path(
            endpoint=ENDPOINT,
            cert_filepath=PATH_TO_CERTIFICATE,
            pri_key_filepath=PATH_TO_PRIVATE_KEY,
            ca_filepath=PATH_TO_AMAZON_ROOT_CA_1,
            client_bootstrap=client_bootstrap,
            client_id=CLIENT_ID,
            clean_session=False
        )
        connection_future = mqtt_connection.connect()
        connection_future.result()
        mqtt_connection.publish(topic=TOPIC, payload=json.dumps(payload), qos=mqtt.QoS.AT_LEAST_ONCE)
        disconnect_future = mqtt_connection.disconnect()
        disconnect_future.result()