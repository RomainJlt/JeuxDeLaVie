import os
def clear_screen():
    """Nettoie le terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()