from app import app


@app.route("/")
def default():
    return "<h2>Hello.</h2>"
@app.route("/index")

def index():
    return "Hello world"