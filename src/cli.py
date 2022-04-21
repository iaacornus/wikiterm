import argparse

from main import main
from colors import colors

color = colors

def program_options():
    description = "wiki (iaacornus/wiki-term) is a wikipedia client for terminal written in Python with martin-majlis/Wikipedia-API."
    parser = argparse.ArgumentParser(prog="wiki", usage="wiki [TERM] [OPTIONS]",
                                     description=description, epilog="Cheers!")

    parser.add_argument("word")
    parser.add_argument("-f", "--full", help="Search for the full text page.",
                        action="store_true")
    
    args = parser.parse_args()
    print(args.word)
    main(args.word, args.full)

try:
    if __name__ == "__main__":
        program_options()
except KeyboardInterrupt:
    raise SystemExit(f"{color.CRED}Keyboard Interrupt.{color.CEND}")
except ConnectionError:
    raise SystemExit(f"{color.CRED}Connection Error.{color.CEND}")
