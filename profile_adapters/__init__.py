"""profile adapter 注册：方便 CLI 一行切换。"""
from pathlib import Path

import yaml

PROFILES = Path(__file__).resolve().parent.parent / "profiles.yaml"


def get(name):
    return (yaml.safe_load(PROFILES.read_text()) or {}).get(name)


def all_names():
    return list((yaml.safe_load(PROFILES.read_text()) or {}).keys())
