#!/usr/bin/env python3
"""Render every slide in the selected HTML deck to a full-bleed PDF.

The deck is designed for 1280x720 screens. Chrome's print-to-PDF leaves
default margins, so this script screenshots each slide with ?clean=1 and
stitches the images into a 13.333 x 7.5 in PDF (96 dpi).

Usage:
    python3 assets/demos/render_pdf.py
    CHROME="/path/to/Chrome" python3 assets/demos/render_pdf.py
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import tempfile
import time
from pathlib import Path

from PIL import Image
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
CHROME = os.environ.get(
    "CHROME",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
)
W, H = 1280, 720


def screenshot(url: str, out: Path, profile: Path) -> None:
    cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--window-size=1280,720",
        f"--user-data-dir={profile}",
        "--virtual-time-budget=4000",
        "--run-all-compositor-stages-before-draw",
        f"--screenshot={out}",
        url,
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--html", default="docs/index.html", help="HTML file to render")
    ap.add_argument("--out", default="docs/from-next-token-to-next-theorem.pdf", help="PDF output")
    ap.add_argument("--contact-sheet", help="Optional overview PNG for visual review")
    args = ap.parse_args()
    html_path = (ROOT / args.html).resolve()
    out_path = (ROOT / args.out).resolve()
    pages = len(re.findall(r'<section\b[^>]*class="slide(?:\s[^"]*)?"', html_path.read_text()))
    if not pages:
        raise SystemExit(f"No slides found: {html_path}")

    if not Path(CHROME).exists():
        raise SystemExit(f"Chrome not found: {CHROME}")

    tmp = Path(tempfile.mkdtemp(prefix="opencode-pdf-"))
    profile = tmp / "chrome-profile"
    try:
        images = []
        for i in range(pages):
            url = html_path.as_uri() + f"?s={i}&clean=1&v={time.time_ns()}"
            png = tmp / f"page-{i:02d}.png"
            screenshot(url, png, profile)
            im = Image.open(png).convert("RGB")
            if im.size != (W, H):
                raise SystemExit(f"page {i + 1}: expected {W}x{H}, got {im.size}")
            images.append(im)
            print(f"  {i + 1:02d}/{pages}")

        if args.contact_sheet:
            columns = 5
            sheet = Image.new("RGB", (columns * 256, ((pages + columns - 1) // columns) * 144), "white")
            for i, image in enumerate(images):
                sheet.paste(image.resize((256, 144)), ((i % columns) * 256, (i // columns) * 144))
            sheet.save((ROOT / args.contact_sheet).resolve())

        images[0].save(
            out_path,
            "PDF",
            resolution=96.0,
            save_all=True,
            append_images=images[1:],
        )
        print(f"\nwrote {out_path} ({out_path.stat().st_size / 1e6:.1f} MB)")
        print(f"pages: {len(PdfReader(out_path).pages)}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
