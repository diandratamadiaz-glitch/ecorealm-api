import os
import psycopg2
import psycopg2.extras
from flask import Flask, jsonify, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    return conn

@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "sukses", "message": "API EcoRealm aktif!"}), 200

# ==========================================
# CRUD TABEL 'pemain'
# ==========================================

# 1. READ (GET): Mengambil semua data pemain
@app.route('/pemain', methods=['GET'])
def get_pemain():
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) 
        cur.execute('SELECT * FROM pemain ORDER BY id_pemain ASC;')
        pemain = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify({"status": "sukses", "data": pemain}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# 2. CREATE (POST): Menambah pemain baru
@app.route('/pemain', methods=['POST'])
def add_pemain():
    try:
        data = request.get_json()
        
        # username dan kata_sandi wajib ada sesuai skema NOT NULL
        username = data['username']
        kata_sandi = data['kata_sandi']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO pemain (username, kata_sandi) VALUES (%s, %s) RETURNING id_pemain;',
            (username, kata_sandi)
        )
        new_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({
            "status": "sukses", 
            "message": "Pemain berhasil ditambahkan", 
            "data": {"id_pemain": new_id, "username": username}
        }), 201
    except KeyError:
        return jsonify({"status": "error", "message": "Field 'username' dan 'kata_sandi' wajib diisi!"}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# 3. UPDATE (PUT): Mengubah kata sandi pemain berdasarkan ID
@app.route('/pemain/<int:id_pemain>', methods=['PUT'])
def update_pemain(id_pemain):
    try:
        data = request.get_json()
        kata_sandi_baru = data['kata_sandi']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'UPDATE pemain SET kata_sandi = %s WHERE id_pemain = %s RETURNING id_pemain;',
            (kata_sandi_baru, id_pemain)
        )
        updated = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        if updated is None:
            return jsonify({"status": "error", "message": "Pemain tidak ditemukan"}), 404

        return jsonify({"status": "sukses", "message": f"Kata sandi pemain ID {id_pemain} berhasil diubah"}), 200
    except KeyError:
        return jsonify({"status": "error", "message": "Field 'kata_sandi' wajib diisi!"}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# 4. DELETE: Menghapus pemain berdasarkan ID
@app.route('/pemain/<int:id_pemain>', methods=['DELETE'])
def delete_pemain(id_pemain):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('DELETE FROM pemain WHERE id_pemain = %s RETURNING id_pemain;', (id_pemain,))
        deleted = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        if deleted is None:
            return jsonify({"status": "error", "message": "Pemain tidak ditemukan"}), 404

        return jsonify({"status": "sukses", "message": f"Pemain ID {id_pemain} berhasil dihapus"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)