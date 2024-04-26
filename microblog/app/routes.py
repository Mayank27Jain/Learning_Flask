from app import app # the variable from the package

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"