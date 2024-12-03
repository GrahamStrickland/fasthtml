from fasthtml.common import (
    FastHTML,
    H1,
    Main,
    picolink,
    serve,
    Style,
    Title,
)


css = Style(":root {--pico-font-size:90%,--pico-font-family: Pacifico, cursive;}")
app = FastHTML(hdrs=(picolink, css))


@app.get("/")
def home():
    return (Title("Hello World"), Main(H1("Hello, World"), cls="container"))


@app.route("/", methods=["post", "put"])
def post_or_put():
    return "got a POST or PUT request"


@app.get("/greet/{nm}")
def greet(nm: str):
    return f"Good day to you, {nm}!"


serve()
