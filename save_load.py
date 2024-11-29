import pickle

def save_grid(grid, filename="game_save.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(grid, f)

def load_grid(filename="game_save.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None
