# Schichtplaner3
Schichtplaner API
Dies ist eine einfache API zur Verwaltung von Schichten. Die API ermöglicht das Erstellen, Abrufen, Aktualisieren und Löschen von Schichten.
Installation
1.	Repository klonen:
2.	git clone <DEIN-REPO-LINK>
3.	In das Projektverzeichnis wechseln:
4.	cd schichtplaner
5.	Erforderliche Abhängigkeiten installieren:
6.	pip install -r requirements.txt
Nutzung
Starten des Servers
python app.py
Die API läuft dann auf http://127.0.0.1:5000.
API-Endpunkte
•	GET /schichten – Gibt alle Schichten zurück
•	POST /schichten – Erstellt eine neue Schicht (JSON-Daten im Body erforderlich)
•	PUT /schichten/ – Aktualisiert eine bestehende Schicht
•	DELETE /schichten/ – Löscht eine Schicht
Beispiel-Request
Neue Schicht hinzufügen
{
    "datum": "2024-04-02",
    "zeit": "09:00-17:00",
    "mitarbeiter": "Max Mustermann"
}
