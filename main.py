def get_text_from_url(filename):
    from urllib.request import urlopen
    import os.path
    extension = os.path.splitext(filename)[1]
    if extension != ".txt":
        print("Error: Please pass the .txt file.")
        exit()
    try:
        file = urlopen(filename)
        return file.read().decode("utf-8")
    except ValueError:
        try:
            file = open(filename)
            return file.read()
        except:
            print("Error: Could not find the file '" + filename +"'")
            exit()

# get text from url

# The Wonderful Wizard of Oz
text_wizard = get_text_from_url("https://www.gutenberg.org/files/55/55.txt") 

# Peter Pan
text_peter = get_text_from_url("https://www.gutenberg.org/files/16/16-0.txt") 

# count number of Dorothy and Peter
words_wizard = text_wizard.split()
words_peter = text_peter.split()
dorothy = "Dorothy"
peter = "Peter"

from collections import Counter
num_dorothy = Counter(words_wizard)[dorothy]
num_peter = Counter(words_peter)[peter]



import markovify

class SentencesByChar(markovify.Text):
    def word_split(self, sentence):
        return list(sentence)
    def word_join(self, words):
        return "".join(words)



# change to "word" for a word-level model
level = "char"
# controls the length of the n-gram
order = 10
# weights between the models; text A first, text B second.
# if you want to completely exclude one model, set its corresponding value to 0
weights = [0.5, 0.5]
# limit sentence output to this number of characters
length_limit = 500

model_cls = markovify.Text if level == "word" else SentencesByChar
gen_wizard = model_cls(text_wizard, state_size=order)
gen_peter = model_cls(text_peter, state_size=order)
gen_combo = markovify.combine([gen_wizard, gen_peter], weights)


sents_dorothy = set()
sents_peter = set()

while True:
    sent = gen_combo.make_short_sentence(length_limit, test_output=False).replace("\n", " ")
    if sent[:7] == dorothy:
        sents_dorothy.add(sent)
    elif sent[:5] == peter:
        sents_peter.add(sent)
    if len(sents_dorothy) >= 1 and len(sents_peter) >= 1:
        break


# print(sents_dorothy, sents_peter)

for sent_dorothy in sents_dorothy:
    print(sent_dorothy)

for sent_peter in sents_peter:
    print(sent_peter)
