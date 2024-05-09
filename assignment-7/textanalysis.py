import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('vader_lexicon')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer , WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer

text = """Welcome you to programming knowledge. Lets start with out first program on NLTK.We'll learn"""
demoWords= ['playing','happiness','going','go','playing','play','yes','no','having','bad','coding','programming','program']

stop_words = set(stopwords.words('english'))
#print(stop_words)


# tokenization
from nltk.tokenize import word_tokenize , sent_tokenize

tokenized_words = word_tokenize(text)
#print(words)

#removing stop words from tokenized worda
tokenized_words_without_stop_words = []
for word in tokenized_words:
    if word not in stop_words:
        tokenized_words_without_stop_words.append(word)
#words removed (these are stopwords)
# print('Stopwords that get removed from text are',set(tokenized_words)-set(tokenized_words_without_stop_words))
# print ('Tokenized words which includes stop words',tokenized_words)
# print('Without stop words',tokenized_words_without_stop_words)


#lemmatization and stemming
# lemmalizer = WordNetLemmatizer()
# stemmer = PorterStemmer()

# for word in demoWords:
#     #word stem lemmatize
#     print(word,stemmer.stem(word),lemmalizer.lemmatize(word,'v'))
        
sia = SentimentIntensityAnalyzer()
print(sia.polarity_scores("Programming in fun"))
