# -*- coding: utf-8 -*-
"""curso datascience.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EJTvRleAVlwnOXxNbE63Udhq6CyVV4tC
"""

!pip install chatterbot
!pip install chatterbot_corpus

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('Pybot')
bot = ChatBot(
       'Pybot',
       storage_adapter='chatterbot.storage.SQLStorageAdapter',
       database_uri='sqlite:///database.sqlite3'
       )
conversa = ListTrainer(bot)
conversa.train([
                'Oi?',
                'Olá!',
                'Qual o seu nome?',
                'Pybot',
                'Prazer em te conhecer',
                'Igualmente!',
                'Tudo bem?',
                'Muito Bem, e você?',
                'Òtimo'
])
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.portuguese')

while True:
  resposta = bot.get_response(input("Usuário: "))
  if float(resposta.confidence) > 0.5:
    print("Pedro:", resposta)
  else:
      print("Desculpe, Eu não Entendi!")