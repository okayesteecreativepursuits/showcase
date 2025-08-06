from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('base.html')

# Run the app or freeze the static site
if __name__ == "__main__":
    app.run(debug=True)  # Generate static files for deployment