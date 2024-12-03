from fasthtml.common import (
    Div,
    FastHTML,
    H1,
    P,
    serve,
    Title,
)

app = FastHTML()


@app.get("/")
def home():
    return (
        Title("Page Demo"),
        Div(H1("Hello, World")),
        P("Some text"),
        P("Some more text"),
    )


serve()
