"""Make the self-contained teaching module importable from any pytest working directory."""

from pathlib import Path
import sys


MODULE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MODULE_ROOT))
