"""Agenda 11 - Simulação de controle dos níveis de água de um reservatório."""

from colorama import Fore, Style, init

init(autoreset=False)

# Cada posição da lista representa um nível do reservatório.
situacoes = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)",
]


def definir_cor(nivel):
    """Retorna a cor correspondente ao nível informado (de 1 a 5)."""
    cores = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE]
    if 1 <= nivel <= len(cores):
        return cores[nivel - 1]
    raise ValueError("O nível deve estar entre 1 e 5.")


def mostrar_situacao(nivel):
    """Exibe a situação do reservatório e restaura a cor do terminal."""
    if not 1 <= nivel <= len(situacoes):
        raise ValueError("O nível deve estar entre 1 e 5.")

    mensagem = situacoes[nivel - 1]
    cor = definir_cor(nivel)
    print(f"{cor}Nível {nivel}: {mensagem}{Style.RESET_ALL}")


def main():
    print("=== CONTROLE DE NÍVEIS DE ÁGUA ===")
    print("Simulação do monitoramento do reservatório:\n")

    for nivel in range(1, len(situacoes) + 1):
        mostrar_situacao(nivel)

    print("\nSimulação finalizada.")


if __name__ == "__main__":
    main()
