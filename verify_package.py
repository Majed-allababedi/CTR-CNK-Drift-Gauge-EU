"""Verify this repository's package and an optional release ZIP (stdlib only)."""
from pathlib import Path
import argparse
import hashlib
import json
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parent
PACKAGE = ROOT / 'package' / 'reserves-cnk-drift-gauge'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def verify(package=PACKAGE, archive=None):
    manifest = json.loads((package / 'mod.json').read_text(encoding='utf-8'))
    assert manifest['version'] == '1.0.9'
    assert manifest['author'] == 'Majed-allababedi'
    declared = {record['file']: record for record in manifest['files']}
    assert len(declared) == len(manifest['files'])
    actual = {p.relative_to(package).as_posix() for p in package.rglob('*') if p.is_file()}
    assert actual == set(declared) | {'mod.json'}
    for name, record in declared.items():
        data = (package / name).read_bytes()
        assert len(data) == record['bytes'], name
        assert digest(data) == record['sha256'], name
    for operation in manifest['operations']:
        assert digest((package / operation['payload']).read_bytes()) == operation['patched_sha256']
    tree = ET.parse(package / 'patches/reserves.xml')
    assert [node.text for node in tree.findall('./TitleID/ID')] == ['CUSA14876']
    lines = list(tree.iter('Line'))
    assert len(manifest['operations']) == 29 and len(lines) == 7
    for line in lines:
        assert len(line.get('ExpectedSHA256', '')) == 64
        bytes.fromhex(line.get('Value'))
    records = json.loads((ROOT / 'verification/package-files.json').read_text())
    assert set(records) == actual
    for name, record in records.items():
        data = (package / name).read_bytes()
        assert digest(data) == record['sha256'] and len(data) == record['bytes']
    if archive:
        with zipfile.ZipFile(archive) as z:
            assert z.testzip() is None
            prefix = 'reserves-cnk-drift-gauge/'
            assert {info.filename for info in z.infolist()} == {prefix + name for name in actual}
            assert len(z.infolist()) == len(actual)
            for name in actual:
                assert z.read(prefix + name) == (package / name).read_bytes(), name
    return {'package_files': len(actual), 'archive_operations': 29, 'executable_writes': 7,
            'status': 'PASS', 'checks': 'Package/ZIP integrity and metadata; not an in-game test.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--zip', type=Path)
    args = parser.parse_args()
    print(json.dumps(verify(archive=args.zip), indent=2))
