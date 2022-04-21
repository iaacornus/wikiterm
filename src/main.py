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

    sys.stdout.write("\033[K")

    print(f"{colors.CBLUEBG}{colors.CBOLD} {word.upper()} {colors.CEND}\n")
    print(f"{summary}\n\n{colors.CREDBG}{colors.CBOLD}Wikipedia page URL(s):{colors.CEND}\n{colors.CBOLD}Full URL:{colors.CEND} {results[1]}\n{colors.CBOLD}Canonical URL:{colors.CEND} {results[2]}{colors.CEND}")

    
main("space", fetch="full")