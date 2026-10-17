"""V0.81 Korean patcher. Standard-library CLI and a standalone Windows GUI."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import sys

VERSION = 'V0.81'
SOURCE_SIZE = 1_048_576
TARGET_SIZE = 2_097_152
SOURCE_SHA256 = '988eeb2c00dedecbf18f1eb22b5c462b604ac2863a9ead3dc2118c5fefb5d4d7'
TARGET_SHA256 = '3ed1c3f092caa0cf6ae5dca73f06553e0f6a219416c481eb239ec2cfc29ce52f'
PATCH_SHA256 = '37e564ef4d7787a5ee1e8ebea08c6b890e6551b17517549cee70d4843346b191'
PATCH_NAME = 'Kachou_Shima_Kousaku_KR_V0.81.ips'


class PatchError(ValueError):
    """An actionable input or patch validation error."""


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def normalize_source(data: bytes) -> tuple[bytes, bool]:
    if len(data) == TARGET_SIZE and digest(data) == TARGET_SHA256:
        raise PatchError('이미 V0.81 한글 패치가 적용된 ROM입니다.')
    header_removed = len(data) == SOURCE_SIZE + 512
    body = data[512:] if header_removed else data
    if len(body) != SOURCE_SIZE or digest(body) != SOURCE_SHA256:
        raise PatchError(
            '지원하는 일본판 원본 ROM과 일치하지 않습니다.\n'
            f'선택한 파일: {len(data):,}바이트\n'
            f'본문 SHA-256: {digest(body)}\n'
            f'필요한 SHA-256: {SOURCE_SHA256}')
    return body, header_removed


def apply_ips(source: bytes, patch: bytes, maximum_size: int = TARGET_SIZE) -> bytes:
    if not patch.startswith(b'PATCH'):
        raise PatchError('IPS 파일의 시작 표식이 올바르지 않습니다.')
    result = bytearray(source)
    at = 5

    def take(size: int) -> bytes:
        nonlocal at
        if at + size > len(patch):
            raise PatchError('IPS 파일이 중간에서 잘렸습니다.')
        data = patch[at:at + size]
        at += size
        return data

    while True:
        offset_raw = take(3)
        if offset_raw == b'EOF':
            break
        offset = int.from_bytes(offset_raw, 'big')
        size = int.from_bytes(take(2), 'big')
        if size:
            data = take(size)
        else:
            count = int.from_bytes(take(2), 'big')
            if count == 0:
                raise PatchError('길이가 0인 IPS 반복 레코드입니다.')
            data = take(1) * count
        end = offset + len(data)
        if end > maximum_size:
            raise PatchError('IPS 레코드가 허용된 ROM 크기를 벗어납니다.')
        if end > len(result):
            result.extend(bytes(end - len(result)))
        result[offset:end] = data
    remaining = len(patch) - at
    if remaining == 3:
        size = int.from_bytes(take(3), 'big')
        if size > maximum_size:
            raise PatchError('IPS 최종 크기가 허용 범위를 벗어납니다.')
        if len(result) < size:
            result.extend(bytes(size - len(result)))
        del result[size:]
    elif remaining:
        raise PatchError('IPS 종료 표식 뒤에 알 수 없는 데이터가 있습니다.')
    return bytes(result)


def patch_path() -> Path:
    if getattr(sys, 'frozen', False):
        return Path(sys._MEIPASS) / 'patches' / PATCH_NAME
    return Path(__file__).resolve().parents[1] / 'patches' / PATCH_NAME


def read_patch() -> bytes:
    data = patch_path().read_bytes()
    if digest(data) != PATCH_SHA256:
        raise PatchError('내장 IPS의 SHA-256이 일치하지 않습니다. 패처를 다시 받아 주세요.')
    return data


def patch_file(input_path: Path, output_path: Path) -> dict:
    source_path = input_path.expanduser().resolve(strict=True)
    destination = output_path.expanduser().resolve()
    if os.path.normcase(str(source_path)) == os.path.normcase(str(destination)):
        raise PatchError('원본 ROM과 저장할 파일의 이름을 다르게 지정해 주세요.')
    if destination.exists():
        raise PatchError('저장 위치에 같은 이름의 파일이 있습니다. 다른 이름을 선택해 주세요.')
    if source_path.stat().st_size not in (SOURCE_SIZE, SOURCE_SIZE + 512, TARGET_SIZE):
        raise PatchError('ROM 크기가 다릅니다. 헤더 없는 원본은 1,048,576바이트입니다.')
    source, header_removed = normalize_source(source_path.read_bytes())
    result = apply_ips(source, read_patch())
    if len(result) != TARGET_SIZE or digest(result) != TARGET_SHA256:
        raise PatchError('패치 결과의 크기 또는 SHA-256이 맞지 않습니다. 파일을 저장하지 않았습니다.')
    created = False
    try:
        # Exclusive creation also protects existing files if the path changed
        # between the checks above and this write.
        with destination.open('xb') as stream:
            created = True
            stream.write(result)
            stream.flush()
            os.fsync(stream.fileno())
        if digest(destination.read_bytes()) != TARGET_SHA256:
            raise PatchError('저장한 파일의 검증에 실패했습니다.')
    except Exception:
        if created:
            destination.unlink(missing_ok=True)
        raise
    return dict(result='pass', version=VERSION, copier_header_removed=header_removed,
                source_sha256=SOURCE_SHA256, patch_sha256=PATCH_SHA256,
                output_sha256=TARGET_SHA256, output_bytes=TARGET_SIZE,
                source_preserved=True, output=str(destination))


def launch_gui(smoke: bool = False) -> None:
    import tkinter as tk
    from tkinter import filedialog, messagebox, ttk

    root = tk.Tk()
    if smoke:
        root.withdraw()
    root.title('시마과장 V0.81 한글 패처')
    root.geometry('740x430')
    root.minsize(660, 420)
    root.option_add('*Font', ('맑은 고딕', 10))
    style = ttk.Style(root)
    if 'vista' in style.theme_names():
        style.theme_use('vista')
    panel = ttk.Frame(root, padding=24)
    panel.pack(fill='both', expand=True)
    panel.columnconfigure(0, weight=1)
    ttk.Label(panel, text='시마과장 V0.81', font=('맑은 고딕', 21, 'bold')).grid(row=0, column=0, columnspan=2, sticky='w')
    ttk.Label(panel, text='일본판 원본 ROM을 선택하면 원본을 보존하고 한글 ROM을 새로 만듭니다.').grid(row=1, column=0, columnspan=2, sticky='w', pady=(8, 22))
    source = tk.StringVar()
    destination = tk.StringVar()
    status = tk.StringVar(value='원본 SHA-256 확인 → 내장 IPS 적용 → 저장한 파일의 SHA-256 확인')
    ttk.Label(panel, text='일본판 원본 ROM').grid(row=2, column=0, sticky='w')
    ttk.Entry(panel, textvariable=source, state='readonly').grid(row=3, column=0, sticky='ew', pady=(6, 16))

    def choose_source():
        path = filedialog.askopenfilename(parent=root, title='일본판 원본 ROM 선택', filetypes=[('SFC/SNES ROM', '*.sfc *.smc'), ('모든 파일', '*.*')])
        if path:
            source.set(path)
            p = Path(path)
            destination.set(str(p.with_name(p.stem + ' [KR V0.81].sfc')))

    ttk.Button(panel, text='원본 선택', command=choose_source).grid(row=3, column=1, padx=(10, 0), pady=(6, 16))
    ttk.Label(panel, text='저장할 한글 ROM').grid(row=4, column=0, sticky='w')
    ttk.Entry(panel, textvariable=destination, state='readonly').grid(row=5, column=0, sticky='ew', pady=(6, 20))

    def choose_destination():
        path = filedialog.asksaveasfilename(parent=root, title='한글 ROM 저장 위치', defaultextension='.sfc', initialfile=Path(destination.get()).name if destination.get() else 'Shima_KR_V0.81.sfc', filetypes=[('SFC ROM', '*.sfc')])
        if path:
            destination.set(path)

    ttk.Button(panel, text='저장 위치', command=choose_destination).grid(row=5, column=1, padx=(10, 0), pady=(6, 20))

    def run():
        if not source.get() or not destination.get():
            messagebox.showinfo('원본 ROM 선택', '일본판 원본 ROM과 저장 위치를 선택해 주세요.', parent=root)
            return
        button.state(['disabled'])
        status.set('원본과 패치 결과를 확인하고 있습니다…')
        root.update_idletasks()
        try:
            result = patch_file(Path(source.get()), Path(destination.get()))
        except Exception as error:
            status.set('완료되지 않았습니다. 원본 ROM은 보존했습니다.')
            messagebox.showerror('패치 확인', str(error), parent=root)
        else:
            status.set('완료 · 저장 파일의 SHA-256 검증 통과')
            header = '\n512바이트 복사기 헤더를 제거했습니다.' if result['copier_header_removed'] else ''
            messagebox.showinfo('한글 패치 완료', f"저장: {result['output']}{header}\n\nSHA-256\n{TARGET_SHA256}", parent=root)
        finally:
            button.state(['!disabled'])

    button = ttk.Button(panel, text='한글 패치 적용', command=run)
    button.grid(row=6, column=0, columnspan=2, sticky='ew', ipady=9)
    ttk.Label(panel, textvariable=status, wraplength=650).grid(row=7, column=0, columnspan=2, sticky='w', pady=(15, 0))
    ttk.Label(panel, text='1MB 일본판 원본 · 512바이트 복사기 헤더 자동 인식 · 결과 2MB', foreground='#555555').grid(row=8, column=0, columnspan=2, sticky='w', pady=(10, 0))
    if smoke:
        read_patch()
        root.update_idletasks()
        root.update()
        root.destroy()
    else:
        root.mainloop()


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description='시마과장 V0.81 한글 패처')
    parser.add_argument('--input', type=Path)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--report', type=Path, help='검사 결과 JSON 저장 위치')
    parser.add_argument('--smoke-ui', action='store_true', help='창 구성과 내장 패치의 자동 검사')
    args = parser.parse_args(argv)
    result = None
    try:
        if args.smoke_ui:
            launch_gui(smoke=True)
            result = dict(result='pass', gui_constructed=True, patch_sha256=PATCH_SHA256)
        elif args.input or args.output:
            if not args.input or not args.output:
                raise PatchError('--input과 --output을 함께 지정해 주세요.')
            result = patch_file(args.input, args.output)
        else:
            launch_gui()
            return 0
    except Exception as error:
        result = dict(result='fail', error=str(error), version=VERSION)
    if args.report:
        args.report.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    if sys.stdout is not None:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['result'] == 'pass' else 1


if __name__ == '__main__':
    raise SystemExit(main())
