import os
import uuid

from datetime import datetime

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

db = SQLAlchemy(app)


class Stain(db.Model):
    __tablename__ = "stain"
    id = db.Column(
        UUID,
        primary_key=True,
        nullable=False,
        default=str(uuid.uuid4())
        )
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    message = db.Column(db.Text)
    context = db.Column(db.Text)
    valid = db.Column(db.Boolean)
    document_id = db.Column(UUID, db.ForeignKey('document.id'))

class Document(db.Model):
    __tablename__ = "document"
    id = db.Column(
        UUID,
        primary_key=True,
        nullable=False,
        default=str(uuid.uuid4())
        )
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    text = db.Column(db.Text)
    stains = db.relationship(Stain, backref="document")


@app.route('/')
def index():
    return "Hello, world!"

@app.route('/document', methods=["POST"])
def document_post():
    document = Document()
    document.text = request.values["text"]
    db.session.add(document)
    db.session.commit()
    return (document.id, 200)

@app.route('/document/<uuid:id>', methods=["GET"])
def document_get(id):
    document = Document.query.filter_by(id=str(id)).one()
    return (document.text, 200)

def main():
    app.run(debug=True, use_reloader=True)

if __name__ == '__main__':
    main()
