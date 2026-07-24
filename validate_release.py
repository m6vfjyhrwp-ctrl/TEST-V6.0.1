from pathlib import Path
import hashlib
import json
import re
import subprocess

root = Path(__file__).resolve().parents[1]
QA_VERSION = "6.0.1-qa.1"
PRODUCTION_VERSION = "6.0.1"

for name in ("VERSION.json", "manifest.webmanifest", "release-identity.json", "integrity-manifest.json"):
    json.loads((root / name).read_text(encoding="utf-8"))

html = (root / "index.html").read_text(encoding="utf-8")
ids = re.findall(r'\bid="([^"]+)"', html)
assert len(ids) == len(set(ids)), "duplicate HTML IDs"

app = (root / "app.js").read_text(encoding="utf-8")
assert 'const STORE = "acbf-companion-m3"' in app, "storage key changed"
assert 'const APP_VERSION = RELEASE.version || "6.0.1"' in app, "app version fallback mismatch"

production = json.loads((root / "VERSION.json").read_text(encoding="utf-8"))
qa_identity = json.loads((root / "release-identity.json").read_text(encoding="utf-8"))
manifest = json.loads((root / "integrity-manifest.json").read_text(encoding="utf-8"))
package = json.loads((root / "package.json").read_text(encoding="utf-8"))

assert production["version"] == PRODUCTION_VERSION, "embedded production version mismatch"
assert production["releaseChannel"] == "production", "embedded production channel mismatch"
assert production["databaseVersion"] == 9 and production["userDataVersion"] == 3
assert qa_identity["version"] == QA_VERSION, "QA wrapper version mismatch"
assert qa_identity["releaseChannel"] == "qa", "QA wrapper channel mismatch"
assert package["version"] == QA_VERSION, "package QA version mismatch"
assert manifest["releaseVersion"] == QA_VERSION, "integrity manifest QA version mismatch"
assert manifest["buildId"] == qa_identity["buildId"], "QA build ID mismatch"
assert qa_identity["databaseVersion"] == production["databaseVersion"]
assert qa_identity["userDataSchemaVersion"] == production["userDataVersion"]

node = r'''const fs=require('fs'),vm=require('vm');const sandbox={window:{}};vm.createContext(sandbox);vm.runInContext(fs.readFileSync('database.js','utf8'),sandbox);const rows=sandbox.window.ACBF_LOCATIONS;const ids=rows.map(x=>x.id);if(rows.length!==104||new Set(ids).size!==104)process.exit(2);console.log(rows.length);'''
subprocess.run(["node", "-e", node], cwd=root, check=True, capture_output=True, text=True)

for item in manifest["files"]:
    path = root / item["path"]
    assert path.is_file(), f'missing {item["path"]}'
    assert path.stat().st_size == item["size"], f'size mismatch {item["path"]}'
    assert hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], f'stale hash {item["path"]}'

sw = (root / "service-worker.js").read_text(encoding="utf-8")
assert f'const CACHE="acbf-v{QA_VERSION}"' in sw, "service worker QA cache mismatch"
for asset in re.findall(r'"(\./[^"?]+)"', sw.split("];", 1)[0]):
    if asset == "./":
        continue
    target = root / asset[2:]
    assert target.exists(), f"service worker asset missing: {asset}"

print(f"release validation passed: QA {QA_VERSION} wrapping production {PRODUCTION_VERSION}")
