#!/usr/bin/env bash
# Builds the cookbook on Cloudflare Workers Builds.
# Adapted from https://gohugo.io/host-and-deploy/host-on-cloudflare/
# Trimmed to just Hugo: this site has no SCSS, no Hugo modules, no JS.

set -euo pipefail

build_temp_dir=""
cleanup() {
  if [[ -n "${build_temp_dir:-}" && -d "${build_temp_dir}" ]]; then
    rm -rf "${build_temp_dir}"
  fi
}
trap cleanup EXIT SIGINT SIGTERM

main() {
  # renovate: datasource=github-releases depName=gohugoio/hugo
  HUGO_VERSION=0.161.1

  build_temp_dir=$(mktemp -d)
  pushd "${build_temp_dir}" > /dev/null

  mkdir -p "${HOME}/.local/hugo"

  echo "Installing Hugo ${HUGO_VERSION}..."
  curl -sLJO "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_linux-amd64.tar.gz"
  tar -C "${HOME}/.local/hugo" -xf "hugo_${HUGO_VERSION}_linux-amd64.tar.gz"
  export PATH="${HOME}/.local/hugo:${PATH}"

  popd > /dev/null

  echo "Hugo: $(hugo version)"

  git config core.quotepath false
  if [ "$(git rev-parse --is-shallow-repository)" = "true" ]; then
    git fetch --unshallow
  fi

  echo "Building the site..."
  hugo build --gc --minify
}

main "$@"
