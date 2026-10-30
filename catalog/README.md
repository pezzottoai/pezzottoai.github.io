# Catalog

`clones.json` is the whole stall: a JSON array of entries, one per clone. The site at
https://pezzottoai.github.io renders it directly. No build step.

## Entry

```json
{
  "id": "example-notes",
  "target":  { "name": "Original App", "url": "https://original.example", "category": "notes" },
  "clone":   { "name": "Pezzotto Notes", "repo": "https://github.com/someone/pezzotto-notes",
               "license": "MIT", "stack": ["sveltekit", "sqlite"] },
  "coverage": ["editor", "sync", "sharing"],
  "missing":  ["mobile app", "offline"],
  "status":   "alive",
  "grade":    "B",
  "vibecoded_with": "claude-code",
  "added":    "2026-10-30",
  "checked":  "2026-10-30",
  "notes":    "Single-user only; sync is a cron job and a prayer."
}
```

| field | meaning |
|---|---|
| `id` | kebab-case, unique, stable |
| `target` | the closed-source original: `name`, `url`, `category` (free text, lowercase) |
| `clone` | `name`, `repo` (git URL), `license` (SPDX id), `stack` (lowercase tags) |
| `coverage` / `missing` | features of the original that the clone has / lacks |
| `status` | `alive` (commit in last 90 days), `stale` (90 days to 1 year), `abandoned` |
| `grade` | pezzotto grade A–D, see below |
| `vibecoded_with` | agent or tool the clone was mostly built with, if known |
| `added` / `checked` | ISO dates: when the entry was added, when the clone was last verified |
| `notes` | one or two honest sentences |

## Grade

How far away does it still fool you?

- **A** indistinguishable at arm's length
- **B** convincing from three metres: core flows match, details drift
- **C** recognisable from across the street: right shape, half the features
- **D** you'd have to be told

Grade is about looks and behaviour versus the original. It is not a code-quality score.

## Rules

- The original must be closed source. The clone must be open source (any OSI license).
- Someone must have actually run the clone before it goes in.
- Dead clones are marked `abandoned`, never deleted. The graveyard is part of the record.
- Catalog data is CC0.
