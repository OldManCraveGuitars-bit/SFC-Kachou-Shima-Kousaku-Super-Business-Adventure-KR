# V0.8 파일 식별 및 해시

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
| SHA-256 | `92f03ebb46760334a2d26daa21b74816031a4b0897987d32a5b2ed9db6330d06` |
| SHA-1 | `3683f8665441e19537d17a1658f8a3cd9282be43` |
| MD5 | `c54439228e776afbbb4c152fa16c4a41` |
| CRC32 | `A57715B4` |

원본과 결과 ROM은 배포 파일에 포함하지 않습니다. 512바이트 복사기 헤더가 있으면 패처가 헤더를 제거한 본문을 원본 SHA-256과 대조합니다. 이미 수정한 ROM이나 다른 판본은 거부합니다.

## 배포 파일

| 파일 | 크기(bytes) | SHA-256 |
| --- | ---: | --- |
| [KachouShimaKRPatcher-V0.8.exe](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/V0.8/KachouShimaKRPatcher-V0.8.exe) | 11,757,600 | `99a930169f0f561356eda963bdbd082546d33cb23618222e375fdfcbd9d6b9eb` |
| [Kachou_Shima_Kousaku_KR_V0.8.ips](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/V0.8/Kachou_Shima_Kousaku_KR_V0.8.ips) | 465,823 | `b76f7b1e1136cfb6d5beada07d53b501fdf66f9a740d36f63b4510e7e959dfe9` |
| [KachouShimaDialogueEditor-V0.8.exe](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/V0.8/KachouShimaDialogueEditor-V0.8.exe) | 34,501,684 | `71fa39ab17dad3a28259f24a1b652b0fabaf60696270fb5723136e5c6ee7856e` |
| [Kachou_Shima_Kousaku_KR_V0.8.zip](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/V0.8/Kachou_Shima_Kousaku_KR_V0.8.zip) | 11,798,893 | `2a5cc06297793f1bdcc8326b1f7e3e5a5f57bf55418768813d1be492a88d1c7a` |
| [release-manifest-V0.8.json](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/V0.8/release-manifest-V0.8.json) | 2,314 | `44d130f39ad8f02edc5a0873331854eb1f1500cac35891bb3384c586b4a69a2d` |

## 다운로드 확인

릴리스의 `SHA256SUMS.txt`와 대조할 파일을 같은 폴더에 놓습니다. Windows PowerShell 예시:

```powershell
Get-FileHash -Algorithm SHA256 .\KachouShimaKRPatcher-V0.8.exe
```

기계 판독용 전체 식별 정보는 [`release_manifest.json`](release_manifest.json), 패처 EXE의 실제 검사 결과는 [`patcher_validation.json`](patcher_validation.json)에 있습니다.
