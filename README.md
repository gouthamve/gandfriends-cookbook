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

Hosted on Cloudflare via the [Workers + Static Assets](https://gohugo.io/host-and-deploy/host-on-cloudflare/) flow that the Hugo project officially documents. CF clones the repo, runs `build.sh`, and serves `public/`. No GitHub Action is involved in the deploy path; the `Lint recipes` workflow only gates PRs.

The two files that drive the deploy live at the repo root:

- `wrangler.toml` &mdash; tells CF the build command (`./build.sh`) and the assets directory (`./public`)
- `build.sh` &mdash; downloads Hugo at the pinned version and runs `hugo build --gc --minify`. The Hugo version is pinned in two places (`build.sh` and `.github/workflows/lint-recipes.yml`), both tagged with `# renovate: datasource=github-releases depName=gohugoio/hugo` so Renovate bumps them together in one PR (config: `renovate.json`)

### Cloudflare dashboard (one-time)

Workers &amp; Pages &rarr; **Import a repository** &rarr; select this repo.

- **Project name**: `gnfriends-cookbook` (must match `name` in `wrangler.toml`)
- **Production branch**: `main`
- **Build command**: leave blank &mdash; `wrangler.toml` supplies it

Click **Create and deploy**.

Then, in the new project:

- **Preview deployments**: disable (Settings &rarr; Builds &amp; deployments &rarr; Preview deployments &rarr; *None*)
- **Custom domain**: add `cookbook.gouthamve.dev` (Custom domains &rarr; Add)

## Structure

- `content/recipes/<section>/*.md` &mdash; recipes, organised by meal/course
- `content/authors/<name>/_index.md` &mdash; author profile (becomes the `/authors/<name>/` page)
- `layouts/` &mdash; bespoke minimal templates, no theme
- `static/css/main.css` &mdash; screen + print styles
- `/index/` &mdash; back-of-book style index across ingredients, cuisines, and tags
