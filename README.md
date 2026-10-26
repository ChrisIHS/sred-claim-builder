# SR&ED Claim Builder

Guided web process from Impact Technical Advisors: set up an SR&ED evidence system, capture evidence per project, and draft the T661 and Alberta / BC / Saskatchewan documentation.

- `src/index.src.html` is the source (single page, no dependencies).
- `python3 build.py` embeds the logo and writes `site/index.html`.
- Deployed from `site/` (see `vercel.json`). No build step is needed on Vercel because `site/index.html` is committed.

Data stays in the user's browser (localStorage) unless they download a `.sred.json` file.
