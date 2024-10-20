from pyfiglet import Figlet

from textual.app import App, on
from textual.containers import Horizontal, Container, VerticalScroll
from textual.widgets import Header, Footer, Button, Static, TextArea, Select

# NOTE: There are 549 fonts available.
# This is a small sample of some of the simplest and most professional looking.
# The fonts.txt file is not actually used in this script, its just for reference.
# You can also use `$ pyfiglet --list_fonts` in bash to see the list.

class PyFigletApp(App):

    CSS_PATH = "styles.tcss"

    font_options = [
        ("big", "big"),             # The display name and the actual font name
        ("small", "small"),             # which are the same, in this case.
        ("calvin_s", "calvin_s"), 
        ("slant", "slant"), 
        ("small_slant", "small_slant"), 
        ("standard", "standard"), 
        ("ansi_regular", "ansi_regular"), 
        ("modular", "modular"), 
        ("chunky", "chunky"), 
        ("broadway_kb", "broadway_kb"), 
        ("cybermedium", "cybermedium"),
    ]

    def compose(self):
        yield Header("PyFiglet Demo")

        with VerticalScroll(id="main_content"):
            self.figlet_static = PyFigletStatic("Hello, World!", font="big", classes="figlet_text")
            yield self.figlet_static

        with Horizontal(id="options_bar"):
            yield Select(options=self.font_options, value="big", id="font_select")
            yield TextArea("Enter text here", id="text_input")
            yield Button("Update Text", id="update_text")

        yield Footer()


    async def on_resize(self, event):
        width, height = event.size
        self.figlet_static.change_width(width-4)    # -4 to account for padding

    @on(Select.Changed, selector="#font_select")           
    def select_changed(self, event: Select.Changed) -> None:
        self.figlet_static.change_font(event.value)

    @on(Button.Pressed, selector="#update_text")
    def render_text(self):
        text = self.query_one("#text_input").text
        self.figlet_static.renderable = text

        # Call automatic_refresh() to update ASCII art after text change.
        self.figlet_static.automatic_refresh()

        # Since we're using a hacky custom render method, simply updating the text
        # does not make the ASCII art refresh. We need to call automatic_refresh().
        # I'm not entirely sure why this magic works, but it does.


class PyFigletStatic(Static):
    """Adds simple PyFiglet ability to the Static widget."""


    def __init__(self, *args, font: str="calvin_s", **kwargs) -> None:
        """A custom widget for turnig text into ASCII art using PyFiglet.   
        This docstring is copied from the Static widget. It's the same except for the font argument.

        This class is designed to be an easy drop in replacement for the Static widget.
        The only new argument is 'font', which has a default set to one of the smallest fonts.
        You can replace any Static widget with this and it should just work (aside from the size)

        Args:
            renderable: A Rich renderable, or string containing console markup.
            font: Font to use for the ASCII art. Default is "calvin_s".
            expand: Expand content if required to fill container.
            shrink: Shrink content if required to fill container.
            markup: True if markup should be parsed and rendered.
            name: Name of widget.
            id: ID of Widget.
            classes: Space separated list of class names.
            disabled: Whether the static is disabled or not.
            
        Common good fonts:
        - big
        - small
        - calvin_s
        - slant
        - small slant
        - standard
        - ansi_regular
        - modular
        - chunky
        - broadway_kb
        - cybermedium

        There are hundreds of fonts available.   
        TO SEE MORE FONTS (bash command):   
        `$ pyfiglet --list_fonts`

        I also included the list in a text file in the root directory of this project.
        
        """
        super().__init__(*args, **kwargs)
        self.font = font
        screen_width = self.app.size.width
        self.figlet = Figlet(font=font, width=screen_width-4)   # -4 to account for padding
        # NOTE: Figlet also has "direction" and "justify" arguments,
        # but I'm not using them here.

    # NOTE: Part of the trick here is that Textual will automatically call 
    # the render method when the screen is resized.
    # We also still need to use automatic_refresh() in the parent widget.
    def render(self):
        text = str(self.renderable)           # ensure text is a string
        self.set_styles("width: auto;") 
        return self.figlet.renderText(text)

    def change_font(self, font: str) -> None:
        self.figlet.setFont(font=font)

    def change_width(self, width: int) -> None:
        self.figlet.width = width


# for running script directly
if __name__ == "__main__":
    app = PyFigletApp()
    app.run()