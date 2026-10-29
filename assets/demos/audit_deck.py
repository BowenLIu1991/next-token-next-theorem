#!/usr/bin/env python3
"""Check deck structure and browser geometry without modifying the source."""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")

AUDIT_JS = """
<script>
window.addEventListener('load', async () => {
  await document.fonts.ready;
  // --dump-dom has a different viewport height from --screenshot on some Chrome versions.
  // Give absolute slides an explicit 1280x720 containing block for consistent checks.
  document.getElementById('stage').style.position = 'relative';
  const report = [...document.querySelectorAll('section.slide')].map((slide, i) => {
    const title = slide.querySelector('h2,h1')?.textContent.trim();
    const footer = slide.querySelector('.footer').getBoundingClientRect();
    const problems = [];
    for (const el of slide.querySelectorAll('h1,h2,.sub,.content p,.content li,.content .big,.content .k,.content .keyline')) {
      const r = el.getBoundingClientRect();
      if (!r.width || !r.height) continue;
      const text = el.textContent.trim().slice(0, 130);
      if (r.bottom > footer.top - 8) problems.push({type:'footer_overlap',text,bottom:r.bottom});
      if (r.left < 0 || r.right > 1281) problems.push({type:'horizontal_overflow',text,left:r.left,right:r.right});
      if (el.scrollWidth > el.clientWidth + 2 && el.clientWidth) problems.push({type:'text_overflow',text});
    }
    const heading = slide.querySelector('h2');
    const sub = slide.querySelector(':scope > .sub');
    const content = slide.querySelector('.content');
    if (content) {
      const top = content.getBoundingClientRect().top;
      for (const el of content.querySelectorAll('p,li,.big,.k,.keyline')) {
        if (el.getBoundingClientRect().top < top - 2) problems.push({type:'content_above_box',text:el.textContent.trim().slice(0,100)});
      }
      const preceding = sub || heading;
      if (preceding && top < preceding.getBoundingClientRect().bottom - 2) problems.push({type:'heading_overlap'});
    }
    for (const img of slide.querySelectorAll('img')) {
      if (!img.complete || !img.naturalWidth) problems.push({type:'broken_image',src:img.getAttribute('src')});
    }
    return {page:i+1,title,problems};
  });
  const pre = document.createElement('pre');
  pre.id = 'deck-audit';
  pre.textContent = JSON.stringify(report);
  document.body.append(pre);
});
</script>
"""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--html", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    source = (ROOT / args.html).resolve()
    text = source.read_text()
    count = len(re.findall(r'<section\b[^>]*class="slide(?:\s[^"]*)?"', text))
    labels = re.findall(r'<span class="pnum">(\d+) / (\d+)</span>', text)
    if labels != [(f"{i:02d}", str(count)) for i in range(1, count + 1)]:
        raise SystemExit("Page labels do not match slide order/count")
    if re.search(r'<script\b[^>]*src=', text):
        raise SystemExit("External script found")
    def absolute_src(match: re.Match) -> str:
        value = match[1]
        if re.match(r"(?:https?:|data:|file:)", value):
            return match[0]
        return f'src="{(source.parent / value).resolve().as_uri()}"'
    text = re.sub(r'src="([^"]+)"', absolute_src, text)
    text = text.replace("</body>", AUDIT_JS + "</body>")
    with tempfile.TemporaryDirectory(prefix="deck-audit-") as temp:
        temp = Path(temp)
        audit = temp / "audit.html"
        audit.write_text(text)
        result = subprocess.run([
            CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
            "--window-size=1280,720", "--virtual-time-budget=5000",
            f"--user-data-dir={temp / 'profile'}", "--dump-dom",
            audit.as_uri() + "?clean=1",
        ], check=True, capture_output=True, text=True)
        match = re.search(r'<pre id="deck-audit">(.*?)</pre>', result.stdout, re.S)
        if not match:
            raise SystemExit("Browser audit did not finish")
        report = json.loads(html.unescape(match[1]))
    out = (ROOT / args.out).resolve()
    out.write_text(json.dumps({"source": str(source), "slides": count, "pages": report}, ensure_ascii=False, indent=2))
    findings = [(p["page"], p["problems"]) for p in report if p["problems"]]
    print(json.dumps({"slides": count, "flagged_pages": findings, "report": str(out)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
