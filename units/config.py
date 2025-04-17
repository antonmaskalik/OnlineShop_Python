import json
from pathlib import Path


class Config:
    CONFIG_PATH = Path(__file__).parent.parent / "configs" / "default.json"

    def __init__(self):
        self._load_config()

    def _load_config(self):
        if not self.CONFIG_PATH.exists():
            raise FileNotFoundError(f"Config file not found at {self.CONFIG_PATH}")

        with open(self.CONFIG_PATH, "r") as f:
            config = json.load(f)

        self.BROWSER = config.get("browser").lower()
        self.HEADLESS = config.get("headless") == "true"
        self.BASE_URL = config.get("base_url")
        self.WINDOW_SIZE = config.get("window_size", {})
