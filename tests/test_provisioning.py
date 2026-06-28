"""Cloud key-provisioning contract for plugin-cloudflare."""

from __future__ import annotations

import re
import tomllib
from pathlib import Path

from plugin_cloudflare import CloudflarePlugin
from plugin_cloudflare.client import CloudflareClient

PKG = Path(__file__).resolve().parents[1] / "plugin_cloudflare"


def test_client_uses_base_url_override() -> None:
    c = CloudflareClient("tok", "acct", base_url="https://gw.example/proxy/cloudflare")
    assert str(c._http.base_url).rstrip("/") == "https://gw.example/proxy/cloudflare"


def test_client_defaults_to_real_upstream() -> None:
    c = CloudflareClient("tok", "acct")
    assert str(c._http.base_url).startswith("https://api.cloudflare.com/client/v4")


def test_credential_slot_advertises_base_url_var() -> None:
    slots = CloudflarePlugin().credential_slots()
    assert slots[0].slug == "cloudflare"
    assert slots[0].env_key_var == "LUNA_CLOUDFLARE_API_KEY"
    assert slots[0].env_base_url_var == "LUNA_CLOUDFLARE_BASE_URL"


def test_manifest_and_code_versions_agree() -> None:
    toml_version = tomllib.loads((PKG / "luna-plugin.toml").read_text())["version"]
    code_version = re.search(r'version="([^"]+)"', (PKG / "__init__.py").read_text()).group(1)
    assert toml_version == code_version == CloudflarePlugin.manifest.version
