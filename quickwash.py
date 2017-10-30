import json
import proselint
import sys

def error_str_to_json(err_string):
    return json.loads(
        proselint.tools.errors_to_json(
            proselint.tools.lint(err_string)
            )
        )

def main(text=None):
    if text is None:
        with open(sys.argv[1], "r") as f:
            text = f.read()
    print(error_str_to_json(text))

if __name__ == "__main__":
    main()
