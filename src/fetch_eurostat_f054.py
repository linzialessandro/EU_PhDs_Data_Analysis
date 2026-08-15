#!/usr/bin/env python3
"""Compatibility wrapper. Prefer src/fetch_eurostat.py."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_eurostat import main

if __name__ == "__main__":
    main()
