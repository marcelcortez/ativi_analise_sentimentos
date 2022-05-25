
from analise_sentimentos import AnaliseSentimentos
from googletrans import Translator

analise = AnaliseSentimentos()

msg = input('Digite um texto: ')

tradutor = Translator()
textoTraduzido = tradutor.translate(msg)
resultado = analise.avalia(textoTraduzido.text)
resultado = resultado['score']

if resultado < 0:
    print('Frase negativa')

elif resultado == 0:
    print('Frase neutra')

elif resultado > 0:
    print('Frase positiva')
