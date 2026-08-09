# Visual layout notes

These notes implement HNU-D-29 to HNU-D-35. Treat the Rule PDF as controlling;
the Sample PDF is a visual aid only.

## Page and typography

| Element | Required setting |
| --- | --- |
| Page | A4 (210 × 297 mm); top/bottom 25 mm; left/right 30 mm; header/footer 10 mm |
| Line spacing | 20 pt |
| Chapter title | 18 pt 小二号黑体; before 0.5 line, after 1.5 lines |
| Level 1 | 15 pt 小三号黑体; 12 pt before/after |
| Level 2 | 14 pt 四号黑体; 6 pt before/after |
| Level 3 | 12 pt 小四号黑体; 6 pt before/after |
| Body | 12 pt 小四号宋体; English/digits Times New Roman; first line 2 characters; justified |
| Table number/title | 10.5 pt 五号黑体; English Times New Roman; single-rule table, top/bottom 1.5 pt and middle 0.75 pt |
| Header | 9 pt 小五号宋体 |
| Footer/page number | 9 pt 小五号 Times New Roman |
| Footnote | 9 pt 小五号宋体; English/digits Times New Roman; justified; single spaced |

Source: Rule PDF p. 18, §§4.1–4.2. Sample PDF pp. 9–11 illustrates the
rendered result.

## Headers and pagination

- Begin headers at the Chinese abstract page, centered at the top. Put a 15 pt
  thick-thin double rule below it, thick rule above. **Ambiguity:** the Rule PDF
  literally says 15 pt, while the supplied rendered sample visually corresponds
  to approximately 1.5 pt upper and 0.75 pt lower rules. Treat 1.5/0.75 pt as a
  sample-informed implementation target, not a silent correction; verify the
  rendered output and obtain clarification if it differs from the current HNU
  template.
- Use the prescribed dissertation label on odd pages and the thesis title on even
  pages. Use neutral placeholders during drafting; use the exact authorized title
  only in the private deliverable.
- Number Chinese abstract through final contents page with centered Roman numerals.
  Start Arabic numbering at the body, centered at the foot of the page.

Source: Rule PDF pp. 18–19, §4.3; Sample PDF pp. 9–11.

## Visual inspection checklist

- Confirm each body chapter begins on a new page and no hierarchy heading is the
  last line of a page.
- Inspect two odd/even header pairs, the Roman-to-Arabic transition, and a
  one-sided-start blank verso where applicable.
- Check a long equation, one table, one multi-part figure, one figure near a page
  boundary, a reference-list continuation, and the final end-matter ordering.
- Keep a table caption above its table; keep a figure and its below-image caption
  as one unit without applying `keep-with-next` to the figure caption itself.
- Do not treat the sample’s factual committee-list record as a scholarly three-line
  table. Do not render sample degree or attachment labels literally in a doctoral
  dissertation.
- For printing, follow the source-specific one-sided or duplex order; do not infer
  blank-verso handling from a word processor's ordinary duplex setting.

Source: Rule PDF pp. 13, 19–20, §§3.14.3, 4.8, 4.10.
