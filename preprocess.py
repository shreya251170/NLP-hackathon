import re
from nltk.tokenize import  RegexpTokenizer
import nltk
nltk.download('punkt')
nltk.download('stopwords')

def preprocess(text):
    txt=text.replace('Human 1','')
    txt=txt.replace('Human 2','')
    txt= re.sub('\d+','',txt)
    txt = re.sub(r'\n{2,}|^\n', '', text)
    txt = re.sub(r'^\d+\s|\s\d+\s|\s\d+$', ' ', txt)
    txt = re.sub(r'(?<=[\n])\s+|^\s+', '', txt)
    tok = RegexpTokenizer(r'\w+')
    no_punc = tok.tokenize(txt)
    lower = no_punc
    #lower=txt.split()
    words = []
    #print(lower)
    for x in lower:
        words.append(x.lower())    
    return words

if __name__ == "__main__":
    txt = """
    Lorem ipsum dolor sit amet, 13 consectetur adipiscing elit. Sed massa felis, fermentum et tortor sit amet, semper imperdiet orci. Donec congue nibh quis lacinia suscipit. Suspendisse sed felis nulla. Donec faucibus sed sem eget elementum. Curabitur quis cursus orci. Pellentesque metus magna, facilisis a arcu ut, molestie blandit tellus. Donec sagittis imperdiet arcu, id elementum odio molestie sed.
    Phasellus imperdiet lacinia dignissim. Aliquam posuere magna vel mollis dignissim. Morbi in tristique neque, eu rutrum nibh. Pellentesque elementum congue eros, ut elementum sem placerat id. Sed eget mollis lectus. Sed ut odio suscipit, feugiat justo porta, pellentesque libero. Fusce molestie est a mi tempus, a vehicula mauris consectetur. Curabitur placerat rhoncus suscipit. Pellentesque imperdiet gravida orci, sed fringilla elit porttitor rutrum. Maecenas maximus egestas odio, viverra finibus nunc viverra quis. Integer eget massa sit amet mauris consequat sagittis. In nec tortor pellentesque, maximus mauris sed, rutrum velit. In commodo felis vitae leo mollis pellentesque. Morbi interdum at nulla vitae mollis.
    Sed ultrices, eros et bibendum volutpat, quam ipsum feugiat nisi, eu varius velit nisl sit amet ex. Nunc sapien ex, pulvinar non dolor sed, mollis fringilla mi. Phasellus congue placerat elit quis tincidunt. Etiam ut leo quis nisi feugiat fermentum luctus nec nulla. Sed vitae laoreet magna. Donec sit amet lacus blandit, aliquet urna sed, accumsan elit. Fusce tincidunt tincidunt lectus a vestibulum. Sed fermentum ante vel mi posuere, non scelerisque justo dignissim. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Maecenas auctor commodo mauris id aliquam. Phasellus id semper felis. Aliquam rhoncus risus lobortis sem ultrices euismod. Donec sed ipsum purus.
    Mauris lacinia turpis vel bibendum ultrices. Nulla et egestas sem. Nam sem mi, maximus eu risus nec, laoreet sagittis justo. Proin cursus dui at varius eleifend. Aenean molestie in nisl at feugiat. In neque lorem, malesuada id elit et, vehicula pellentesque felis. Fusce maximus scelerisque quam, non efficitur ante.
    Duis non semper augue. Proin laoreet dignissim urna quis eleifend. Duis sollicitudin laoreet malesuada. Phasellus in dolor non leo tempus accumsan. Mauris felis libero, efficitur sed pellentesque vitae, faucibus at massa. Curabitur placerat et nibh lacinia feugiat. Nullam maximus orci sed leo iaculis tincidunt. Morbi vel sem non sapien interdum mollis at sed nisl. In sit amet sapien bibendum, ornare purus et, cursus leo. In mattis libero a tincidunt mollis.
    """
    print(preprocess(txt))