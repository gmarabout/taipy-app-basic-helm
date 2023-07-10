"""
A single-page Taipy application.

Please refer to https://docs.taipy.io/en/latest/manuals/gui/ for more details.
"""

import webbrowser

from taipy.gui import Markdown, notify
import taipy as tp

value = 0
logo = "images/taipy_logo.jpg"

page = Markdown(
"""
<center>
<|navbar|lov={[("page1", "Homepage"), ("https://docs.taipy.io/en/latest/manuals/about/", "Taipy Docs"), ("https://docs.taipy.io/en/latest/getting_started/", "Getting Started")]}|>
</center>

<|
<center>
    <|{logo}|image|height=200px|width=200px|on_action=image_action|>
</center>
|>

# Taipy Application

<|{value}|slider|on_change=on_slider|> <|Push|button|on_action=on_push|>
"""
)


def image_action(state):
    webbrowser.open("https://taipy.io")


def on_push(state):
    ...


def on_slider(state):
    if state.value == 100:
        notify(state, "success", "Taipy is running!")


def on_change(state, var_name: str, var_value):
    ...


gui = tp.Gui(page=page)

if __name__ == '__main__':
    # Execute by the _Python_ interpretor, for debug only.
    tp.run(gui, title="Taipy Application (development)")
else:
    # Execute by _Gunicorn_, for production environment.
    app = tp.run(gui, title="Taipy Application", run_server=False)