# v1.0 해시와 파일 식별

SHA-256을 원본·패치·결과 검증에 사용합니다. SHA-1·MD5·CRC32는 파일 식별용입니다. 원본과 완성 ROM은 배포하지 않습니다.

## 일본판 원본 ROM · 헤더 없음

| 항목 | 값 |
| --- | --- |
| 크기 | 1,048,576 bytes |
| SHA256 | `988eeb2c00dedecbf18f1eb22b5c462b604ac2863a9ead3dc2118c5fefb5d4d7` |
| SHA1 | `18f6451f3973f2c649726cb719b9e383fb13eac6` |
| MD5 | `6abe2920bc017a66665ae114ffa2bf0f` |
| CRC32 | `B9DCA26D` |

## 정상 패치 결과 ROM · 헤더 없음

| 항목 | 값 |
| --- | --- |
| 크기 | 2,097,152 bytes |
| SHA256 | `91cff6851c185e701db379cdbfe73675fbaeb008cd3667acbfa56e6d96cc982b` |
| SHA1 | `cdde8957740c8f26fcc7d2b5cd250d4917070e26` |
| MD5 | `56c11da102ab943446428f85d0bc4fd2` |
| CRC32 | `A01628FD` |

## 배포 파일

| 파일 | 크기(bytes) | SHA-256 |
| --- | ---: | --- |
| [KachouShimaKRPatcher-v1.0.exe](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/v1.0/KachouShimaKRPatcher-v1.0.exe) | 11,755,386 | `c7f0b7fc3e187e84133b70a3afcab756d520448d0b1a3732d3357186098d98a0` |
| [Kachou_Shima_Kousaku_KR_v1.0.ips](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/v1.0/Kachou_Shima_Kousaku_KR_v1.0.ips) | 466,824 | `f56c8139ded46772b0a0bfb80fd714f13bf614378993cfd5cee8286201799039` |
| [Kachou_Shima_Kousaku_KR_v1.0.zip](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/v1.0/Kachou_Shima_Kousaku_KR_v1.0.zip) | 11,796,133 | `c3a8f1eb686877f364de0e02a01d1b09e79b1d3f2c23b57707a614b1579f86df` |
| [release-manifest-v1.0.json](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/v1.0/release-manifest-v1.0.json) | 2,031 | `c340b4daccf3dafee1d185e1fbedfc0660b7d8f1b82c9d8c9a94990a40f0c7d9` |

복사기 헤더가 있으면 패처는 512바이트를 제외한 본문으로 원본 해시를 검사합니다. 잘못된 원본, 이미 수정된 ROM, 기존 출력 파일 덮어쓰기는 거부합니다.

```powershell
Get-FileHash -Algorithm SHA256 .\KachouShimaKRPatcher-v1.0.exe
```

[기계 판독용 목록](release_manifest.json) · [실제 EXE 검사 결과](patcher_validation.json)
