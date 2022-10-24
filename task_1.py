# Напишите программу, удаляющую из текста все слова, содержащие ""абв""
def delete_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

user_text = 'абвУ рек, известно, есть свои истоки \
и жизнь нам преподноситабв бесценные уроки:\
чтоб жить абвкрасиво, мудро и богато – \
заприте глубоко вабв подвал свои пороки.'

print(user_text)

new_text = delete_words(user_text)

print(new_text)
