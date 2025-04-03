from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Datei für persistente Speicherung
DATA_FILE = "schichten.json"

def lade_schichten():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def speichere_schichten():
    with open(DATA_FILE, "w") as f:
        json.dump(schichten, f)

# Lade bestehende Schichten
schichten = lade_schichten()

@app.route("/schichten", methods=["GET"])
def get_schichten():
    return jsonify({"schichten": schichten})

@app.route("/schichten", methods=["POST"])
def add_schicht():
    data = request.get_json()
    schichten.append(data)
    speichere_schichten()
    return jsonify({"message": "Schicht gespeichert!", "data": data})

@app.route("/schichten/<int:index>", methods=["PUT"])
def update_schicht(index):
    if 0 <= index < len(schichten):
        data = request.get_json()
        schichten[index] = data
        speichere_schichten()
        return jsonify({"message": "Schicht aktualisiert!", "data": data})
    return jsonify({"error": "Index ungültig!"}), 400

@app.route("/schichten/<int:index>", methods=["DELETE"])
def delete_schicht(index):
    if 0 <= index < len(schichten):
        entfernte_schicht = schichten.pop(index)
        speichere_schichten()
        return jsonify({"message": "Schicht gelöscht!", "data": entfernte_schicht})
    return jsonify({"error": "Index ungültig!"}), 400

if __name__ == "__main__":
    app.run(debug=True)
