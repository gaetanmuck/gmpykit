import textwrap
import re
import unicodedata


def wrap(text, length=150):
    texts = text.split("\n")
    wraped_texts = [textwrap.wrap(text, length) for text in texts]

    result = ""
    first = True
    for lines in wraped_texts:
        for line in lines:
            result += ("\n" if not first else "") + line
            first = False
        if len(lines) == 0:
            result += "\n"

    return result


def cli_bold(text):
    return "\033[1m" + text + "\033[0m"


def cli_underline(text):
    return "\033[4m" + text + "\033[0m"


def cli_italic(text):
    return "\033[3m" + text + "\033[0m"


def to_camel_case(text):
    output = "".join(x for x in text.title() if x.isalnum()).replace("'", "")
    return output[0].lower() + output[1:]


def to_snake_case(text):
    # Normalize text to decompose accented characters (e.g., é -> e)
    normalized_text = unicodedata.normalize("NFKD", text)

    # Remove diacritics (accents) by filtering out non-ASCII characters
    no_accents_text = "".join([c for c in normalized_text if not unicodedata.combining(c)])

    # Remove punctuation
    cleaned_text = re.sub(r"[^\w\s]", "", no_accents_text)

    # Replace spaces with underscores and convert to lowercase
    snake_case_text = re.sub(r"\s+", "_", cleaned_text.strip()).lower()

    return snake_case_text
