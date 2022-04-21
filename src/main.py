import sys

from colors import colors
from functions import wiki

if __name__ != "__main__":
    raise SystemExit("This is not a module for use in other scripts.")

color = colors

def main(word, fetch="summary"):
    WIKI = wiki(word.lower())
    print(f"{colors.CGREENBG}{colors.CBOLD}Fetching definition of {word.upper()} {colors.CEND}", end="\r")
        
    if fetch == "summary":        
        results = WIKI.fetch_summary()
        summary = results[0].replace("\n", "\n\n")

    elif fetch == "full":
        results = WIKI.fetch_full()

    # remove the status 
    sys.stdout.write("\033[K")

    # print the word
    print(f"{colors.CBLUEBG}{colors.CBOLD} {word.upper()} {colors.CEND}\n")
    
    # print the fetched information
    print(f"{summary}\n\n{colors.CBEIGEBG}{colors.CBOLD}Wikipedia page URL(s):{colors.CEND}\n{colors.CBOLD}Full URL:{colors.CEND} {results[1]}\n{colors.CBOLD}Canonical URL:{colors.CEND} {results[2]}{colors.CEND}")

word = "Python"
WIKI = wiki(word.lower())
alt = WIKI.alternative()

if str(type(alt)) == "<class 'list'>":
    print(f"{colors.CYELLOWBG}{colors.CBOLD}Perhaps you mean:{colors.CEND}")
    for num, words in enumerate(alt):
        print(f"\t{num+1}) {words}")
else:
    print(f"{colors.CREDBG}{colors.CBOLD}{alt}{colors.CEND}")