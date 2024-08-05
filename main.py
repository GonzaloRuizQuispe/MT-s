from flask import Flask, render_template, request

app = Flask(__name__)

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
    app.run(debug=True)