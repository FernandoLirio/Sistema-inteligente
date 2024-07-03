import tkinter as tk
from tkinter import messagebox
import pandas as pd


data = {
    'title': [
        'Call of Duty', 'PUBG', 'Tetris', 'God of War', 'Tomb Raider', 'Black Desert', 'Dota', 'EA FC 24', 'Forza',
        'Game J', 'Minecraft', 'The Witcher 3', 'Fortnite', 'Valorant', 'League of Legends', 'Among Us', 'GTA V',
        'Cyberpunk 2077', 'Assassin\'s Creed Valhalla', 'FIFA 23', 'Mortal Kombat 11', 'Red Dead Redemption 2',
        'Overwatch', 'Hades',
        'Resident Evil Village', 'Apex Legends', 'Dark Souls III', 'Sekiro: Shadows Die Twice',
        'The Legend of Zelda: Breath of the Wild', 'Animal Crossing: New Horizons', 'Battlefield V', 'Stardew Valley',
        'Fall Guys', 'Horizon Zero Dawn',
        'Rocket League', 'Super Mario Odyssey', 'Dead by Daylight', 'Rainbow Six Siege', 'The Last of Us Part II',
        'Control'
    ],
    'genre': [
        'Ação', 'Ação', 'Quebra-cabeça', 'Ação', 'Aventura', 'Estratégia', 'RPG', 'Esportes', 'Corrida', 'Online',
        'Sandbox', 'RPG', 'Battle Royale', 'FPS', 'MOBA', 'Party', 'Ação', 'RPG', 'Aventura', 'Esportes',
        'Luta', 'Aventura', 'FPS', 'Roguelike', 'Terror', 'Battle Royale', 'RPG', 'Ação', 'Aventura', 'Simulação',
        'FPS', 'Simulação', 'Party', 'Aventura', 'Esportes', 'Plataforma', 'Terror', 'FPS', 'Ação', 'Aventura'
    ],
    'description': [
        'jogo de ação', 'ação e aventura', 'jogo de quebra-cabeça divertido', 'jogo de ação emocionante',
        'aventura e exploração', 'jogo estratégico', 'jogo de RPG', 'esportes competitivos',
        'corrida em alta velocidade', 'multijogador online', 'jogo de construção e exploração', 'jogo de RPG épico',
        'battle royale competitivo',
        'tiro em primeira pessoa', 'multijogador online battle arena', 'jogo de festa social', 'ação em mundo aberto',
        'jogo de RPG futurista',
        'aventura épica', 'simulação de futebol', 'jogo de luta', 'aventura no velho oeste', 'tiro em primeira pessoa',
        'roguelike hack and slash', 'jogo de terror e sobrevivência', 'battle royale de heróis', 'RPG desafiador',
        'ação e aventura no Japão feudal',
        'aventura em mundo aberto', 'simulação de vida', 'FPS militar', 'simulação de fazenda',
        'jogo de festa e competição', 'aventura futurista',
        'futebol com carros', 'plataforma 3D', 'terror e sobrevivência', 'tiro tático', 'ação pós-apocalíptica',
        'aventura sobrenatural'
    ]
}

# Cria um DataFrame do pandas a partir dos dados fornecidos
df = pd.DataFrame(data)


# Função para recomendar jogos com base nos gêneros selecionados
def recommend_games(selected_genres):
    # Filtra jogos que correspondem a qualquer um dos gêneros selecionados
    filtered_games = df[df['genre'].isin(selected_genres)]
    if filtered_games.empty:
        return None
    return filtered_games


# Função chamada ao clicar no botão de recomendar jogos
def recomendar_jogos():
    if selected_genres:
        # Chama a função de recomendação e obtém os jogos recomendados
        recommended_games = recommend_games(selected_genres)
        if recommended_games is not None:
            # Cria uma string de recomendações para exibir
            recomendacoes = "Jogos recomendados com base em suas preferências de gênero:\n"
            recomendacoes += '\n'.join(
                f"{row['title']} - {row['description']}" for _, row in recommended_games.iterrows())
        else:
            recomendacoes = "Não há jogos disponíveis para os gêneros selecionados."
    else:
        recomendacoes = "Por favor, selecione pelo menos um gênero para recomendar jogos."
    # Exibe a mensagem com as recomendações
    messagebox.showinfo("Recomendações", recomendacoes)


# Lista para rastrear os gêneros selecionados pelo usuário
selected_genres = []

# Índice do gênero atual que está sendo exibido
current_genre_index = 0

# Lista de todos os gêneros únicos disponíveis no DataFrame
all_genres = sorted(df['genre'].unique())


# Função para atualizar o rótulo do gênero atual
def update_genre_label():
    genre_label.config(text=f"Você gosta do gênero '{all_genres[current_genre_index]}'?")


# Função para avançar para o próximo gênero
def next_genre():
    global current_genre_index
    current_genre_index += 1
    if current_genre_index >= len(all_genres):
        # Se todos os gêneros foram revisados, exibe uma mensagem e mostra os gêneros selecionados
        messagebox.showinfo("Fim", "Você revisou todos os gêneros disponíveis.")
        genre_label.config(text="Gêneros selecionados:")
        next_button.pack_forget()
        yes_button.pack_forget()
        no_button.pack_forget()
        show_selected_genres()
        return
    # Atualiza o rótulo do gênero atual
    update_genre_label()


# Função chamada ao selecionar um gênero
def select_genre():
    selected_genres.append(all_genres[current_genre_index])
    next_genre()


# Função para exibir os gêneros selecionados
def show_selected_genres():
    selected_genres_label.config(text="Gêneros selecionados: " + ", ".join(selected_genres))
    recommend_button.pack(pady=20)


# Cria a janela principal
root = tk.Tk()
root.title("Recomendador de Jogos")

# Cria e exibe um rótulo para instruir o usuário
label = tk.Label(root, text="Selecione os gêneros de jogos que você gosta:")
label.pack(pady=10)

# Cria e exibe um rótulo para mostrar o gênero atual
genre_label = tk.Label(root, text="")
genre_label.pack(pady=10)

# Botões para selecionar e avançar entre os gêneros
yes_button = tk.Button(root, text="Sim", command=select_genre)
yes_button.pack(side=tk.LEFT, padx=10)

no_button = tk.Button(root, text="Não", command=next_genre)
no_button.pack(side=tk.RIGHT, padx=10)

# Botão para recomendar jogos, inicialmente oculto
recommend_button = tk.Button(root, text="Recomendar Jogos", command=recomendar_jogos)
recommend_button.pack_forget()

# Rótulo para mostrar os gêneros selecionados
selected_genres_label = tk.Label(root, text="")
selected_genres_label.pack(pady=10)

# Botão para avançar para o próximo gênero, inicialmente oculto
next_button = tk.Button(root, text="Avançar", command=next_genre)
next_button.pack_forget()

# Inicia o processo de seleção de gêneros exibindo o primeiro gênero
update_genre_label()

# Executa a janela principal do Tkinter
root.mainloop()
