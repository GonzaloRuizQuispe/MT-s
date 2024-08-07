from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('POSTGRES_URL')
db = SQLAlchemy(app)

@app.route('/')
def home():
    user_agent = request.headers.get('User-Agent')
    if 'Mobile' in user_agent:
        # Si el User-Agent indica un dispositivo móvil
        return render_template('movile_home.html')
    else:
        # Si el User-Agent indica un dispositivo de escritorio
        return render_template('desktop_home.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)