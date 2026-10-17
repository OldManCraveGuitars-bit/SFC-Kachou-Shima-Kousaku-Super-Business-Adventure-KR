# V0.81 파일 식별 및 해시

2026-10-17 기준입니다. SHA-256을 패처의 원본 검사와 결과 검사에 사용합니다. SHA-1·MD5·CRC32는 파일 식별용으로 함께 제공합니다.

## 일본판 원본 ROM · 헤더 없음

| 항목 | 값 |
| --- | --- |
| 크기 | 1,048,576 bytes |
| SHA-256 | `988eeb2c00dedecbf18f1eb22b5c462b604ac2863a9ead3dc2118c5fefb5d4d7` |
| SHA-1 | `18f6451f3973f2c649726cb719b9e383fb13eac6` |
| MD5 | `6abe2920bc017a66665ae114ffa2bf0f` |
| CRC32 | `B9DCA26D` |

## 정상 패치 결과 ROM · 헤더 없음

| 항목 | 값 |
| --- | --- |
| 크기 | 2,097,152 bytes |
| SHA-256 | `3ed1c3f092caa0cf6ae5dca73f06553e0f6a219416c481eb239ec2cfc29ce52f` |
| SHA-1 | `1b6bed3dd75df4c87e3dfb67c4b6eade1a23de33` |
| MD5 | `94c447352cb8998161351cda1691ec06` |
| CRC32 | `F52CD2B8` |

원본과 결과 ROM은 배포 파일에 포함하지 않습니다. 512바이트 복사기 헤더가 있으면 패처가 헤더를 제거한 본문을 원본 SHA-256과 대조합니다. 이미 수정한 ROM이나 다른 판본은 거부합니다.

## 배포 파일

| 파일 | 크기(bytes) | SHA-256 |
| --- | ---: | --- |
| [KachouShimaKRPatcher-V0.81.exe](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/V0.81/KachouShimaKRPatcher-V0.81.exe) | 11,755,467 | `1099d9c0de93c61c1af7e3679963bca62ddf2db3d787fdd19cd85e8fb757b1b1` |
| [Kachou_Shima_Kousaku_KR_V0.81.ips](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/V0.81/Kachou_Shima_Kousaku_KR_V0.81.ips) | 464,871 | `37e564ef4d7787a5ee1e8ebea08c6b890e6551b17517549cee70d4843346b191` |
| [KachouShimaDialogueEditor-V0.81.exe](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/V0.81/KachouShimaDialogueEditor-V0.81.exe) | 34,502,210 | `400f70cc985a1bba1ff68c23a785ad9e15321193ae5406ceb6d3115ff4dff3d6` |
| [Kachou_Shima_Kousaku_KR_V0.81.zip](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/V0.81/Kachou_Shima_Kousaku_KR_V0.81.zip) | 11,796,588 | `b76d5dfaabd67c4f62308326eb705f8a247e8cc95617b4c9974f7a760c113050` |
| [release-manifest-V0.81.json](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/V0.81/release-manifest-V0.81.json) | 2,266 | `2a54bf86a4e860b264c4a25b0d824c7ca316eaa9803d5a45e504e769be073629` |

## 다운로드 확인

릴리스의 `SHA256SUMS.txt`와 대조할 파일을 같은 폴더에 놓습니다. Windows PowerShell 예시:

```powershell
Get-FileHash -Algorithm SHA256 .\KachouShimaKRPatcher-V0.81.exe
```

기계 판독용 전체 식별 정보는 [`release_manifest.json`](release_manifest.json), 패처 EXE의 실제 검사 결과는 [`patcher_validation.json`](patcher_validation.json)에 있습니다.
