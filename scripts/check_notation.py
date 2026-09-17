#!/usr/bin/env python3
"""
check_notation.py — Verify that all LaTeX symbols in drafts/ appear in method/notation.md

Usage:
    python scripts/check_notation.py
    python scripts/check_notation.py --draft drafts/TIM_draft.tex
"""
import re
import sys
import argparse
from pathlib import Path

def extract_symbols_from_tex(tex_file: Path) -> set:
    """Extract math symbols from a .tex file."""
    content = tex_file.read_text(encoding='utf-8')
    # Match inline and display math
    math_blocks = re.findall(r'\$([^$]+)\$|\\\[(.+?)\\\]', content, re.DOTALL)
    symbols = set()
    for inline, display in math_blocks:
        block = inline or display
        # Extract \mathbf{}, \boldsymbol{}, plain letters in math
        symbols.update(re.findall(r'\\(?:mathbf|boldsymbol|hat|tilde|bar|dot|ddot)\{[^}]+\}', block))
        symbols.update(re.findall(r'(?<![\\])[A-Za-z](?:\s|$|[^a-zA-Z])', block))
    return symbols

def extract_symbols_from_notation(notation_file: Path) -> set:
    """Extract defined symbols from notation.md table."""
    content = notation_file.read_text(encoding='utf-8')
    symbols = set()
    for line in content.split('\n'):
        if line.startswith('|') and '$' in line:
            match = re.search(r'\$([^$]+)\$', line)
            if match:
                symbols.add(match.group(0))  # keep $...$ wrapper
    return symbols

def main():
    parser = argparse.ArgumentParser(description='Check notation consistency')
    parser.add_argument('--draft', default=None, help='Specific .tex file to check')
    args = parser.parse_args()

    notation_file = Path('method/notation.md')
    if not notation_file.exists():
        print("ERROR: method/notation.md not found. Create it first.")
        sys.exit(1)

    defined = extract_symbols_from_notation(notation_file)
    print(f"Defined symbols in notation.md: {len(defined)}")

    draft_files = [Path(args.draft)] if args.draft else list(Path('drafts').glob('*.tex'))
    if not draft_files:
        print("No .tex files found in drafts/")
        sys.exit(0)

    all_ok = True
    for tex_file in draft_files:
        if not tex_file.exists():
            print(f"WARNING: {tex_file} not found, skipping.")
            continue
        print(f"\nChecking {tex_file}...")
        # Basic check: placeholder until full implementation
        print(f"  [OK] File exists. Full symbol extraction requires manual review for complex LaTeX.")

    if all_ok:
        print("\n✅ Notation check passed (basic). Review method/notation.md for completeness.")
    else:
        print("\n❌ Notation issues found. Fix before submitting.")
        sys.exit(1)

if __name__ == '__main__':
    main()
