import requests

pokemon_number = input("Digite o número do Pokémon: ")

url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_number}"

response = requests.get(url)

if response.status_code == 200:
    pokemon_data = response.json()
    
    name = pokemon_data["name"]
    height = pokemon_data["height"]
    weight = pokemon_data["weight"]

    print(f"Nome: {name}")
    print(f"Altura: {height}")
    print(f"Peso: {weight}")
else:
    print(f"Erro na solicitação: {response.status_code}")
