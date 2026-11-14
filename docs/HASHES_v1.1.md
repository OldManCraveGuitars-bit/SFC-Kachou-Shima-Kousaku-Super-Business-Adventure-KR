# v1.1 해시와 파일 식별

SHA-256을 원본·패치·결과 검증에 사용합니다. SHA-1·MD5·CRC32는 파일 식별용입니다. ROM은 배포하지 않습니다.

## 일본판 원본 ROM · 헤더 없음

| 항목 | 값 |
| --- | --- |
| 크기 | 1,048,576 bytes |
| SHA256 | `988eeb2c00dedecbf18f1eb22b5c462b604ac2863a9ead3dc2118c5fefb5d4d7` |
| SHA1 | `18f6451f3973f2c649726cb719b9e383fb13eac6` |
| MD5 | `6abe2920bc017a66665ae114ffa2bf0f` |
| CRC32 | `B9DCA26D` |

## v1.1 패치 결과 ROM · 헤더 없음

| 항목 | 값 |
| --- | --- |
| 크기 | 2,097,152 bytes |
| SHA256 | `191aa46eae0c2b5cfb5bf89c8bb53a8d1153f41de303156b52b84147754b5f12` |
| SHA1 | `30e054c244ca7c296deca317951353250ad223d9` |
| MD5 | `68b970ea87677f7252fdfbf30894058c` |
| CRC32 | `CA41E474` |

## 배포 파일

| 파일 | 크기(bytes) | SHA-256 |
| --- | ---: | --- |
| [KachouShimaKRPatcher-v1.1.exe](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/v1.1/KachouShimaKRPatcher-v1.1.exe) | 11,762,413 | `fd39a5a028728f95a00ec9836d85e6771c23cef1af3890f11f97ca7019563a12` |
| [Kachou_Shima_Kousaku_KR_v1.1.ips](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/v1.1/Kachou_Shima_Kousaku_KR_v1.1.ips) | 483,991 | `bd88a120b13d963e32b52a3533ce51cc65d88b6f29a076c130d5589e1cf3692e` |
| [Kachou_Shima_Kousaku_KR_v1.1.zip](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/v1.1/Kachou_Shima_Kousaku_KR_v1.1.zip) | 11,810,265 | `ce09e76e83ec77849c1abbe4f95e5c4fb0fad292b519e8c6841f6e25c1f13a9e` |
| [release-manifest-v1.1.json](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/v1.1/release-manifest-v1.1.json) | 2,508 | `eb85b698f6ae958bbf3b4f528227783a2a36df52e9dad3fabb3ae059b9c0542b` |

[기계 판독용 목록](release_manifest_v1.1.json) · [EXE 검사](patcher_validation_v1.1.json)

```powershell
Get-FileHash -Algorithm SHA256 .\KachouShimaKRPatcher-v1.1.exe
```
