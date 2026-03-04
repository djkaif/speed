from flask import Flask 
app = Flask(__name__)

@app.route('/')
def index():
  return "Server is running!"

if __name__ = 'main':
  app.run(debug=True)

  