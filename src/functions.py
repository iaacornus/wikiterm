import wikipediaapi as wikiapi
import enchant as suggest 
import urllib

class wiki:
    def __init__(self, word, lang="en") -> None:
        self.lang = lang
        self.word = word
    
    def alternative(self) -> bool:
        alpha, ALPHA, comb = list("abcdefghijklmnopqrstuvwxyz"), list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), []
        
        for x in ALPHA:
            for y in alpha:
                comb.append(x+y)
        
        if (self.word[0].upper()+self.word[1].lower()) not in comb:
            return f"Sorry the term \"{self.word}\" is not in Wikipedia\nPlease kindly correct the term and try again."
        
        else:
            wiki = "https://en.wikipedia.org/wiki/Special:AllPages/" + self.word[0].upper() + self.word[1].lower()
            
            if urllib.request.urlopen(wiki).getcode() not in [x for x in range(200, 299)]:
                return f"The source is unfortunately down."

            else:
                lang = suggest.Dict("en_US")

                lang.check(self.word)
                return lang.suggest(self.word) if lang.suggest(self.word) != [] else "There is no available suggestion for the given word."
    
    def fetch_summary(self) -> str or list:
        wiki = wikiapi.Wikipedia(self.lang)
        page_py = wiki.page(self.word)        
        
        if page_py.exists() is True:
            return f"{str(page_py.summary)}", page_py.fullurl, page_py.canonicalurl

        else:
            return self.alternative()

    def fetch_full(self) -> str:
        wiki = wikiapi.Wikipedia(self.lang, extract_format=wikiapi.ExtractFormat.WIKI)
        page_py = wiki.page(self.word)
        print(page_py.text)
        