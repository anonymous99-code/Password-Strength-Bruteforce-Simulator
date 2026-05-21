import typer

from app.strength import analyze_password
from app.simulator import simulate_attack
from app.ui import display_result, display_simulation

app = typer.Typer()


@app.command()
def check(password: str):
    """
    Analyze password strength
    """

    result = analyze_password(password)

    display_result(password, result)


@app.command()
def simulate(password: str):
    """
    Simulate brute force attack
    """

    result = simulate_attack(
        password,
        "wordlists/common.txt"
    )

    display_simulation(result)


def main():
    app()


if __name__ == "__main__":
    main()