# plugin-cloudflare

Cloudflare infrastructure management for [Luna](https://github.com/huemorgan/luna):
DNS zones and records, CDN cache purge, Workers, Workers KV, and Pages.

This is a **Luna plugin** built against the Luna Plugin SDK (`luna_sdk`) v0. It
imports nothing from `luna.*` — only the stable SDK surface (including
`SkillDef` and `get_current_user` for route auth) — so it installs from the Luna
marketplace and runs without being part of Luna core.

## Install

In Luna: **Marketplace → Luna Official → plugin-cloudflare → Install**. Then
open **Settings → Connectors → Cloudflare**, paste a Cloudflare API token + your
account ID, and connect. Ships OFF by default.

## What it does

15 skill-gated tools across five skills:

| Skill | Tools |
|---|---|
| `cloudflare-dns` | list zones, list/create/update/delete DNS records |
| `cloudflare-cache` | purge cache (everything or by URL) |
| `cloudflare-workers` | list / read / deploy Worker scripts |
| `cloudflare-kv` | list namespaces, get/put/delete KV keys |
| `cloudflare-pages` | list / inspect Pages projects |

The API token + account ID are stored in Luna's vault; auth-gated REST routes
live under `/api/p/plugin-cloudflare/*` (including a webhook receiver).

## Settings UI

Served as a themed **iframe** from the plugin's own managed directory
(`interface/webui/settings/index.html`) — ships its own UI without compiling
into Luna core's bundle. Crash-isolated and React-version immune.

## Layout

```
plugin_cloudflare/
  __init__.py        # the plugin (luna_sdk only) — tools + skills + settings tab
  client.py          # CloudflareClient (pure httpx)
  routes.py          # REST routes (SDK auth) + webhook + iframe UI serving
  interface/webui/settings/index.html   # the iframe settings page
  luna-plugin.toml   # the data manifest the marketplace reads
```

## License

MIT — see [LICENSE](./LICENSE).
