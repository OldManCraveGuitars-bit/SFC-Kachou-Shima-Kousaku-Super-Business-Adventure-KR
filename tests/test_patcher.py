import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('shima_patcher', ROOT / 'patcher/patcher.py')
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)


class IpsFormatTests(unittest.TestCase):
    def test_literal_rle_and_expansion(self):
        patch = b'PATCH' + bytes.fromhex('000001 0002') + b'XY' + bytes.fromhex('000005 0000 0003') + b'Z' + b'EOF'
        self.assertEqual(p.apply_ips(b'abcd', patch), b'aXYd\0ZZZ')

    def test_explicit_truncation(self):
        self.assertEqual(p.apply_ips(b'abcdef', b'PATCHEOF\0\0\3'), b'abc')

    def test_truncated_records(self):
        for patch in [b'PATCH', b'PATCH\0\0', b'PATCH\0\0\1\0', b'PATCH\0\0\1\0\2X', b'PATCH\0\0\1\0\0\0\2']:
            with self.subTest(patch=patch), self.assertRaises(p.PatchError):
                p.apply_ips(b'abcd', patch)

    def test_extra_bytes_rejected(self):
        with self.assertRaises(p.PatchError):
            p.apply_ips(b'abcd', b'PATCHEOFgarbage')

    def test_oversize_record_rejected(self):
        with self.assertRaises(p.PatchError):
            p.apply_ips(b'abcd', b'PATCH' + bytes.fromhex('200000 0001') + b'XEOF')

    def test_oversize_truncation_rejected(self):
        with self.assertRaises(p.PatchError):
            p.apply_ips(b'abcd', b'PATCHEOF' + bytes.fromhex('200001'))

    def test_zero_length_rle_rejected(self):
        with self.assertRaises(p.PatchError):
            p.apply_ips(b'abcd', b'PATCH' + bytes.fromhex('000001 0000 0000') + b'XEOF')

    def test_wrong_magic_rejected(self):
        with self.assertRaises(p.PatchError):
            p.apply_ips(b'abcd', b'NOTIPS')

    def test_embedded_release_patch_hash(self):
        self.assertEqual(p.digest(p.read_patch()), p.PATCH_SHA256)

    def test_wrong_source_rejected(self):
        with self.assertRaises(p.PatchError):
            p.normalize_source(bytes(p.SOURCE_SIZE))

    def test_same_output_path_protects_source(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / '원본.sfc'
            path.write_bytes(b'original')
            with self.assertRaises(p.PatchError):
                p.patch_file(path, path)
            self.assertEqual(path.read_bytes(), b'original')

    def test_existing_destination_is_preserved(self):
        with tempfile.TemporaryDirectory() as temp:
            source, target = Path(temp) / 'original.sfc', Path(temp) / '한글.sfc'
            source.write_bytes(b'original')
            target.write_bytes(b'keep me')
            with self.assertRaises(p.PatchError):
                p.patch_file(source, target)
            self.assertEqual(target.read_bytes(), b'keep me')


if __name__ == '__main__':
    unittest.main()
