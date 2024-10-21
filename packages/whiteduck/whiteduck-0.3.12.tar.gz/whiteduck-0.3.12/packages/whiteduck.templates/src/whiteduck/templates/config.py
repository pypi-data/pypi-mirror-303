__version__ = "0.3.9"


import os
from typing import Dict

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")
COMPONENTS_DIR = os.path.join(os.path.dirname(__file__), "data/components")

POE_TEMPLATES = "packages/whiteduck.templates/src/whiteduck/templates/templates/poe_tasks/default_tasks.toml"

# Global dictionary for storing environment variables and other global information
GLOBAL_VARS = Dict[str, str]


STYLE_SPEC = {
    "banner": {
        "text_style": "bold orange3",
        "justify": "center",
    },
    "version_info": {
        "version_style": "bold",
        "company_style": "bold",
        "url_style": "cyan",
    },
    "main_title": {
        "style": "bold blue",
        "emoji": "🚀",
    },
    "panel": {
        "border_style": "bold",
        "padding": (1, 1),
    },
    "headers": {
        "h1": {
            "style": "bold blue",
            "emoji": "📌",
        },
        "h2": {
            "style": "bold cyan",
            "emoji": "🔹",
        },
        "h3": {
            "style": "bold green",
            "emoji": "➡️",
        },
    },
    "prompts": {
        "select": {
            "emoji": "🔍",
        },
        "text": {
            "emoji": "✏️",
        },
        "password": {
            "emoji": "🔒",
        },
        "file_dir": {
            "emoji": "📁",
        },
    },
    "steps": {
        "title": {
            "style": "bold yellow",
            "emoji": "🔸",
        },
        "skip": {
            "style": "yellow",
            "emoji": "⏭️",
        },
    },
    "wizard": {
        "title": {
            "style": "cyan",
            "emoji": "🧙",
        },
    },
    "module_execution": {
        "title": {
            "style": "bold magenta",
            "emoji": "🔧",
        },
        "running": {
            "style": "bold green",
            "emoji": "⚙️",
        },
        "success": {
            "style": "bold green",
            "emoji": "✅",
        },
    },
    "output": {
        "title": {
            "style": "cyan",
            "emoji": "📄",
        },
    },
    "errors": {
        "style": "bold red",
        "emoji": "❌",
    },
    "info": {
        "style": "yellow",
        "emoji": "ℹ️",
    },
}
