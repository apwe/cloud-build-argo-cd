from flask import Flask
app = Flask('example-app')

@app.route('/')
def hello():
  return "Works!\n"

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)
