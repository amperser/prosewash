import json
import sys

import spacy

import proselint

nlp = spacy.load('en')


def error_str_to_json(err_string):
    return json.loads(
        proselint.tools.errors_to_json(
            proselint.tools.lint(err_string)
            )
        )


def sentence_context(text, position):
    """The sentence in the text that includes the given position."""
    doc = nlp(text)
    print(text)
    print(type(position))
    counter = 0
    for sentence in doc.sents:
        counter += len(sentence)
        if counter >= position:
            return sentence


def main(text=None):
    if text is None:
        with open(sys.argv[1], "r") as f:
            text = f.read()
    errors = error_str_to_json(text)['data']['errors']
    for error in errors:
        print(sentence_context(text, error['start']))


if __name__ == "__main__":
    main()
