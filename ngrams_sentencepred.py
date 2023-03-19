import nltk
from nltk.util import pad_sequence
from nltk.util import bigrams
from nltk.util import ngrams
from nltk.util import everygrams
from nltk.lm.preprocessing import pad_both_ends
from nltk.lm.preprocessing import flatten
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk.lm import MLE
from nltk.lm import Laplace
from nltk.tokenize.treebank import TreebankWordDetokenizer

def model_building(n, text):
    train_data, padded_sents = padded_everygram_pipeline(n, text)
    model=Laplace(1)
    model.fit(train_data, padded_sents)
    return model

def generate_sent(model, num_words, text_seed):
    """
    :param model: An ngram language model from `nltk.lm.model`.
    :param num_words: Max no. of words to generate.
    :param random_seed: Seed value for random.
    """
    detokenize = TreebankWordDetokenizer().detokenize
    content = []
    for token in model.generate(num_words,text_seed=text_seed):
        if token == '<s>':
            continue
        if token == '</s>':
            break
        content.append(token)
    return detokenize(content)

def model_eval(text,n, model):
    test_data, padded_sents = padded_everygram_pipeline(n, text)
    pep=[]
    for i, test in enumerate(test_data):
        pep.append(model.perplexity(test))
        #print("PP of sentence({0}):{1}".format(i,model.perplexity(test)))
    print('Average perplexity of the model is',round(sum(pep)/len(pep),2))
  
if __name__ == "__main__":
  n = 3
  text = [['I','need','to','book', 'ticket', 'to', 'Australia' ], ['I', 'want', 'to' ,'read', 'a' ,'book', 'of' ,'Shakespeare']]
  model=model_building(n, text)
  k=generate_sent(model, num_words=20,text_seed=['book'])
  model_eval(text,n,model)
  print(k)