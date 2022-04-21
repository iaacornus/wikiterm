import sys

from os import get_terminal_size, getlogin
from datetime import datetime

from colors import colors
from functions import wiki

def main(word, full=False, lang="en"):
    color, cols, time_log = colors, get_terminal_size().columns, datetime.now().strftime("%H:%M:%S")
    
    print(f"{colors.CBLINK2}{colors.CGREENBG}{colors.CBOLD}Fetching definition of {word.upper()} {colors.CEND}", end="\r")

    WIKI = wiki(word.lower(), full=full, lang=lang)
    results = WIKI.fetch_info()
    
    # remove the status 
    sys.stdout.write("\033[K")
    
    if results[0] is False:
        if str(type(results[1])) == "<class 'list'>":
            print(f"{colors.CYELLOWBG}{colors.CBOLD}Perhaps you mean:{colors.CEND}")
            for num, words in enumerate(results[1]):
                print(f"╰─╼({num+1}) {words}")
        else:
            print(f"{colors.CREDBG}{colors.CBOLD}{results[1]}{colors.CEND}")
    elif results[0] is True:
        summary = results[3].replace("\n", "\n\n")

        # print the title page of wikipedia page
        print(f"{colors.CBOLD}{colors.CREDBG2} Wikipedia Page ({results[7]}): {results[1].upper()} {colors.CEND}{' '*(cols-(len(results[7])+len(results[1])+len(time_log)+21))}{time_log}")

        # print the word
        print(f"{colors.CBLUEBG}{colors.CBOLD} User ({getlogin()}) Keyword: {word.upper()} {colors.CEND}\n")
        print(f"{colors.CVIOLETBG}{colors.CBOLD} Summary {colors.CEND}\n\n{summary}\n") 

        if full is False:             
            # print the fetched information
            print(f"{summary}\n")
            
        elif full is True:            
            for contents in results[2]:
                if str(contents.title).lower() == "references" or str(contents.title).lower() == "see also" or "external links" in str(contents.title).lower():
                    pass
                else:
                    print(f"{colors.CVIOLETBG2}{colors.CBOLD} {contents.title} {colors.CEND}\n")
                    print(f"{contents.text}\n")

        print(f"{colors.CBEIGEBG}{colors.CBOLD}Wikipedia page URL(s):{colors.CEND}\n╰─╼{colors.CBOLD}Full URL:{colors.CEND} {results[5]}\n╰─╼{colors.CBOLD}Canonical URL:{colors.CEND} {results[6]}{colors.CEND}")