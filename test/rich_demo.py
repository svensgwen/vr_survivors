from rich.console import Console
from rich.text import Text

console = Console()

# Basic text with RGB colors
console.print("This is [bold red]bold red[/bold red] text.")
console.print("This is [green]green[/green] and [blue]blue[/blue] text.")

# Using hex colors
console.print("Custom color: [#ff69b4]Hot Pink[/#ff69b4] 💖")
console.print("Gradient test: [#FF0000]R[/#FF0000][#FF7F00]A[/#FF7F00][#FFFF00]I[/#FFFF00][#00FF00]N[/#00FF00][#0000FF]B[/#0000FF][#4B0082]O[/#4B0082][#9400D3]W[/#9400D3] 🌈")

# Styled text using Text object
rainbow_text = Text("This is styled with RGB", style="bold underline #00ffee on #222222")
console.print(rainbow_text)

# Emojis + formatting
console.print(":rocket: [bold cyan]Launch sequence initiated...[/bold cyan]")
console.print(":zap: [blink bold magenta]Power Surge![/blink bold magenta]")
