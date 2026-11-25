# Former Students Period Sorting Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Automatically order former students with explicit ending months from newest to oldest while preserving the existing order of year-only entries.

**Architecture:** The People table shortcode will convert each former-student page into a record containing the page and one numeric sort key. Explicit `MM/YYYY` endings receive a date-derived key; entries without a month receive a fallback key derived from `former_weight`. One ascending sort then produces the required table order.

**Tech Stack:** Hugo 0.152 templates, Go template functions, Markdown/YAML author profiles, shell-based rendered HTML verification.

## Global Constraints

- Parse dates only when the final `period` component is exactly `MM/YYYY` after trimming spaces.
- Sort explicit ending months in descending chronological order.
- Use `former_weight` to break same-month ties.
- Place entries without an explicit ending month after all month-specific entries and preserve their existing `former_weight` order.
- Keep Darren Chai Xin Lun out of the People page without deleting the author profile.
- Display Han Zhou in `Former Students/Researchers` with the requested Period, Topic, and To values.

---

### Task 1: Implement Period-Based Former Student Sorting

**Files:**
- Modify: `layouts/shortcodes/people-table.html:1-35`
- Modify: `content/authors/Darren Chai Xin Lun/_index.md:35-38`
- Modify: `content/authors/han-zhou/_index.md:1-43`
- Modify: `AGENTS.md`

**Interfaces:**
- Consumes: author front matter fields `user_groups`, `period`, `former_weight`, `former_name`, `topic`, and `to`.
- Produces: a sorted `$rows` slice whose records expose `.person` for table rendering and `.sort_key` for ordering.

- [x] **Step 1: Run the rendered-order check and verify the current template fails**

```bash
people_build_dir=$(mktemp -d /tmp/tump-people-red-XXXXXX)
hugo --destination "$people_build_dir" >/dev/null
han_line=$(rg -n '<td>Han Zhou</td>' "$people_build_dir/people/index.html" | cut -d: -f1)
li_line=$(rg -n 'Li Zhou \(Visiting Professor, SWU, China\)' "$people_build_dir/people/index.html" | cut -d: -f1)
test "$han_line" -lt "$li_line"
```

Expected: the final `test` exits non-zero because Li Zhou currently appears above Han Zhou.

- [x] **Step 2: Replace manual former-student sorting with a composite period key**

Replace the sorting branch and range setup at the top of `layouts/shortcodes/people-table.html` with:

```go-html-template
{{- $group := .Get "group" | default "" -}}
{{- $people := where site.Pages "Section" "authors" -}}
{{- if $group -}}
  {{- $people = where $people ".Params.user_groups" "intersect" (slice $group) -}}
{{- end -}}
{{- $rows := slice -}}
{{- if eq $group "Former Students/Researchers" -}}
  {{- range $people -}}
    {{- $person := . -}}
    {{- $weight := int ($person.Params.former_weight | default 999) -}}
    {{- $sortKey := add 1000000000 $weight -}}
    {{- $period := strings.TrimSpace ($person.Params.period | default "") -}}
    {{- $matches := findRE `[0-9]{2}/[0-9]{4}$` $period -}}
    {{- if gt (len $matches) 0 -}}
      {{- $endParts := split (index $matches 0) "/" -}}
      {{- $month := int (replaceRE `^0` "" (index $endParts 0)) -}}
      {{- $year := int (index $endParts 1) -}}
      {{- $yearMonth := add (mul $year 100) $month -}}
      {{- $sortKey = add (mul (sub 999999 $yearMonth) 1000) $weight -}}
    {{- end -}}
    {{- $rows = $rows | append (dict "person" $person "sort_key" $sortKey) -}}
  {{- end -}}
  {{- $rows = sort $rows "sort_key" "asc" -}}
{{- else -}}
  {{- $people = sort $people "Params.weight" "asc" -}}
  {{- range $people -}}
    {{- $rows = $rows | append (dict "person" .) -}}
  {{- end -}}
{{- end -}}
```

Change the table body loop from `range $people` to:

```go-html-template
{{- range $rows -}}
{{- $person := .person -}}
<tr>
  <td>{{ $person.Params.former_name | default $person.Title }}</td>
  <td>{{ $person.Params.period | default "" }}</td>
  <td>{{ $person.Params.topic | default "" }}</td>
  <td>{{ $person.Params.to | default "" }}</td>
</tr>
{{- end -}}
```

- [x] **Step 3: Record the durable People-page rule in repository instructions**

Append this section to `AGENTS.md`:

```markdown
## People Page Updates

- The `Former Students/Researchers` table sorts entries with an ending `MM/YYYY` in `period` from newest to oldest.
- Use `MM/YYYY-MM/YYYY` for `period` whenever both months are known.
- Entries without an ending month stay after month-specific entries and use `former_weight` for their relative order.
```

- [x] **Step 4: Run the full build and rendered-page verification**

```bash
hugo --renderToMemory
git diff --check
people_build_dir=$(mktemp -d /tmp/tump-people-green-XXXXXX)
hugo --destination "$people_build_dir" >/dev/null
people_html="$people_build_dir/people/index.html"
! rg -q 'Darren Chai Xin Lun' "$people_html"
han_line=$(rg -n '<td>Han Zhou</td>' "$people_html" | cut -d: -f1)
li_line=$(rg -n 'Li Zhou \(Visiting Professor, SWU, China\)' "$people_html" | cut -d: -f1)
huigui_line=$(rg -n 'Huigui Yan \(Visiting PhD, YSU, China\)' "$people_html" | cut -d: -f1)
huizhong_line=$(rg -n 'Huizhong Guo \(Visiting PhD, ZJU, China\)' "$people_html" | cut -d: -f1)
test "$han_line" -lt "$li_line"
test "$li_line" -lt "$huigui_line"
test "$huigui_line" -lt "$huizhong_line"
rg -q '<td>02/2026-11/2026</td>' "$people_html"
rg -q '<td>Poisoning Attack in Sequential Recommendation</td>' "$people_html"
rg -q '<td>PHD, SUFE, CN</td>' "$people_html"
```

Expected: both Hugo builds exit zero; Darren is absent; the explicit-month order starts with Han Zhou, Li Zhou, Huigui Yan, and Huizhong Guo; Han's requested fields are present.

- [ ] **Step 5: Commit the implementation**

```bash
git add AGENTS.md layouts/shortcodes/people-table.html \
  'content/authors/Darren Chai Xin Lun/_index.md' \
  content/authors/han-zhou/_index.md \
  docs/superpowers/plans/2026-11-25-former-students-period-sorting.md
git commit -m "Sort former students by ending period"
```
