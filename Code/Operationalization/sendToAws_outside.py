from multiprocessing import connection
from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder
from csv import reader
from time import sleep
import json

url_outside = '/app/Data/Processed/outside.csv'

ENDPOINT = "ar95nzm5vzl5q-ats.iot.us-east-1.amazonaws.com"
CLIENT_ID = "Sensor_outside"
# PASTA DOS ARQUIVOS AWS DEVEM ESTAR NA PASTA DO PROJETO
PATH_TO_CERTIFICATE = "/app/Code/Operationalization/certificates/Sensor_outside.cert.pem"
# PASTA DOS ARQUIVOS AWS DEVEM ESTAR NA PASTA DO PROJETO
PATH_TO_PRIVATE_KEY = "/app/Code/Operationalization/certificates/Sensor_outside.private.key"
# PASTA DOS ARQUIVOS AWS DEVEM ESTAR NA PASTA DO PROJETO
PATH_TO_AMAZON_ROOT_CA_1 = "/app/Code/Operationalization/certificates/root-CA-outside.crt"

TOPIC = "Sensor_outside/temperature"


def connect_to_aws():
    event_loop_group = io.EventLoopGroup(1)
    host_resolver = io.DefaultHostResolver(event_loop_group)
    client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
    mqtt_connection = mqtt_connection_builder.mtls_from_path(
        endpoint=ENDPOINT,
        cert_filepath=PATH_TO_CERTIFICATE,
        pri_key_filepath=PATH_TO_PRIVATE_KEY,
        client_bootstrap=client_bootstrap,
        ca_filepath=PATH_TO_AMAZON_ROOT_CA_1,
        client_id=CLIENT_ID,
        clean_session=False,
        keep_alive_secs=6
    )
    connect_future = mqtt_connection.connect()
    connect_future.result()
    return mqtt_connection, connect_future


if __name__ == "__main__":
    mqtt_connection, connection = connect_to_aws()
    with open(url_outside, 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        if header != None:
            for row in csv_reader:
                print(int(row[3]))
                content_date = row[0]
                content_temp = int(row[3])
                message = {
                    "noted_date": content_date,
                    "temperature_outside": content_temp
                }
                mqtt_connection.publish(topic=TOPIC,
                                        payload=json.dumps(message),
                                        qos=mqtt.QoS.AT_LEAST_ONCE)
                sleep(.1)
    disconnect_future = mqtt_connection.disconnect()
    disconnect_future.result
