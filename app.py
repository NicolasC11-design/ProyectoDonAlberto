from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

peritajes_db = [
    {
	"placa": "ABC-123",
	"modelo": "2024"
    }
]

@app.route('/api/repuestos')
def get_repuestos():
	return jsonify({
		"status": "online",
		"servidor": "Ubuntu de Nicolas Cristiano",
		"hora_servidor": str(datetime.datetime.now()),
		"inventario": ["Bujias de Iridio", "Filtro de aceite", "Aceite motul 7100"]
	})

@app.route('/api/peritajes', methods=['POST'])
def crear_peritaje():
	data = request.get_json()

	if not data or 'placa' not in data:
		return jsonify({"error": "Falta el dato de la placa"}), 400

	nuevo_peritaje = {
		"placa": data['placa'],
		"modelo": data.get('modelo', '2026'),
		"fecha_registro": str(datetime.datetime.now())
	}

	peritajes_db.append(nuevo_peritaje)
	return jsonify({
		"mensaje": "Moto registrada correctamente",
		"peritaje": nuevo_peritaje
	}), 201

@app.route('/api/peritajes', methods=['GET'])
def get_peritajes():
	return jsonify({
		"peritajes_guardados": peritajes_db
	})

if __name__ == "__main__":
    app.run()
