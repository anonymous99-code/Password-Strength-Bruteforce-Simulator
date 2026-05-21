from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def load_logo():

    try:
        logo_path = Path(__file__).parent / "assets" / "logo.txt"

        with open(logo_path, "r", encoding="utf-8") as f:
            return f.read()

    except:
        return "PASSENTINEL"


def display_result(password, result):

    score_colors = {
        0: "red",
        1: "red",
        2: "yellow",
        3: "cyan",
        4: "green"
    }

    score_labels = {
        0: "VERY WEAK",
        1: "WEAK",
        2: "MODERATE",
        3: "STRONG",
        4: "VERY STRONG"
    }

    score = result["score"]

    console.print(load_logo())

    table = Table(title="Password Analysis")

    table.add_column("Metric")
    table.add_column("Value")

    table.add_row(
        "Strength",
        f"[{score_colors[score]}]{score_labels[score]}[/{score_colors[score]}]"
    )

    table.add_row(
        "Estimated Guesses",
        str(result["guesses"])
    )

    table.add_row(
        "Offline Fast Hashing",
        result["crack_times"]["offline_fast_hashing_1e10_per_second"]
    )

    feedback = result["feedback"]["suggestions"]

    if feedback:

        table.add_row(
            "Suggestions",
            "\n".join(feedback)
        )

    console.print(
        Panel(
            table,
            title="PASSENTINEL",
            border_style=score_colors[score]
        )
    )

def display_simulation(result):

    table = Table(title="Brute Force Simulation")

    table.add_column("Metric")
    table.add_column("Value")

    if result.get("error"):

        table.add_row("Error", result["error"])

        console.print(table)

        return

    status = (
        "[green]SUCCESS[/green]"
        if result["success"]
        else "[red]FAILED[/red]"
    )

    table.add_row("Attack Status", status)
    table.add_row("Attempts", str(result["attempts"]))
    table.add_row("Time Taken", f"{result['time']} sec")

    if result["success"]:

        table.add_row(
            "Discovered Password",
            result["password"]
        )

    console.print(
        Panel(
            table,
            title="PASSENTINEL Simulator",
            border_style="red"
        )
    )