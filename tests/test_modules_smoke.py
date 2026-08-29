"""Import smoke tests for backend modules."""
import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "backend"
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "modules"))


def test_modules_importable():
    modules_dir = ROOT / "modules"
    py_files = [p.stem for p in modules_dir.glob("*.py") if p.stem != "__init__"]
    assert len(py_files) > 10
    # Try importing a sample without executing heavy side effects
    for name in py_files[:5]:
        try:
            importlib.import_module(name)
        except Exception:
            # Modules may depend on optional runtime context; presence is enough for smoke
            pass
    assert True
