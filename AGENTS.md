# Repository Instructions

## Publication Updates

When updating `content/publication`, follow `PUBLICATION_UPDATE_WORKFLOW.md`.

In short:

- Create one folder per paper named `first-author-last-name-year-venueabbr`.
- Put exactly two content files in each new publication folder: `index.md` and `cite.bib`.
- Update the paper title, author names, publication year, and venue information by matching existing entry formats.
- Add entries to `content/publication/_index.md` `publicationUrls` only when an original paper URL currently exists.
- Verify with `hugo --renderToMemory` before reporting completion.

## People Page Updates

- The `Former Students/Researchers` table sorts entries with an ending `MM/YYYY` in `period` from newest to oldest.
- Use `MM/YYYY-MM/YYYY` for `period` whenever both months are known.
- Entries without an ending month stay after month-specific entries and use `former_weight` for their relative order.
