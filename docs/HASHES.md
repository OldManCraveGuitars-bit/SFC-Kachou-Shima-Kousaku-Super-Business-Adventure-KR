# v1.11 해시와 파일 식별

SHA-256을 원본·패치·결과 검증에 사용합니다. SHA-1·MD5·CRC32는 파일 식별용입니다. ROM은 배포하지 않습니다.

## 일본판 원본 ROM · 헤더 없음

| 항목 | 값 |
| --- | --- |
| 크기 | 1,048,576 bytes |
| SHA256 | `988eeb2c00dedecbf18f1eb22b5c462b604ac2863a9ead3dc2118c5fefb5d4d7` |
| SHA1 | `18f6451f3973f2c649726cb719b9e383fb13eac6` |
| MD5 | `6abe2920bc017a66665ae114ffa2bf0f` |
| CRC32 | `B9DCA26D` |

## v1.11 패치 결과 ROM · 헤더 없음

| 항목 | 값 |
| --- | --- |
| 크기 | 2,097,152 bytes |
| SHA256 | `a2bdd89e572f1640c5675fc3c9f88a502da6d8f8dcf37dbd8871f425e66b027b` |
| SHA1 | `7ea1a0dc37bc1e8b98dbdc1cc474e722cd9f5529` |
| MD5 | `8cedf65363c9ea5260b383304ef62ee7` |
| CRC32 | `CC4F02CB` |

## 배포 파일

| 파일 | 크기(bytes) | SHA-256 |
| --- | ---: | --- |
| [KachouShimaKRPatcher-v1.11.exe](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/v1.11/KachouShimaKRPatcher-v1.11.exe) | 11,763,459 | `2d2b0bd8c85a1ff6f5e36ab8178b71bb2dba17f84af834971ca098c4bcd226fe` |
| [Kachou_Shima_Kousaku_KR_v1.11.ips](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/v1.11/Kachou_Shima_Kousaku_KR_v1.11.ips) | 484,027 | `af64d0d4aa28ea7010539f5b45ac11274b665692988d010e5aecb6c72b839048` |
| [Kachou_Shima_Kousaku_KR_v1.11.zip](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/v1.11/Kachou_Shima_Kousaku_KR_v1.11.zip) | 11,811,350 | `b0e79061447e6ba201fe8c4f93c3edbde2c6c51bbd2070393d19a82e614c997d` |
| [release-manifest-v1.11.json](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/v1.11/release-manifest-v1.11.json) | 2,525 | `a2394992902ea62667229a245afa5aa1d85586b9a62d8dae9fb17d4904bccfbb` |

[기계 판독용 목록](release_manifest.json) · [EXE 검사](patcher_validation.json)

```powershell
Get-FileHash -Algorithm SHA256 .\KachouShimaKRPatcher-v1.11.exe
```
