import sys

from colors import colors
from functions import wiki

if __name__ != "__main__":
    raise SystemExit("This is not a module for use in other scripts.")

color = colors

def main(word, fetch="summary"):
    print(f"{colors.CGREENBG}{colors.CBOLD}Fetching definition of {word.upper()} {colors.CEND}", end="\r")

    WIKI = wiki(word.lower())
    results = WIKI.fetch_summary() if fetch == "summary" else WIKI.fetch_full()

    # remove the status 
    sys.stdout.write("\033[K")
    
    if results[0] is False:
        if str(type(results[1])) == "<class 'list'>":
            print(f"{colors.CYELLOWBG}{colors.CBOLD}Perhaps you mean:{colors.CEND}")
            for num, words in enumerate(results[1]):
                print(f"\t{num+1}) {words}")
        else:
            print(f"{colors.CREDBG}{colors.CBOLD}{results[1]}{colors.CEND}")
    elif results[1] is True:
        # print the word
        print(f"{colors.CBLUEBG}{colors.CBOLD} {word.upper()} {colors.CEND}\n")
    
        if fetch == "summary": 
            summary = results[1].replace("\n", "\n\n")
            
            # print the fetched information
            print(f"{summary}\n\n{colors.CBEIGEBG}{colors.CBOLD}Wikipedia page URL(s):{colors.CEND}\n{colors.CBOLD}Full URL:{colors.CEND} {results[1]}\n{colors.CBOLD}Canonical URL:{colors.CEND} {results[2]}{colors.CEND}")

        elif fetch == "full":
            pass
  
main(word="hello")
