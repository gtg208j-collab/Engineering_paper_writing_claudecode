#!/usr/bin/env python3
"""
format_references.py — Convert references.bib to IEEE or Elsevier citation style

Usage:
    python scripts/format_references.py --style ieee
    python scripts/format_references.py --style elsevier
    python scripts/format_references.py --style ieee --input drafts/references.bib --output drafts/references_ieee.bib

Note: This script validates bib file structure and reports style-specific issues.
For full conversion, use a BibTeX processor (bibtex/biber) with the appropriate .bst/.cls.
"""
import re
import sys
import argparse
from pathlib import Path

IEEE_REQUIRED = ['author', 'title', 'journal', 'year', 'volume', 'pages']
ELSEVIER_REQUIRED = ['author', 'title', 'journal', 'year', 'volume', 'pages', 'doi']

def parse_bib_entries(content: str) -> list:
    entries = re.findall(r'@\w+\{[^@]+\}', content, re.DOTALL)
    return entries

def check_entry(entry: str, required_fields: list) -> list:
    missing = []
    for field in required_fields:
        if not re.search(rf'\b{field}\s*=', entry, re.IGNORECASE):
            missing.append(field)
    return missing

def main():
    parser = argparse.ArgumentParser(description='Validate/format references for IEEE or Elsevier')
    parser.add_argument('--style', choices=['ieee', 'elsevier'], required=True)
    parser.add_argument('--input', default='drafts/references.bib')
    parser.add_argument('--output', default=None)
    args = parser.parse_args()

    bib_file = Path(args.input)
    if not bib_file.exists():
        print(f"ERROR: {bib_file} not found.")
        sys.exit(1)

    content = bib_file.read_text(encoding='utf-8')
    entries = parse_bib_entries(content)
    required = IEEE_REQUIRED if args.style == 'ieee' else ELSEVIER_REQUIRED

    print(f"Style: {args.style.upper()}")
    print(f"Entries found: {len(entries)}")

    issues = 0
    for entry in entries:
        key_match = re.search(r'@\w+\{(\S+),', entry)
        key = key_match.group(1) if key_match else 'unknown'
        missing = check_entry(entry, required)
        if missing:
            print(f"  [WARN] {key}: missing fields: {', '.join(missing)}")
            issues += 1

    if args.style == 'ieee':
        print("\nIEEE style notes:")
        print("  - Use \\IEEEtran class with \\bibliographystyle{IEEEtran}")
        print("  - Citations appear as [1], [2], ...")
        print("  - Volume/number format: vol. X, no. Y, pp. Z–W")
    else:
        print("\nElsevier style notes:")
        print("  - Use elsarticle class with \\bibliographystyle{elsarticle-num} or -harv")
        print("  - Numeric: [1], [2] OR Author-year: (Smith, 2021)")
        print("  - DOI field strongly recommended")

    if issues == 0:
        print(f"\n✅ All {len(entries)} entries have required fields for {args.style.upper()}.")
    else:
        print(f"\n⚠️  {issues} entries have missing fields. Fix before submission.")

    if args.output:
        Path(args.output).write_text(content, encoding='utf-8')
        print(f"Output written to {args.output}")

if __name__ == '__main__':
    main()
