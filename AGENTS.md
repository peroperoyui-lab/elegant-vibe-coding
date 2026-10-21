# Elegant Vibe Coding · contributor instructions

This repository is a Chinese field guide for people directing coding agents.
This repository contains general documentation and independently authored fictional examples.

## Editorial contract

- Write clear Chinese. Introduce English terms with a concrete Chinese explanation.
- Connect each recommendation to a task, an example instruction and observable evidence.
- Distinguish a standard, a vendor-specific behaviour, an editorial recommendation and an illustrative example.
- Verify changing commands, tool features and technical thresholds against primary documentation. Record the access date and link near the claim.
- Use independently invented project identities and sample data, or clearly cited public sources. Private conversations and unreleased projects are not source material for public examples. Publishing project names, architecture, plans, research topics or work history requires explicit permission to disclose them publicly. A teaching-example label does not grant that permission.
- Keep established files and navigation coherent. Add focused chapters instead of duplicating entire sections.
- Use original diagrams. Explain their meaning in adjacent text. Include SVG title/description and readable contrast.
- Code examples must say whether they are executable, pseudocode or incomplete sketches. Identify their prerequisites and side effects.
- Reports must distinguish passed checks, unexecuted checks and platform-specific work that remains.

## Repository workflow

1. Read `README.md`, `CONTRIBUTING.md` and the chapter being changed.
2. Edit Markdown or the original example/asset. `reader/index.html` is generated.
3. Run `python3 scripts/check_docs.py`. Run `npm run build:reader` after content changes if the declared build dependency is installed.
4. For reader or demo changes, open the actual page and verify the changed interaction at desktop and narrow viewport widths.
5. Summarize the useful change, evidence and any remaining limitation. Follow the user's authorization for Git delivery.

No paid API, credentials or remote service is needed to read this guide.
