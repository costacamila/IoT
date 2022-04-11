# Charter do projeto

## Business background
- Para todos que desejam uma maior comodidade e conforto em controle de temperatura
- Ter um ambiente com uma temperatura mais agradável em dias quentes

## Escopo
- Criar um projeto que com base na temperatura externa que mantenha sempre uma temperatura agradável para um cômodo, por meio de sensores e ar-condicionado
- Para todos que queiram um espaço com uma temperatura mais amena de forma automatizada

## Pessoal
- Camila Costa
    - Data Scientist
    - Data Administrator
- Christian Tavares
    - Data Scientist
    - Data Administrator
- Juann Suassuna
    - Data Scientist
    - Data Administrator
- Thiago Rios
    - Data Scientist
    - Data Administrator
- Fernando 
    - Business contact

## Métricas
- Qual o objetivo qualitativo? Reduzir a temperatura do ambiente(ex: sala, escritório, etc.)
- Qual é a métrica quantificável? Reduzir a temperatura do ambiente em até 10 minutos
- Quais aprimoramentos podem ser feitos nos valores das métricas? Reduzir a temperatura do ambiente em até 10 minutos ou em um período de tempo que esteja relacionado com o
tamanho do ambiente x potência do ar-condicionado.

## Arquitetura
- Dados
    - 3 CSVs:
        - IoT-temp
        - inside
        - outside
- Tratativa
    - Recebemos o csv IoT-temp e separamos nos outros 2 arquivos
    - Enviamos ambos como leituras com data e temperatura
    - Armazenamos ambas no serviço AWS
    - Utilizamos os dados para realizarmos a predição
- Serviços e ferramentas
    - AWS para uso dos serviços de IoT
    - Prophet para a predição do projeto

## Comunicação
- A equipe se falava todos os dias, mas geralmente realizava reuniões semanais para tratar do projeto.
- Todos da equipe podiam se comunicar com o responsável do projeto(professor Fernando).
