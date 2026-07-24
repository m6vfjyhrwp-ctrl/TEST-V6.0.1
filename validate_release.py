from pathlib import Path
import json,re,hashlib,subprocess,tempfile
root=Path(__file__).resolve().parents[1]
for name in ('VERSION.json','manifest.webmanifest','release-identity.json','integrity-manifest.json'):
    json.loads((root/name).read_text())
html=(root/'index.html').read_text()
ids=re.findall(r'\bid="([^"]+)"',html)
assert len(ids)==len(set(ids)), 'duplicate HTML IDs'
app=(root/'app.js').read_text()
assert 'const STORE = "acbf-companion-m3"' in app, 'storage key changed'
assert 'const APP_VERSION = RELEASE.version || "6.0.1"' in app, 'app version mismatch'
version=json.loads((root/'VERSION.json').read_text())
assert version['databaseVersion']==9 and version['userDataVersion']==3
node="""const fs=require('fs'),vm=require('vm');const sandbox={window:{}};vm.createContext(sandbox);vm.runInContext(fs.readFileSync('database.js','utf8'),sandbox);const rows=sandbox.window.ACBF_LOCATIONS;const ids=rows.map(x=>x.id);if(rows.length!==104||new Set(ids).size!==104)process.exit(2);console.log(rows.length);"""
subprocess.run(['node','-e',node],cwd=root,check=True,capture_output=True,text=True)
manifest=json.loads((root/'integrity-manifest.json').read_text())
assert manifest['releaseVersion']=='6.0.1'
for item in manifest['files']:
    p=root/item['path']; assert p.is_file(), f'missing {item["path"]}'
    assert p.stat().st_size==item['size'], f'size mismatch {item["path"]}'
    assert hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256'], f'stale hash {item["path"]}'
sw=(root/'service-worker.js').read_text()
for asset in re.findall(r'"(\./[^"?]+)"',sw.split('];',1)[0]):
    target=root/(asset[2:] or 'index.html')
    if asset=='./': continue
    assert target.exists(), f'service worker asset missing: {asset}'
print('release validation passed')
