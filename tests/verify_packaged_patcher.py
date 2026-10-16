"""Exercise the distributed EXE with a user-supplied original ROM, kept local."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--exe', type=Path, required=True)
    parser.add_argument('--report', type=Path, required=True)
    args = parser.parse_args()
    source = args.source.read_bytes()
    source_hash = hashlib.sha256(source).hexdigest()
    expected_source = '988eeb2c00dedecbf18f1eb22b5c462b604ac2863a9ead3dc2118c5fefb5d4d7'
    target_hash = '92f03ebb46760334a2d26daa21b74816031a4b0897987d32a5b2ed9db6330d06'
    assert source_hash == expected_source
    exe = args.exe.resolve(strict=True)
    cases = []
    flags = subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
    with tempfile.TemporaryDirectory(prefix='shima-v08-') as temp:
        folder = Path(temp)

        def run(name, original=None, output=None, success=False, extra=()):
            report = folder / (name + '.json')
            command = [str(exe), *extra, '--report', str(report)]
            if original is not None:
                command += ['--input', str(original), '--output', str(output)]
            result = subprocess.run(command, capture_output=True, encoding='utf8', errors='replace', creationflags=flags, timeout=60)
            assert report.is_file(), (name, result.returncode, result.stderr)
            data = json.loads(report.read_text(encoding='utf8'))
            assert (result.returncode == 0) == success, (name, data)
            assert data['result'] == ('pass' if success else 'fail'), (name, data)
            entry = dict(case=name, result='pass', expected_acceptance=success, exit_code=result.returncode)
            if success and output is not None:
                output_data = output.read_bytes()
                assert len(output_data) == 2097152 and hashlib.sha256(output_data).hexdigest() == target_hash
                entry.update(output_sha256=target_hash, copier_header_removed=data['copier_header_removed'])
            cases.append(entry)

        original = folder / '일본판 원본.sfc'
        original.write_bytes(source)
        output = folder / '시마과장 한글 V0.8.sfc'
        run('headerless_unicode_paths', original, output, True)
        headered = folder / '복사기 헤더 포함.smc'
        headered.write_bytes(bytes(range(256)) * 2 + source)
        run('copier_header_removed', headered, folder / 'headerless_result.sfc', True)
        bad = folder / 'wrong_source.sfc'
        corrupt = bytearray(source)
        corrupt[100] ^= 1
        bad.write_bytes(corrupt)
        rejected = folder / 'must_not_exist.sfc'
        run('same_size_wrong_hash_rejected', bad, rejected)
        assert not rejected.exists()
        run('already_patched_rejected', output, rejected)
        assert not rejected.exists()
        existing = folder / 'existing.sfc'
        existing.write_bytes(b'existing file must survive')
        run('existing_output_preserved', original, existing)
        assert existing.read_bytes() == b'existing file must survive'
        run('same_path_rejected', original, original)
        assert original.read_bytes() == source
        short = folder / 'invalid.sfc'
        short.write_bytes(b'invalid')
        run('wrong_size_rejected', short, rejected)
        assert not rejected.exists()
        run('gui_constructed_and_embedded_patch_checked', success=True, extra=('--smoke-ui',))
    assert hashlib.sha256(args.source.read_bytes()).hexdigest() == source_hash
    data = dict(result='pass', version='V0.8', executable_sha256=hashlib.sha256(exe.read_bytes()).hexdigest(),
                source_sha256=source_hash, target_sha256=target_hash, source_preserved=True, cases=cases)
    args.report.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    print('PACKAGED_PATCHER_PASS', len(cases), 'cases', data['executable_sha256'])


if __name__ == '__main__':
    main()
