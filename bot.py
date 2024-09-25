import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Substitua 'YOUR_API_KEY' pelo token do seu bot
bot = telebot.TeleBot('8075987584:AAGXtvS5MDEmEJcZYoQocVBFcudF5OeTF3M')

# Dicionários para armazenar as perguntas e respostas
quizzes = {
    "filmes": [
        {"pergunta": "Qual filme ganhou o Oscar de Melhor Filme em 2020?", "opcoes": ["Parasita", "1917", "Coringa", "Era Uma Vez em... Hollywood"], "correta": 0, "gif": "https://media.giphy.com/media/g01FakEbcUua6yM34a/giphy.gif?cid=790b76110dlh4q3iouwykrchrj5xfraodhkue0tev7onkbkh&ep=v1_gifs_search&rid=giphy.gif&ct=g"},
        {"pergunta": "Quem dirigiu o filme 'Titanic'?", "opcoes": ["James Cameron", "Steven Spielberg", "Christopher Nolan", "Quentin Tarantino"], "correta": 0, "gif": "https://media.giphy.com/media/FoH28ucxZFJZu/giphy.gif?cid=790b76113hwdkm7trdnoq57ybdckj06h9zw1x9moh5db31d3&ep=v1_gifs_search&rid=giphy.gif&ct=g"},
        {"pergunta": "Qual ator interpretou o Coringa no filme 'O Cavaleiro das Trevas'?", "opcoes": ["Heath Ledger", "Joaquin Phoenix", "Jack Nicholson", "Jared Leto"], "correta": 0, "gif": "https://media.giphy.com/media/mcOP7zqlraM24/giphy.gif?cid=ecf05e474nuj1ep4ixhsu2ibb3jrbd8ivhf5hmcb00henlsq&ep=v1_gifs_search&rid=giphy.gif&ct=g"},
        {"pergunta": "Em qual filme Tom Hanks interpreta um sobrevivente em uma ilha deserta?", "opcoes": ["O Resgate do Soldado Ryan", "Forrest Gump", "Náufrago", "Apollo 13"], "correta": 2, "gif": "https://media.giphy.com/media/jvJtAbu54HCpi/giphy.gif?cid=ecf05e47enn69jqkp97qsxvrk32othctajb3b33kymrrvpwh&ep=v1_gifs_search&rid=giphy.gif&ct=g"},
        {"pergunta": "Qual é o nome do primeiro filme da saga 'Star Wars'?", "opcoes": ["O Império Contra-Ataca", "O Retorno de Jedi", "A Ameaça Fantasma", "Uma Nova Esperança"], "correta": 3, "gif": "https://media.giphy.com/media/8McNH1aXZnVyE/giphy.gif?cid=790b7611udoqm8w2lcv2ubpm0pinzueneos2gh7vvqu6ee6c&ep=v1_gifs_search&rid=giphy.gif&ct=g"},
        {"pergunta": "Qual filme de 1994 tem como tema principal o encarceramento?", "opcoes": ["Pulp Fiction", "Forrest Gump", "Um Sonho de Liberdade", "O Rei Leão"], "correta": 2, "gif": "https://media.giphy.com/media/P2xf5nPyu5WP6/giphy.gif?cid=790b76119asq6tqgr5okochgi6wvwawvgi625omgfy23iuh7&ep=v1_gifs_search&rid=giphy.gif&ct=g"},
        {"pergunta": "Quem interpretou o Homem de Ferro no Universo Cinematográfico da Marvel?", "opcoes": ["Robert Downey Jr.", "Chris Evans", "Mark Ruffalo", "Chris Hemsworth"], "correta": 0, "gif": "https://media.giphy.com/media/PJsCSxZijckyA/giphy.gif?cid=ecf05e47ytxhwn06kvn1gen9u7y8y1u7n64305p5xjnp1h12&ep=v1_gifs_search&rid=giphy.gif&ct=g"},
        {"pergunta": "Qual filme de animação apresenta uma família de super-heróis?", "opcoes": ["Toy Story", "Procurando Nemo", "Os Incríveis", "Monstros S.A."], "correta": 2, "gif": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOTJqazBpdWNtd2d3bzd1cjhhNDA3MWY4bTN3eHRpZWZmd3JhbXd3ZyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/wH95uuWew8Q2mKqU7i/giphy.gif"},
        {"pergunta": "Qual filme é famoso pela frase 'Say hello to my little friend'?", "opcoes": ["O Poderoso Chefão", "Scarface", "Os Bons Companheiros", "Cassino"], "correta": 1, "gif": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExa21uMXliOGpoeGY1czNzajRhdDB4bXp0ZDMyM3RwMTExaG01eWhsayZlcD12MV9naWZzX3NlYXJjaCZjdD1n/CCQ89YgZJXB9WlK9PB/giphy.gif"},
        {"pergunta": "Quem dirigiu o filme 'Clube da Luta'?", "opcoes": ["David Fincher", "Martin Scorsese", "Stanley Kubrick", "Francis Ford Coppola"], "correta": 0, "gif": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZm56eWdqbWE0OW1oZWtwZXF5NTJpeG5mbnV3Z3hpZjVwZGh5endiYiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/OSb7004kul1FZHqxf6/giphy.gif"}
    ],
    "series": [
        {"pergunta": "Qual série tem o personagem Walter White?", "opcoes": ["Breaking Bad", "The Crown", "Game of Thrones", "Stranger Things"], "correta": 0, "gif": "https://media.giphy.com/media/3oz8xLwV2p3UzQ6wqY/giphy.gif"},
        {"pergunta": "Em qual série os personagens tentam sobreviver em um apocalipse zumbi?", "opcoes": ["The Walking Dead", "Westworld", "Lost", "Breaking Bad"], "correta": 0, "gif": "https://media.giphy.com/media/26AHG5KGFxSkUWw1i/giphy.gif"},
        {"pergunta": "Qual série é baseada nos livros de George R.R. Martin?", "opcoes": ["The Witcher", "Game of Thrones", "Vikings", "The Mandalorian"], "correta": 1, "gif": "https://media.giphy.com/media/xT9IgDEI1iZyb2wqoM/giphy.gif"},
        {"pergunta": "Qual série segue a vida de um grupo de amigos em Nova York?", "opcoes": ["Friends", "How I Met Your Mother", "Parks and Recreation", "The Office"], "correta": 0, "gif": "https://media.giphy.com/media/26ufm6sJSoIo1UySk/giphy.gif"},
        {"pergunta": "Qual série tem como protagonista um hacker chamado Elliot?", "opcoes": ["The 100", "Black Mirror", "Mr. Robot", "House of Cards"], "correta": 2, "gif": "https://media.giphy.com/media/xUA7b6LvnID1rgqfCE/giphy.gif"},
        {"pergunta": "Em qual série vemos as aventuras de uma criança com poderes psíquicos chamada Eleven?", "opcoes": ["Sense8", "Stranger Things", "Dark", "The OA"], "correta": 1, "gif": "https://media.giphy.com/media/l0HlwBO2AhKgAGVza/giphy.gif"},
        {"pergunta": "Qual série de ficção científica é conhecida pela frase 'Resistance is futile'?", "opcoes": ["Doctor Who", "Star Trek", "Battlestar Galactica", "The Expanse"], "correta": 1, "gif": "https://media.giphy.com/media/3ohzdPVfQ2pCNfEyFq/giphy.gif"},
        {"pergunta": "Qual série apresenta a história de um empresário de sucesso que vive uma vida dupla como vigilante?", "opcoes": ["Suits", "Narcos", "Dexter", "Better Call Saul"], "correta": 2, "gif": "https://media.giphy.com/media/l3q2yI9u7pIYmBRaQ/giphy.gif"},
        {"pergunta": "Qual série é ambientada em um mundo fictício medieval chamado Westeros?", "opcoes": ["Merlin", "Game of Thrones", "The Witcher", "Shadow and Bone"], "correta": 1, "gif": "https://media.giphy.com/media/xT5LMDitHo8dSb1yxm/giphy.gif"},
        {"pergunta": "Em qual série os detetives Jake Peralta e Rosa Diaz resolvem crimes em Nova York?", "opcoes": ["NCIS", "Law & Order", "The Mentalist", "Brooklyn Nine-Nine"], "correta": 3, "gif": "https://media.giphy.com/media/3ohhwIMtzfLqvzpUuk/giphy.gif"}
    ]
}

# Dicionário para armazenar a pontuação dos usuários
user_scores = {}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Olá! Escolha um tema para o quiz:")

    # Cria o menu com botões inline
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Filmes", callback_data="quiz_filmes"),
               InlineKeyboardButton("Séries", callback_data="quiz_series"))

    bot.send_message(message.chat.id, "Escolha uma categoria:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("quiz_"))
def callback_query(call):
    category = call.data.split("_")[1]
    user_scores[call.from_user.id] = {"categoria": category, "pontuacao": 0, "pergunta_atual": 0}
    enviar_pergunta(call.message, call.from_user.id)

def enviar_pergunta(message, user_id):
    categoria = user_scores[user_id]["categoria"]
    pergunta_atual = user_scores[user_id]["pergunta_atual"]
    pergunta = quizzes[categoria][pergunta_atual]

    # Envia o GIF (se houver)
    if "gif" in pergunta:
        bot.send_animation(message.chat.id, pergunta["gif"])

    # Envia a pergunta e opções de resposta
    markup = InlineKeyboardMarkup()
    for i, opcao in enumerate(pergunta["opcoes"]):
        markup.add(InlineKeyboardButton(opcao, callback_data=f"resposta_{i}"))

    bot.send_message(message.chat.id, pergunta["pergunta"], reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("resposta_"))
def verificar_resposta(call):
    user_id = call.from_user.id
    categoria = user_scores[user_id]["categoria"]
    pergunta_atual = user_scores[user_id]["pergunta_atual"]
    resposta_correta = quizzes[categoria][pergunta_atual]["correta"]
    resposta_usuario = int(call.data.split("_")[1])

    if resposta_usuario == resposta_correta:
        user_scores[user_id]["pontuacao"] += 1

    user_scores[user_id]["pergunta_atual"] += 1

    if user_scores[user_id]["pergunta_atual"] < len(quizzes[categoria]):
        enviar_pergunta(call.message, user_id)
    else:
        pontuacao_final = user_scores[user_id]["pontuacao"]
        bot.send_message(call.message.chat.id, f"Quiz finalizado! Sua pontuação: {pontuacao_final}/{len(quizzes[categoria])}")

bot.polling()
