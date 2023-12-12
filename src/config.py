from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent
TRANSACTIONS_PATH = ROOT_PATH.joinpath("data", "operations.json")
