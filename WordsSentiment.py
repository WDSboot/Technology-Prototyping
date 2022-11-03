import pandas as pd
import matplotlib.pyplot as plt

# Je maakt een dictionary aan om de woorden apart in op te slaan
d = dict()
    
# Woordenlijst met woorden en score tussen -4 (uiterst negatief) en +4 (uiterst positief), bron: https://ithaka.github.io/tdm-notebooks/sentiment-analysis-with-vader.html
def words_sentiment(compound, line):
# Woorden tellen (count) adhv volgende bron: https://www.geeksforgeeks.org/python-count-occurrences-of-each-word-in-given-text-file/
    # Verwijderen van spaties en enters
    line = line.strip()
    # De regel splitsen in woorden
    words = line.split(" ")

    # Over elk woord in elke zin itereren
    for word in words:
    # Checken of het woord al in de aangemaakte dictionary staat
        if word in d:
            # Als het woord al in de dictionary staat, voeg je het woord bij de count toe
            count = d[word][0] + 1
            d[word] = [ 
                count,
                # Bij compound tel je de waarden bij elkaar op, zodat je later het gemiddelde v/d compound kan berekenen
                compound + d[word][1]
            ]
        else:
            # Woord toevoegen aan dictionary als dit woord nog niet voorkomt
            d[word] = [
                1,
                compound
            ]

def print_graphs():
    # Bron: https://realpython.com/iterate-through-dictionary-python/
    word_sentiment = []

    for key, val in d.items():
        val[1] = val[1] / val[0]
        word_sentiment.append([key] + val)

    # Pandas dataframe aanmaken met 3 kolommen per woord
    dfWordSentiment = pd.DataFrame(word_sentiment, columns=['Word', 'Count', 'Compound'])

    # Waarden van de count sorteren op aflopende volgorde (hoogste aantal eerst) en alleen de top 30 laten zien van de count, 
    # bronnen: https://www.geeksforgeeks.org/how-to-sort-pandas-dataframe/
    # https://stackoverflow.com/a/43859466
    mostCommonWords = dfWordSentiment.sort_values(by=['Count'], ascending=False).head(25)

    # Bar maken, bron: https://towardsdatascience.com/very-simple-python-script-for-extracting-most-common-words-from-a-story-1e3570d0b9d0
    threshold_pos = 0.05
    threshold_neg = -0.05
    mostCommonWords.plot.bar(x='Word',y='Compound', color='green')
    # Grenslijnen, bron: https://www.folkstalk.com/tech/how-to-draw-threshold-line-in-bar-graph-python-with-code-examples/
    plt.axhline(y=threshold_pos, linewidth=1, color='black', linestyle ="--")
    plt.axhline(y=threshold_neg, linewidth=1, color='black', linestyle ="--")


    mostNegativeWords = dfWordSentiment.sort_values(by=['Compound'], ascending=True).head(10)
    mostNegativeWords.plot.bar(x='Word',y='Compound',color='green')
