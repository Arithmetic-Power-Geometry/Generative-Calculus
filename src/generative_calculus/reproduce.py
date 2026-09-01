from pathlib import Path
from .benchmarks import run_all

if __name__ == '__main__':
    root=Path(__file__).resolve().parents[2]
    summary=run_all(root/'results', root/'data')
    print(f"Reproduction complete: {root/'results'}")
    print(summary)
