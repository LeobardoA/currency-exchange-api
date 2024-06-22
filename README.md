# Currency Exchange API

## Descripción

Esta es una API de intercambio de divisas que permite consultar tasas de cambio y realizar intercambios entre diferentes divisas.

## Instalación

1. Clonar el repositorio:
   git clone <URL_DEL_REPOSITORIO>
   cd currency-exchange-api

2. Crear y activar un entorno virtual:
    python -m venv venv
    source venv/bin/activate

3. Instalar dependencias:
    pip install -r requirements.txt

USO:

1. Ejecutar la aplicacion:
    uvicorn run:app --reload

2. La API estará disponible en http://127.0.0.1:8000

DOCKERIZACION

1. Construir la imagen Docker:
    docker build -t currency-exchange-api .

2. Ejecutar el contenedor:
    docker run -p 8000:8000 currency-exchange-api

ENDPOINTS
    POST /exchange-rate: Consulta la tasa de cambio.
    POST /exchange: Realiza un intercambio de divisas.

PRUEBAS

1. Ejecutar las pruebas unitarias:
    pytest
2. Tambien se pueden hacer pruebas manuales usando postman o cmd
    Las pruebas que yo hice desde uvicorn fueron:
Invoke-RestMethod -Uri "http://127.0.0.1:8000/exchange" -Method Post -ContentType "application/json" -Body '{"base_currency": "EUR", "quote_currency": "USD", "amount": 150}'
3. Y una prueba que hice desde docker fue:
    curl -X POST "http://127.0.0.1:8000/exchange-rate" -H "Content-Type: application/json" -d '{"base_currency": "USD", "quote_currency": "EUR"}'             


DECISIONES DE DISEÑO
Realice un ultimo test, ademas del test necesario para probar el tipo de cambio de divisas y el intercambio de estas
creé un ultimo test para poder visualizar el registro de las comisiones cobradas
