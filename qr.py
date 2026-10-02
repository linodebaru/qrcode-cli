#!/usr/bin/env python3
"""Generate a QR code PNG from text or a URL."""

import sys

try:
    import segno
except ImportError:
    sys.exit("pip install segno first")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: python3 qr.py '<text-or-url>' [output.png]", file=sys.stderr)
        return 1
    data = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else "qr.png"
    qr = segno.make(data, error="m")
    qr.save(out, scale=8, border=2)
    print(f"saved -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
