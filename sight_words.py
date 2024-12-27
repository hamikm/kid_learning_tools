import random
import os
import sys

words_top_100 = ['the','be','to','of','and','a','in','that','have','I','it','for','not','on','with','he','as','you','do','at','this','but','his','by','from','they','we','say','her','she','or','an','will','my','one','all','would','there','their','what','so','up','out','if','about','who','get','which','go','me','when','make','can','like','time','no','just','him','know','take','people','into','year','your','good','some','could','them','see','other','than','then','now','look','only','come','its','over','think','also','back','after','use','two','how','our','work','first','well','way','even','new','want','because','any','these','give','day','most','us']

session_len = 20
score = 0
wrong_words = []

print ('Welcome, Parker!!!!!!!!!!!!!!')
print()

words = random.sample(words_top_100, session_len)

for i in range(session_len):
    word = words[i]

    input(f'{i + 1} of {session_len}: say \"{word}\" then press return.')
    os.system(f'say \'{word}\' &')
    result = ''
    while result is not 'c' and result is not 'x':
        result = input('If you were correct, press c. If not, press x: ')
    if result is 'c':
        score += 1
    else:
        wrong_words.append(word)

    print()

score = 100 * score / session_len
print (f'Your score was {score} %')
if (score > 99):
    print ('WOW! Perfect!')
elif (score >= 90):
    print ('Good job!!!!! Almost perfect!')
elif (score >= 80):
    print ('Not bad, but review wrong words to get better.')
else:
    print('Review wrong words please.')

print('Wrong words: ', wrong_words)
