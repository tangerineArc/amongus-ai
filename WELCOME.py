import sys
#this is a very basic terminal page we have made will try to improve it for sure in future


from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

console = Console()


def welcome():
    # Display color options
    table = Table(title="🎨 Choose Your Color 🎨", style="bold cyan")
    colors = ["Black","Brown","Pink","White","Red", "Blue", "Green", "Yellow", "Purple", "Orange"]

    table.add_column("No.", justify="center", style="bold white")
    table.add_column("Color", justify="center", style="bold")

    for i, color in enumerate(colors, 1):
        table.add_row(str(i), f"[bold {color.lower()}]{color}[/bold {color.lower()}]")

    console.print(table)

    # Ask user to pick a color
    color_choice = Prompt.ask("Enter the number of your color", choices=[str(i) for i in range(1, len(colors) + 1)])
    console.print(f"You selected: [bold {colors[int(color_choice) - 1].lower()}]{colors[int(color_choice) - 1]}[/bold {colors[int(color_choice) - 1].lower()}]")

    # Display player selection
    num_players = Prompt.ask("How many players? (2-6)(Excluding you OBVIOUSLY....)", choices=[str(i) for i in range(2,9)])
    console.print(f"[bold green]You selected {num_players} players.[/bold green] 🎮")
    return (int)(color_choice),(int)(num_players)


#we have photos only for red,yellow,orange,green,blue

