"""Emit the markdown twin from the rendered report, so the two cannot drift."""
import sys, pathlib
from playwright.sync_api import sync_playwright

JS = r"""() => {
  const out = [];
  const inline = el => {
    let s = "";
    el.childNodes.forEach(n => {
      if (n.nodeType === 3) { s += n.textContent.replace(/\s+/g, " "); return; }
      const t = n.tagName;
      if (t === "CODE") s += "`" + n.textContent + "`";
      else if (t === "STRONG" || t === "B") s += "**" + inline(n).trim() + "**";
      else if (t === "EM" || t === "I") s += "*" + inline(n).trim() + "*";
      else if (t === "BR") s += "\n";
      else if (t === "SPAN" && n.classList.contains("tag")) s += "`" + n.textContent.trim() + "` ";
      else if (t === "A") s += "[" + inline(n).trim() + "](" + n.getAttribute("href") + ")";
      else s += inline(n);
    });
    return s;
  };
  const table = tb => {
    const rows = [...tb.querySelectorAll("tr")].map(r =>
      [...r.children].map(c => inline(c).replace(/\n/g, " ").replace(/\s+/g, " ").trim()));
    if (!rows.length) return "";
    const head = rows[0], body = rows.slice(1);
    return ["| " + head.join(" | ") + " |",
            "| " + head.map(() => "---").join(" | ") + " |",
            ...body.map(r => "| " + r.join(" | ") + " |")].join("\n") + "\n";
  };
  const walk = (root, into) => {
    [...root.children].forEach(el => {
      const t = el.tagName;
      if (t === "H2") into.push("## " + inline(el).trim().replace(/^(\d\d)(?=\S)/, "$1 "));
      else if (t === "H3") into.push("**" + inline(el).trim() + "**");
      else if (t === "P") into.push(inline(el).trim());
      else if (t === "UL" || t === "OL")
        into.push([...el.children].map(li => "- " + inline(li).trim()).join("\n"));
      else if (t === "TABLE") into.push(table(el));
      else if (t === "DETAILS") {
        const sum = el.querySelector("summary");
        into.push("<details" + (el.open ? " open" : "") + ">\n<summary>" +
                  inline(sum).trim() + "</summary>\n");
        const inner = [];
        [...el.children].forEach(c => { if (c.tagName !== "SUMMARY") walk({children:[c]}, inner); });
        into.push(inner.join("\n\n"));
        into.push("</details>");
      }
      else if (t === "DIV" || t === "SECTION" || t === "HEADER" || t === "FOOTER") {
        if (el.classList.contains("controls")) return;
        if (el.classList.contains("answer")) {
          into.push("## The call");
          [...el.children].forEach(c => {
            if (c.classList && c.classList.contains("lbl")) return;
            into.push(c.classList && c.classList.contains("verdict")
              ? "**" + inline(c).trim() + "**" : inline(c).trim());
          });
          return;
        }
        if (el.classList.contains("pull")) {
          const lbl = el.querySelector(".lbl");
          const ps = [...el.querySelectorAll("p")].map(p => inline(p).trim());
          into.push("> **" + (lbl ? inline(lbl).trim() : "") + "**\n>\n" +
                    ps.map(x => "> " + x).join("\n>\n"));
          return;
        }
        walk(el, into);
      }
      else if (t === "DL") {
        const rows = [...el.querySelectorAll("div")].map(d =>
          "| " + inline(d.querySelector("dt")).trim() + " | " + inline(d.querySelector("dd")).trim() + " |");
        into.push(["| | |", "| --- | --- |", ...rows].join("\n"));
      }
      else if (t === "H1") into.push("# " + inline(el).trim());
    });
  };
  const parts = [];
  walk(document.querySelector(".sheet"), parts);
  return parts.filter(x => x && x.trim()).join("\n\n") + "\n";
}"""

src = pathlib.Path(sys.argv[1]); dst = pathlib.Path(sys.argv[2])
with sync_playwright() as pw:
    b = pw.chromium.launch(); pg = b.new_page()
    pg.goto(src.as_uri()); pg.wait_for_timeout(400)
    md = pg.evaluate(JS)
    b.close()
dst.write_text(md)
print(f"wrote {dst} ({len(md)} chars)")
