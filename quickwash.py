import json
import proselint
import sys


def main(text=None):
    if text is None:
        with open(sys.argv[1], "r") as f:
            text = f.read()
    json_dict = json.loads(
        proselint.tools.errors_to_json(
            proselint.tools.lint(text)
            )
        )
    print(json_dict)

if __name__ == "__main__":
    main()
