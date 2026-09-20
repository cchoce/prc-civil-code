# PRC Civil Code Skill

An Agent Skill generated from the *Civil Code of the People's Republic of China* (《中华人民共和国民法典》) with [book-to-skill](https://github.com/virgiliojr94/book-to-skill).

It organizes the Code into a reusable legal-reasoning toolkit for issue spotting, claim-basis analysis, article navigation, and systematic study. The content is synthesized structure and analysis rather than a reproduction of the complete statutory text. For litigation, contract review, or other high-stakes reliance, verify exact wording and current judicial interpretations against an authoritative source.

## Install

```bash
npx skills add https://github.com/cchoce/prc-civil-code --skill prc-civil-code
```

## Contents

- `SKILL.md` — entry point, core analysis models, and topic routing
- `chapters/` — structured guides for all seven Books plus system-level application
- `references/article-index.md` — hierarchy and article-range index
- `references/article-map.json` — machine-readable mapping for all 1,260 articles
- `glossary.md` — key civil-law concepts
- `patterns.md` — reusable legal-analysis patterns
- `cheatsheet.md` — compact decision guide
- `scripts/locate_article.py` — article hierarchy locator

## Scope

This skill covers the Civil Code itself. It does not automatically incorporate judicial interpretations, guiding cases, local rules, or other statutes. Check current authoritative sources whenever those materials may affect the answer.
