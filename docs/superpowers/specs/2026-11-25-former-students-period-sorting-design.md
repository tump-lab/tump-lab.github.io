# Former Students/Researchers Period Sorting Design

## Goal

Sort the `Former Students/Researchers` table by the ending month in each
member's `period` field. A later ending month must appear above an earlier one.

## Sorting Rules

1. Parse an ending value only when the final component of `period` uses the
   `MM/YYYY` format.
2. Convert that value to a numeric `YYYYMM` key and sort these entries in
   descending order.
3. Entries whose ending value has no explicit month, such as `2025` or `2021`,
   are not compared by date. They remain after month-specific entries and keep
   their existing `former_weight` order.
4. If two month-specific entries have the same ending month, use
   `former_weight` as the tie-breaker.

## Implementation

Update `layouts/shortcodes/people-table.html` only in the
`Former Students/Researchers` branch. Build sortable records containing the
author page and one numeric sorting key. For an explicit ending month, calculate
the key as `(999999 - YYYYMM) * 1000 + former_weight`; later dates therefore
have smaller keys, with `former_weight` breaking same-month ties. For an entry
without an explicit ending month, calculate the key as
`1000000000 + former_weight`, which places it after all month-specific entries
while preserving the existing fallback order. Sort the records once in
ascending key order.

The author profile fields remain unchanged apart from the requested Darren Chai
Xin Lun and Han Zhou membership updates already in progress.

## Verification

- Run `hugo --renderToMemory`.
- Render the site to a temporary directory.
- Confirm Darren Chai Xin Lun is absent from the People page.
- Confirm Han Zhou appears above Li Zhou.
- Confirm the month-specific sequence begins with `11/2026`, `10/2026`,
  `08/2026`, and `04/2026`.
- Confirm year-only entries retain their existing relative order.
