meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "РОФЛ":  "шутка",
            "ЩИЩ":  "одобрение или восторг",
            "КРИПОВЫЙ":  "страшный, пугающий",
            "АГРИТЬСЯ":  "злиться",
            "sigma": "someone good",
            "skibidi" : "someone bad"
}
hehe = input('Введите непонятное слово (большими буквами!): ')
if hehe in meme_dict.keys():
    print(meme_dict[hehe])
else:
    print('non existant')
