# Publication Update Workflow

When adding papers to `content/publication`, follow this workflow every time.

## Inputs

Collect the following information for each paper:

- Paper title
- Author list, in order
- Publication year
- Venue full name and venue abbreviation
- Original paper URL, if one currently exists

If a reliable original paper URL cannot be found, do not add a URL placeholder.

## Step 1: Create The Publication Folder

Create one folder per paper under `content/publication`.

Folder naming format:

```text
last-name-year-venueabbr
```

Rules:

- Use the first author's last name.
- Use the publication year.
- Use the venue abbreviation in lowercase.
- Use hyphens between parts.
- Follow existing folders in `content/publication` when a venue has an established naming style.
- Add an extra disambiguating suffix only when needed to avoid collisions.

Examples:

```text
zhou-2026-recsys
wang-2026-acmmm
sun-2024-sigir-llm
```

## Step 2: Add The Two Required Files

Each publication folder must contain exactly these content files:

```text
index.md
cite.bib
```

Use nearby existing publication entries as templates.

For `index.md`, update at least:

- `title`
- `authors`
- `date`
- `publishDate`
- `publication_types`
- `publication`

For `cite.bib`, update at least:

- BibTeX key
- `author`
- `booktitle` or `journal`
- `title`
- `year`

For conference papers, use:

```yaml
publication_types:
- paper-conference
```

and:

```bibtex
@inproceedings{...}
```

For journal papers, use the existing journal-entry pattern in the repository.

## Step 3: Add Original Paper URLs

Open `content/publication/_index.md` and update the `publicationUrls` object.

Add a URL only when the current original paper link is available. If no original paper link exists yet, leave the paper out of `publicationUrls`.

Use a key that matches the folder name after removing hyphens and underscores, because the page script normalizes folder names this way.

Example:

```text
content/publication/wang-2026-acmmm/
```

maps to:

```javascript
"wang2026acmmm": "https://arxiv.org/abs/2605.15203"
```

## Step 4: Verify

Before calling the update complete:

1. Check the new folder contains `index.md` and `cite.bib`.
2. Check the BibTeX key matches the normalized folder naming style.
3. Check `publicationUrls` only includes papers with working original links.
4. Run a Hugo build check:

```bash
hugo --renderToMemory
```

If the working tree has unrelated user edits, do not stage, revert, or commit those unrelated files.
