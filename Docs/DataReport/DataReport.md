# Relatório de dados

## Dados brutos

| Dataset Name | Original Location | Destination Location | Data Movement Tools / Scripts | Link to Report  |
|--------------|-------------------|----------------------|-------------------------------|-----------------|
| IoTtemp    | Informações de temperatura durante o ano de 2018 de dentro e fora de uma sala | Dados que ajudaram a realizar a predição de temperatura | [IOT-temp.csv](/Data/Raw/IOT-temp.csv) | [Data Report](/Docs/DataReport/) |

- IOT-temp, leituras de temperatura com local e data.

## Dados Processados

| Processed Dataset Name | Input Dataset(s) | Data Movement Tools / Scripts | Link to Report  |
|------------------------|------------------|-------------------------------|-----------------|
| Inside | [inside.csv](/Data/Raw/IOT-temp.csv) | [dataPrep.ipynb](/Code/DataPrep/dataPrep.ipynb) | [Processed Dataset Report](/Docs/DataReport/) |
| Outside | [outside.csv](/Data/Raw/IOT-temp.csv) | [dataPrep.ipynb](/Code/DataPrep/dataPrep.ipynb) | [Processed Dataset Report](/Docs/DataReport/) |

- Inside, dados separados somente de dentro da sala.
- Outside, dados separados somente do lado de fora.

## Conjunto de recursos

| Feature Set Name | Input Dataset(s) | Data Movement Tools / Scripts | Link to Report  |
|------------------|------------------|-------------------------------|-----------------|
| dataPrep | [inside.csv](/Data/Raw/IOT-temp.csv) | [dataPrep.ipynb](/Code/DataPrep/dataPrep.ipynb) | [Processed Dataset Report](/Docs/DataReport/) |

- dataPrep, recebe o CSV completo de separa pelo local, dentro ou fora.