import sys
from pathlib import Path

for item in ["mtmtrain", "mtmlib", "mtmdb", "mtmscreentocode"]:
    sys.path.insert(
        0, str(Path(f"{Path(__file__).resolve().parent}/../../../{item}").resolve())
    )
