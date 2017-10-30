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
    counter = 0
    for sentence in doc.sents:
        counter += len(sentence.text)
        if counter >= position:
            return sentence.text


def error_is_valid(text, error):
    """Call out to Judicious and figure out if error is valid."""
    error_message = error['message']
    error_context = sentence_context(text, error['start'])
    return True


def main(text=None):
    if text is None:
        with open(sys.argv[1], "r") as f:
            text = f.read()
    errors = error_str_to_json(text)['data']['errors']

    valid_errors = [error for error in errors
                    if error_is_valid(text, error)]
    json_output = error_str_to_json(text)
    json_output['data']['errors'] = valid_errors

    print(json_output)


if __name__ == "__main__":
    main()
