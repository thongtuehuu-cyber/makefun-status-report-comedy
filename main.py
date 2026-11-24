import os
import sys

LINE = "Status: green. The dashboard is green because I changed what green means. The work is exactly where you left it."

def main():
    if len(LINE) >= 200:
        sys.exit("line must be under 200 characters")
    if "\n" in LINE or "\r" in LINE:
        sys.exit("line must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
