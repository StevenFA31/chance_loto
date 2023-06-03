import requests
import pandas as pd
import matplotlib.pyplot as plt

def retrieve_loto_results(year):
    # Effectuer la requête HTTP pour récupérer les résultats du LOTO pour l'année donnée
    url = f"https://api-loto-foot.herokuapp.com/results/{year}"
    response = requests.get(url)
    data = response.json()
    return data

def calculate_average_draw(results):
    # Calculer la moyenne des boules et du numéro chance pour tous les tirages
    total_draws = len(results)
    total_balls = sum(draw['boule_1'] + draw['boule_2'] + draw['boule_3'] + draw['boule_4'] + draw['boule_5']
                      + draw['numero_chance'] for draw in results)
    average_balls = total_balls / (total_draws * 6)
    return average_balls

def get_top_10_balls(results):
    # Compter le nombre d'occurrences de chaque boule et sélectionner les 10 boules les plus fréquentes
    balls_counts = {}
    for draw in results:
        for ball in range(1, 6):
            balls_counts[draw[f'boule_{ball}']] = balls_counts.get(draw[f'boule_{ball}'], 0) + 1
    top_10_balls = sorted(balls_counts, key=balls_counts.get, reverse=True)[:10]
    return top_10_balls

def get_bottom_10_balls(results):
    # Compter le nombre d'occurrences de chaque boule et sélectionner les 10 boules les moins fréquentes
    balls_counts = {}
    for draw in results:
        for ball in range(1, 6):
            balls_counts[draw[f'boule_{ball}']] = balls_counts.get(draw[f'boule_{ball}'], 0) + 1
    bottom_10_balls = sorted(balls_counts, key=balls_counts.get)[:10]
    return bottom_10_balls

def visualize_ball_frequencies(balls_counts):
    # Visualiser les fréquences des boules sous forme de graphique
    balls = list(balls_counts.keys())
    frequencies = list(balls_counts.values())

    plt.bar(balls, frequencies)
    plt.xlabel('Boules')
    plt.ylabel('Fréquence')
    plt.title('Fréquence des boules dans les tirages du LOTO')
    plt.xticks(rotation=45)
    plt.show()

# Exemple d'utilisation
year = 2023

# Récupérer les résultats du LOTO pour l'année donnée
results = retrieve_loto_results(year)

# Calculer la moyenne d'un tirage sur l'année
average_balls = calculate_average_draw(results)
print(f"Moyenne des boules pour l'année {year} : {average_balls:.2f}")

# Obtenir les 10 boules les plus fréquentes
top_10_balls = get_top_10_balls(results)
print(f"Les 10 boules les plus fréquentes pour l'année {year} : {top_10_balls}")

# Obtenir les 10 boules les moins fréquentes
bottom_10_balls = get_bottom_10_balls(results)
print(f"Les 10 boules les moins fréquentes pour l'année {year} : {bottom_10_balls}")

# Visualiser les fréquences des boules (optionnel)
balls_counts = {ball: balls_counts[ball] for ball in top_10_balls}
visualize_ball_frequencies(balls_counts)
