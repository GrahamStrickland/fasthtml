from fasthtml.common import (
    FastHTML,
    H1,
    serve,
)

app = FastHTML()


@app.get("/")
def home():
    return H1("Hello, World")


@app.route("/", methods=["post", "put"])
def post_or_put():
    return "got a POST or PUT request"


@app.get("/greet/{nm}")
def greet(nm: str):
    return f"Good day to you, {nm}!"


serve()
