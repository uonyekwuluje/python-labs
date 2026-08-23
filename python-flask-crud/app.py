import os

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

# External PostgreSQL connection.
#
# Example:
# postgresql+psycopg://username:password@hostname:5432/database
#
# The DATABASE_URL environment variable is supplied when the
# container is started.
database_url = os.getenv("DATABASE_URL")

if not database_url:
    raise RuntimeError("DATABASE_URL environment variable is required")

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


# CREATE
@app.route("/api/items", methods=["POST"])
def create_item():
    data = request.get_json(silent=True) or {}

    name = str(data.get("name", "")).strip()
    description = str(data.get("description", "")).strip()

    if not name:
        return jsonify({"error": "Name is required"}), 400

    item = Item(
        name=name,
        description=description,
    )

    db.session.add(item)
    db.session.commit()

    return jsonify(item.to_dict()), 201


# READ - all
@app.route("/api/items", methods=["GET"])
def get_items():
    items = Item.query.order_by(Item.id.desc()).all()

    return jsonify([item.to_dict() for item in items])


# READ - one
@app.route("/api/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = db.session.get(Item, item_id)

    if item is None:
        return jsonify({"error": "Item not found"}), 404

    return jsonify(item.to_dict())


# UPDATE
@app.route("/api/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = db.session.get(Item, item_id)

    if item is None:
        return jsonify({"error": "Item not found"}), 404

    data = request.get_json(silent=True) or {}

    name = str(data.get("name", "")).strip()
    description = str(data.get("description", "")).strip()

    if not name:
        return jsonify({"error": "Name is required"}), 400

    item.name = name
    item.description = description

    db.session.commit()

    return jsonify(item.to_dict())


# DELETE
@app.route("/api/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = db.session.get(Item, item_id)

    if item is None:
        return jsonify({"error": "Item not found"}), 404

    db.session.delete(item)
    db.session.commit()

    return jsonify({"message": "Item deleted"})


@app.cli.command("init-db")
def init_db():
    """Create database tables."""
    db.create_all()
    print("Database initialized.")


@app.errorhandler(IntegrityError)
def handle_integrity_error(error):
    db.session.rollback()
    return jsonify({"error": "Database integrity error"}), 409


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(host="0.0.0.0", port=5000, debug=True)
