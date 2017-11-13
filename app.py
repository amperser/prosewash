from flask import Flask, request
# from quickwash import

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, world!"

@app.route('/document', methods=["POST"])
def document_post():
    app.logger.info(request.values["text"])
    return ("post job!", 200)

@app.route('/document', methods=["GET"])
def document_get():
    return ('you got it', 200)

def main():
    app.run(debug=True, use_reloader=True)

if __name__ == '__main__':
    main()
