from ast import main
import subprocess
import threading
from flask import Flask, jsonify, redirect,render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/app')



def run_script():
    subprocess.run(["python", "main.py"])

def home():
    return render_template('index.html')

@app.route('/start_face_recognition', methods=['POST'])
def start_face_recognition():
    # Run the face recognition script in a separate thread
    thread = threading.Thread(target=run_script)
    thread.start()
    return jsonify({"status": "Face recognition app started"})