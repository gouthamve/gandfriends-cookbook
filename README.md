# gn friends cookbook

A plain-text cookbook of recipes from friends. Built with [Hugo](https://gohugo.io/), hosted on Cloudflare Pages.

## Local development

```sh
hugo server
```

Then open <http://localhost:1313>.

To build the production site:

```sh
hugo --minify
```

Output goes to `public/`.

## Adding a recipe

See [CONTRIBUTING.md](CONTRIBUTING.md). Short version:

1. Add a markdown file under `content/recipes/<section>/<your-recipe>.md`
2. If you're a new author, add `content/authors/<your-name>/_index.md` with a short bio
3. Open a pull request

## Deploy

Hosted on Cloudflare Pages via its native Git integration &mdash; CF clones the repo and builds on every push to `main`. No GitHub Action is involved in the deploy path; the `Lint recipes` workflow only gates PRs.

### Cloudflare Pages setup (one-time)

Workers &amp; Pages &rarr; Create application &rarr; Pages &rarr; **Connect to Git** &rarr; select this repo.

- **Project name**: `gnfriends-cookbook`
- **Production branch**: `main`
- **Framework preset**: None
- **Build command**: `hugo --minify --gc`
- **Build output directory**: `public`
- **Environment variable** (production): `HUGO_VERSION=0.161.1` &mdash; pin this; CF defaults to a stale Hugo
- **Preview deployments**: disabled (Settings &rarr; Builds &amp; deployments &rarr; Preview deployments &rarr; *None*)
- **Custom domain**: `cookbook.gouthamve.dev` (Custom domains &rarr; Add)

The `HUGO_VERSION` must match the version pinned in `.github/workflows/lint-recipes.yml` so a build that passes CI also passes on CF.

## Structure

- `content/recipes/<section>/*.md` &mdash; recipes, organised by meal/course
- `content/authors/<name>/_index.md` &mdash; author profile (becomes the `/authors/<name>/` page)
- `layouts/` &mdash; bespoke minimal templates, no theme
- `static/css/main.css` &mdash; screen + print styles
- `/index/` &mdash; back-of-book style index across ingredients, cuisines, and tags
