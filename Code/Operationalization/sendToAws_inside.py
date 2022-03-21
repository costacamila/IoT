from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder
from csv import reader
from time import sleep
import json

url_inside = '../../Data/Processed/inside.csv'

ENDPOINT = "endpoint do aws"
CLIENT_ID = "nome da thing"
# PASTA DOS ARQUIVOS AWS DEVEM ESTAR NA PASTA DO PROJETO
PATH_TO_CERTIFICATE = "certificates/certificado_aws"
# PASTA DOS ARQUIVOS AWS DEVEM ESTAR NA PASTA DO PROJETO
PATH_TO_PRIVATE_KEY = "certificates/chave_aws"
# PASTA DOS ARQUIVOS AWS DEVEM ESTAR NA PASTA DO PROJETO
PATH_TO_AMAZON_ROOT_CA_1 = "certificates/root-CA.crt"

TOPIC = "thing/dado_desejado"


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

    return connect_future


def read_cvs():
    with open(url_inside, 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        if header != None:
            for row in csv_reader:
                print(int(row[3]))
                content = int(row[3])
                sleep(1)
                return content
        return 'Erro'


if __name__ == "__main__":
    while True:
        mqtt_connection = connect_to_aws()
        content = read_cvs()
        message = {"topic": content}
        mqtt_connection.publish(topic=TOPIC,
                                payload=json.dumps(message),
                                qos=1)
        disconnect_future = mqtt_connection.disconnect()
        disconnect_future.result
