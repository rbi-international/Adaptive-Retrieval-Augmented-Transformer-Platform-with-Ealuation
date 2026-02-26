from pathlib import Path

# Root directory
ROOT = Path("ai_platform")

# Folder structure blueprint
STRUCTURE = {
    "apps": ["api", "worker"],
    "packages": [
        "core",
        "llm_gateway",
        "ingestion",
        "retrieval",
        "orchestration",
        "evaluation",
        "monitoring",
        "drift",
        "transformer_math",
    ],
    "research": ["notebooks"],
    "infra": ["docker", "ci"],
    "tests": [],
    "docs": [],
}

# Files to create at root level
ROOT_FILES = [
    "pyproject.toml",
    "README.md",
    ".env.example",
]

# Files inside docs
DOC_FILES = [
    "architecture.md",
    "math_notes.md",
    "design_tradeoffs.md",
    "failure_modes.md",
]


def create_structure():
    print(f"Creating project structure at: {ROOT.resolve()}")
    
    # Create root
    ROOT.mkdir(exist_ok=True)

    # Create folders
    for parent, children in STRUCTURE.items():
        parent_path = ROOT / parent
        parent_path.mkdir(exist_ok=True)

        for child in children:
            (parent_path / child).mkdir(exist_ok=True)

    # Create root files
    for file in ROOT_FILES:
        (ROOT / file).touch(exist_ok=True)

    # Create docs files
    docs_path = ROOT / "docs"
    docs_path.mkdir(exist_ok=True)

    for file in DOC_FILES:
        (docs_path / file).touch(exist_ok=True)

    print("AI Platform structure created successfully.")


if __name__ == "__main__":
    create_structure()