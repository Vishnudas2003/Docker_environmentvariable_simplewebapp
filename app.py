import os
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

app = Flask(__name__)

color = os.environ.get('APP_COLOR')

@app.route('/')
def main():
   print(color)
   return render_template('index.html', color=color)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)