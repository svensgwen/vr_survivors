from rich.console import Console
from rich.panel import Panel

console = Console()

"""
### Example Usage
```py
from modules.decors.boxes import fancy_box

fancy_box("You leveled up! 🎉", title="LEVEL UP", style="bold green")
```
"""



def fancy_box(text, title="✨ Decoration ✨", style="bold magenta"):
    panel = Panel.fit(
        text,
        title=title,
        border_style=style,
        padding=(1, 2)
    )
    console.print(panel)

def banner_box(content, title="🔥 SYSTEM ONLINE 🔥", subtitle="Sven Creations"):
    panel = Panel.fit(
        text = "[bold green]"+content+"[/bold green] 👾",
        title=title,
        subtitle=subtitle,
        b_style ="bright_magenta",
        padding=(1, 4)
    )
    console.print(panel)
