import getpass
from utils import evaluate_password, check_pwned
from rich import print

def main():
    print("[bold cyan]🔐 Password Strength Inspector 🔍[/bold cyan]")
    password = getpass.getpass("Ingresa tu contraseña: ")

    print("\n[bold]📊 Evaluando seguridad...[/bold]")
    score, feedback = evaluate_password(password)

    print(f"\n[bold yellow]Puntuación:[/bold yellow] {score}/100")
    for comment in feedback:
        print(f"- {comment}")

    choice = input("\n¿Quieres revisar si fue filtrada en la web? (s/n): ").strip().lower()
    if choice == 's':
        breaches = check_pwned(password)
        if breaches:
            print(f"[red]⚠️ Tu contraseña apareció en {breaches} filtraciones. Cámbiala urgente.[/red]")
        else:
            print("[green]✅ No se encontraron filtraciones. ¡Bien ahí![/green]")

if __name__ == "__main__":
    main()
