"""Application configuration and repo root detection."""
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Settings:
    port: int = 8000

    # Auto-detect repo root: webapp/ parent directory
    webapp_dir: Path = field(default_factory=lambda: Path(__file__).resolve().parent.parent)

    @property
    def repo_root(self) -> Path:
        return self.webapp_dir.parent

    @property
    def config_path(self) -> Path:
        return self.repo_root / "config.json"

    # Directories excluded from the file browser
    excluded_dirs: frozenset = frozenset({
        "webapp", ".git", ".agents", ".venv", "__pycache__", ".DS_Store", ".claude", ".pm_agent"
    })

    # Only show these file extensions
    allowed_extensions: frozenset = frozenset({".md"})


settings = Settings()
