# V0.8 · 대사 재검수·오프닝 수정·전용 패처

2026-10-17 · 한글화 기타 깎는 노인

## 받기

일반 적용은 **[Kachou_Shima_Kousaku_KR_V0.8.zip](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/V0.8/Kachou_Shima_Kousaku_KR_V0.8.zip)**를 받아 압축을 풀고 패처 EXE를 실행하세요. 원본은 보존하고 새 한글 ROM을 만듭니다. 원본과 결과 ROM은 배포하지 않습니다.

## 변경 사항

- 등록 10,414항목 / 검수 승인 10,406항목 / 보존한 비대사 제어 8항목.
- 본편 대사의 의미·말투·이름·직함·조사·공용 문구·줄바꿈 재검토.
- 누락된 오프닝 인물 소개·임명장·대기 데모 대사 9곳 한글화.
- 줌아웃 로고의 순간 벌어짐, 타이틀 대기 후 그래픽 깨짐, 조기 건너뛰기 처리 보완.
- 원판 그림·영어·完과 중앙 한글화 크레딧 보존.
- 원본 검사와 결과 해시 검증을 포함한 설치 없는 Windows 패처 추가.
- [스크린샷 49장](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/blob/V0.8/docs/SCREENSHOTS.md), 적용 안내·변경 기록·검증 문서를 V0.8 기준으로 갱신.

## 적용 대상

| 구분 | 크기 | SHA-256 |
| --- | ---: | --- |
| 일본판 원본·헤더 없음 | 1,048,576 | `988eeb2c00dedecbf18f1eb22b5c462b604ac2863a9ead3dc2118c5fefb5d4d7` |
| 정상 한글 결과·헤더 없음 | 2,097,152 | `92f03ebb46760334a2d26daa21b74816031a4b0897987d32a5b2ed9db6330d06` |

512바이트 복사기 헤더는 본문 SHA-256 확인 후 자동 제거합니다. 이미 수정한 ROM은 원본 검사에서 거부합니다. SRAM은 백업하고, 업데이트 확인은 저장 상태를 불러오기보다 ROM을 완전히 다시 시작해 진행하세요.

## 배포 파일과 SHA-256

| 파일 | 크기(bytes) | SHA-256 |
| --- | ---: | --- |
| [KachouShimaKRPatcher-V0.8.exe](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/V0.8/KachouShimaKRPatcher-V0.8.exe) | 11,757,600 | `99a930169f0f561356eda963bdbd082546d33cb23618222e375fdfcbd9d6b9eb` |
| [Kachou_Shima_Kousaku_KR_V0.8.ips](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/V0.8/Kachou_Shima_Kousaku_KR_V0.8.ips) | 465,823 | `b76f7b1e1136cfb6d5beada07d53b501fdf66f9a740d36f63b4510e7e959dfe9` |
| [KachouShimaDialogueEditor-V0.8.exe](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/V0.8/KachouShimaDialogueEditor-V0.8.exe) | 34,501,684 | `71fa39ab17dad3a28259f24a1b652b0fabaf60696270fb5723136e5c6ee7856e` |
| [Kachou_Shima_Kousaku_KR_V0.8.zip](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/V0.8/Kachou_Shima_Kousaku_KR_V0.8.zip) | 11,798,893 | `2a5cc06297793f1bdcc8326b1f7e3e5a5f57bf55418768813d1be492a88d1c7a` |
| [release-manifest-V0.8.json](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/V0.8/release-manifest-V0.8.json) | 2,314 | `44d130f39ad8f02edc5a0873331854eb1f1500cac35891bb3384c586b4a69a2d` |

## 확인한 범위

Snes9x 연속 데모·bsnes 데모와 다음 타이틀, 시작 버튼·조기 건너뛰기·리셋을 확인했습니다. 561본문·150선택지·별도 오프닝의 제어 효과 차이 0, 페이지 넘김 차이 0입니다. 패처는 12단위 검사와 8실제 EXE 검사, 대본 도구는 8개 실제 수정·재생성 검사를 통과했습니다.

기존 15개 연결 결말과 대표 저장 검증은 동일한 본편·결말 데이터 대조와 함께 유지했습니다. 모든 선택 조합·모든 기기·15결말을 이번 버전으로 전부 새로 재생한 검사는 아닙니다. [검증 기록](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/blob/V0.8/docs/current_validation.json) · [전체 해시](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/blob/V0.8/docs/HASHES.md).

대본 도구는 검색·열람·CSV용으로 별도 제공합니다. ROM 재생성 기능은 원본과 개발 프로젝트가 있는 환경에서 사용합니다.
