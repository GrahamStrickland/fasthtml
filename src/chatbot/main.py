from claudette import Client, contents, models
from fasthtml.common import (
    Button,
    Div,
    FastHTML,
    Form,
    Group,
    Hidden,
    Input,
    Link,
    picolink,
    Script,
    serve,
    Titled,
)


hdrs = (
    picolink,
    Script(src="https://cdn.tailwindcss.com"),
    Link(
        rel="stylesheet",
        href="https://cdn.jsdelivr.net/npm/daisyui@4.11.1/dist/full.min.css",
    ),
)
app = FastHTML(hdrs=hdrs, cls="p-4 max-w-lg mx-auto")


cli = Client(models[-1])
sp = "You are a helpful and concise assistant."


def ChatMessage(msg, user):
    bubble_class = "chat-bubble-primary" if user else "chat-bubble-secondary"
    chat_class = "chat-end" if user else "chat-start"
    return Div(cls=f"chat {chat_class}")(
        Div("user" if user else "assistant", cls="chat-header"),
        Div(msg, cls=f"chat-bubble {bubble_class}"),
        Hidden(msg, name="messages"),
    )


def ChatInput():
    return Input(
        name="msg",
        id="msg-input",
        placeholder="Type a message",
        cls="input input-bordered w-full",
        hx_swap_oob="true",
    )


@app.get
def index():
    page = Form(hx_post=send, hx_target="#chatlist", hx_swap="beforeend")(
        Div(id="chatlist", cls="chat-box h-[73vh] overflow-y-auto"),
        Div(cls="flex space-x-2 mt-2")(
            Group(ChatInput(), Button("Send", cls="btn btn-primary"))
        ),
    )
    return Titled("Chatbot Demo", page)


@app.post
def send(msg: str, messages: list[str] = None):
    if not messages:
        messages = []
    messages.append(msg.strip())
    r = contents(cli(messages, sp=sp))
    return (ChatMessage(msg, True), ChatMessage(r.strip(), False), ChatInput())


serve()
