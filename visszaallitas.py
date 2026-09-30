#!/usr/bin/env python3
import hashlib, json, shutil, sys, uuid
from pathlib import Path
from urllib.request import Request, urlopen

folder = Path(sys.argv[2] if len(sys.argv) > 2 else '.').resolve()
folder.mkdir(parents=True, exist_ok=True)
manifest = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
def digest(p):
    h = hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda: f.read(4194304), b''): h.update(b)
    return h.hexdigest()
for part in manifest['parts']:
    p = folder / part['name']
    if p.name != part['name']: raise SystemExit('Érvénytelen darabnév.')
    if not p.exists():
        temp = folder / (p.name + '.letoltes-' + uuid.uuid4().hex[:12])
        print('Letöltés:', p.name, flush=True)
        req = Request(part['url'], headers={'User-Agent': 'Hidasz-restore/1'})
        with urlopen(req, timeout=120) as source, temp.open('xb') as target:
            shutil.copyfileobj(source, target, 4194304)
        if temp.stat().st_size != part['bytes'] or digest(temp) != part['sha256']:
            raise SystemExit('Hibás letöltés, megőrizve: ' + str(temp))
        if p.exists(): raise SystemExit('Az új fájlnév közben foglalttá vált.')
        temp.rename(p)
    if p.stat().st_size != part['bytes'] or digest(p) != part['sha256']:
        raise SystemExit('Eltérő vagy sérült darab, változatlanul megőrizve: ' + str(p))
output = folder / ('VISSZAALLITOTT_' + uuid.uuid4().hex[:12] + '.zip')
h = hashlib.sha256()
size = 0
with output.open('xb') as target:
    for part in manifest['parts']:
        ph = hashlib.sha256()
        with (folder / part['name']).open('rb') as source:
            for block in iter(lambda: source.read(4194304), b''):
                target.write(block); h.update(block); ph.update(block); size += len(block)
        if ph.hexdigest() != part['sha256']:
            raise SystemExit('A darab összeállítás közben megváltozott; részleges ZIP megőrizve.')
if h.hexdigest() != manifest['zip_sha256'] or size != manifest['zip_bytes']:
    raise SystemExit('A ZIP ellenőrzőösszege eltér; részleges ZIP megőrizve.')
print('Visszaállítva, SHA-256 ellenőrizve:', output)
