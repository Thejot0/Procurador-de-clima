import os
from projeto_clima import uteis
import requests
import json
from dotenv import load_dotenv
from projeto_clima import entrada

class ApiLocal:

    def procura_local(self):
        self.local = entrada.digitar_local()
        load_dotenv()
        chave = os.getenv("chave_local")

        self.url = f"http://api.geonames.org/postalCodeSearchJSON?placename={self.local}&maxRows=1&username={chave}"

        resposta = requests.get(self.url, timeout=10)
        resposta.raise_for_status()
        resposta_json = resposta.json()

        with open ("api_local.json", 'w', encoding='utf-8') as local:
            json.dump(resposta_json, local, indent=4, ensure_ascii=False)

        for local in resposta_json["postalCodes"]:
            uteis.linha()
            print(
                f'Local: {local["adminName2"]}\n'
                  f'Estado: {local["adminName1"]}\n'
                  f'País: {local["countryCode"]}'
                  )
            uteis.linha()

class ApiClima(ApiLocal):

    def clima(self):
        # try:
        load_dotenv()
        chave = os.getenv("chave_clima")

        dias = entrada.quantidade_dias()

        url = f"http://api.weatherapi.com/v1/forecast.json?key={chave}&q={self.local}&days={dias}&lang=pt"

        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        self.resposta_json = resposta.json()

        with open('clima.json', 'w', encoding='utf-8') as clima:
            json.dump(self.resposta_json, clima, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    teste = ApiClima()
    teste.procura_local()
    teste.clima()