"""One-shot script to add -> None to all test methods missing it."""
import re
import sys
from pathlib import Path


def fix_file(path: Path) -> int:
    content = path.read_text()
    pattern = r"(def (?:test_|setup_method)\w*\([^)]*\))(\s*:)"

    def add_return(m: re.Match[str]) -> str:
        sig = m.group(1)
        colon = m.group(2)
        if "-> None" in sig or "-> None" in colon:
            return m.group(0)
        return sig + " -> None" + colon

    new_content = re.sub(pattern, add_return, content)

    if new_content != content:
        before = content.count("-> None")
        after = new_content.count("-> None")
        path.write_text(new_content)
        return after - before
    return 0


if __name__ == "__main__":
    total = 0
    for arg in sys.argv[1:]:
        p = Path(arg)
        n = fix_file(p)
        print(f"{p.name}: +{n} annotations")
        total += n
    print(f"Total: +{total}")
