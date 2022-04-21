import wikipediaapi as wiki
import enchant as suggest 

import urllib

class wiki:
    def __init__(self, word, lang="en") -> None:
        self.lang = lang
        self.word = word
        
    def fetch_summary(self) -> str or list:
        wiki = wiki.Wikipedia(self.lang)
        page_py = wiki.page(self.word)        
        alpha, ALPHA = list("abcdefghijklmnopqrstuvwxyz"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        comb = []
        
        for x in alpha:
            for y in alpha:
                comb.append(x+y)

        if page_py.exists() is True:
            return f"{str(page_py.summary)}", f"Full URL = {page_py.fullurl}\nCanonical URL = {page_py.canonicalurl}"

        else:
            if (self.word[0].upper()+self.word[1].lower()) not in comb:
                return f"Sorry the term \"{self.word}\" is not in Wikipedia\nPlease kindly correct the term and try again."
            
            else:
                wiki = "https://en.wikipedia.org/wiki/Special:AllPages/" + self.word[0].upper() + self.word[1].lower()
                
                if urllib.request.urlopen(wiki).getcode() not in [x for x in range(200, 299)]:
                    return f"The source is unfortunately down."

                else:
                    lang = suggest.Dict("en_US")

                    lang.check(self.word)
                    return lang.suggest(self.word)

    def fetch_full(self) -> str:
        wiki = wiki.Wikipedia(self.lang, extract_format=wiki.ExtractFormat.WIKI)
        
        