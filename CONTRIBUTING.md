# Contributing a recipe

Thanks for sharing! Here's the short version.

## 1. Pick a section

Choose one of: `breakfast`, `starters`, `mains`, `sides`, `desserts`, `drinks`, `snacks`.

## 2. Create the recipe file

Path: `content/recipes/<section>/<slug>.md` (slug is lowercase, dashes between words).

Use this template &mdash; copy and fill in:

```yaml
---
title: "Your recipe name"
authors: [your-name]            # lowercase, dashes. Must match content/authors/<your-name>/_index.md
cuisines: [italian]             # one or more, free-form
servings: "Serves 4"
prep_time: "15 min"
cook_time: "30 min"
tags: [pasta, weeknight]        # optional, free-form
ingredient_keys:                # clean names for the back-of-book Index, one per ingredient
  - pasta
  - olive oil
  - onion
ingredients:                    # full lines shown on the recipe page, with quantities
  - 200g pasta
  - 2 tbsp olive oil
  - 1 onion, diced
---

## Instructions

1. First step.
2. Second step.

## Notes

Anything optional &mdash; substitutions, make-ahead tips.
```

### Field reference

| Field | Required | Notes |
|---|---|---|
| `title` | yes | Display name of the recipe |
| `authors` | yes | List of author slugs |
| `cuisines` | yes | List of cuisines, free-form |
| `servings` | yes | Free text, e.g. `"Serves 4"` or `"Makes 12 cookies"` |
| `prep_time` | yes | Free text. Use `"N min"` for the home total-time display |
| `cook_time` | yes | Free text. Use `"N min"` for the home total-time display |
| `tags` | no | List of free-form tags |
| `ingredient_keys` | yes | Clean ingredient names (no quantities). Used for the back-of-book index. Lowercase, e.g. `olive oil`, `onion`, `tomatoes` |
| `ingredients` | yes | Full lines with quantities, shown on the recipe page |

## 3. If you're a new author

Add `content/authors/<your-name>/_index.md`:

```yaml
---
title: "Your Name"
---

One or two sentences about yourself. Optional.
```

## 4. Open a pull request

The CI will check that your frontmatter has the required fields. Cloudflare Pages will give you a preview URL on your PR &mdash; click through and check your recipe renders, prints, and shows up in search.

## Tips

- **Ingredients first**: the template puts the ingredients block before instructions for easy scanning while cooking.
- **Markdown ordered lists** in `## Instructions` render as numbered steps.
- **Avoid images** &mdash; this is a text-only cookbook.
- **Print preview** (Cmd+P) is a good way to sanity-check that your recipe reads cleanly on paper.
