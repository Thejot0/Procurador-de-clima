from projeto_clima import tratamento_api

class RespostaApi(tratamento_api.ApiClima):
    def resultado_api(self):
        for clima in self.resposta_json['forecast']['forecastday']:
            print(f'\nData: {clima['date']}\n'
                  f'Condição: {clima['day']['condition']['text']}\n'
                  f'Temp.maxima(C°): {clima['day']['maxtemp_c']}\n'
                  f'Temp.maxima(F°): {clima['day']['maxtemp_f']}\n'
                  f'Temp.minima(C°): {clima['day']['mintemp_c']}\n'
                  f'Temp.minima(F°): {clima['day']['mintemp_f']}')
            print()


if __name__ == "__main__":
    teste = RespostaApi()
    teste.procura_local()
    teste.clima()
    teste.resultado_api()