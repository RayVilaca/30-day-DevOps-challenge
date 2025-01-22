# 30-day-DevOps-challenge

## Projeto

O projeto **Weather Dashboard** faz parte do desafio de 30 dias de DevOps. Este projeto tem como objetivo criar um painel que coleta dados meteorológicos de diferentes cidades e os armazena em um bucket S3 da AWS.

## Funcionalidades

- Criação de um bucket S3 para armazenar os dados meteorológicos.
- Coleta de dados meteorológicos de diferentes cidades usando a API OpenWeather.
- Armazenamento dos dados coletados no bucket S3 em formato JSON.

## Tecnologias Utilizadas

- Python
- Boto3 (AWS SDK para Python)
- Requests (para fazer requisições HTTP)
- Python-dotenv (para carregar variáveis de ambiente de um arquivo .env)

## Como Executar

1. Clone o repositório para sua máquina local.
2. Crie um arquivo `.env` na raiz do projeto e adicione suas chaves de API:
   ```env
   OPENWEATHER_API_KEY=your_openweather_api_key
   AWS_BUCKET_NAME=your_aws_bucket_name
   ```
3. Instale as dependências:
   ```sh
   pip install -r weather-dashboard/requirements.txt
   ```
4. Execute o script:
   ```sh
   python weather-dashboard/src/weather_dashboard.py
   ```

## Estrutura do Projeto

```
├── weather-dashboard/
│   ├── .env
│   ├── data/
│   ├── README.md
│   ├── requirements.txt
│   ├── src/
│   │   ├── **init**.py
│   │   └── weather_dashboard.py
│   ├── tests/
│   └── venv/
```

## Contribuição

Sinta-se à vontade para contribuir com o projeto. Para isso, faça um fork do repositório, crie uma branch para suas alterações e envie um pull request.
