import random
import nltk

BOT_CONFIG = {
    'intents': {
        'hello': {
            'examples': ['Привет!', 'Хай', 'Хэллоу'],
            'responces': ['Здравствуйте!', 'Прив', 'Доброго дня']
        },
        'bye': {
            'examples': ['Пока', 'Увидимся', 'До свиданья'],
            'responces': ['Приходите еще', 'Рад был познакомиться', 'Покеда']
        },
        'howdoyoudo': {
            'examples': ['Как жизнь?', 'Что делаешь?', 'Чем живешь?'],
            'responces': ['Пайдёт', 'Не жалуюсь', 'А кому сейчас легко?']
         },
        'R U A BOT': {
            'examples': ['Ты бот?', 'Ты робот?', 'Ты нейросеть?'],
            'responces': ['Вы очень проницательны!', 'А что?;)', 'Давайте без дискриминации)']
             },
        'WhomadeU': {
            'examples': ['Кто тебя писал?', 'Кто автор?', 'Аффтар?'],
            'responces': ['Начинающий программист!А что?', 'Хороший человек!)', 'Он старался!']


        }
    }
}
def clean(text):
  output_text = ''
  for char in text.lower():
    if char in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
      output_text = output_text + char
  return output_text

def get_intent(text):
  for intent in BOT_CONFIG['intents'].keys():
    for example in BOT_CONFIG['intents'][intent]['examples']:
      text1 = clean(example)
      text2 = clean(text)
      if len(text1) != 0 and len(text2) != 0:
def bot(input_text):
  intent = get_intent(input_text)
  if intent != 'Не удалось определить интент':
    return random.choice(BOT_CONFIG['intents'][intent]['responces'])
  else:
    return 'Извините, я ничего не понял. Я просто глупый бот.'

input_text = ''
while input_text != 'Завершить работу':
  input_text = input()
  print(bot(input_text))
