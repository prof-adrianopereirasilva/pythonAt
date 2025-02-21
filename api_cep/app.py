import requests

lista_ceps: list = ['18120020', '18087809', '06519400']
lista_enderecos: list = []

for cep in lista_ceps:
    url: str = f'https://viacep.com.br/ws/{cep}/json/'

    try:
        req = requests.get(url, timeout=3)
        req.raise_for_status()  # Garantir que a resposta seja OK (status 200)

        # API acessada com sucesso!
        endereco = req.json()

        # Verificando se os campos existem na resposta antes de tentar acessá-los
        lista_enderecos.append([
            endereco.get('cep', 'N/A'),
            endereco.get('logradouro', 'N/A'),
            endereco.get('complemento', 'N/A'),
            endereco.get('bairro', 'N/A'),
            endereco.get('localidade', 'N/A'),
            endereco.get('uf', 'N/A')
        ])

    except requests.exceptions.RequestException as e:
        print(f'Ocorreu um erro ao acessar a API para o CEP {cep}: {e}')

    except Exception as e:
        print(f'Ocorreu um erro inesperado: {e}')

# Imprimir os resultados obtidos
for item in lista_enderecos:
    print(item)
