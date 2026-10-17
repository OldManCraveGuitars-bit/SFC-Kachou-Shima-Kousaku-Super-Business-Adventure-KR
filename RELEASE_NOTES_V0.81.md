# V0.81 · 누락 장 제목 한글화·교토 편 가운데 정렬

2026-10-17 · 한글화 기타 깎는 노인

## 받기

일반 적용은 **[Kachou_Shima_Kousaku_KR_V0.81.zip](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/V0.81/Kachou_Shima_Kousaku_KR_V0.81.zip)**를 받아 압축을 풀고 패처 EXE를 실행하세요. 원본은 보존하고 새 한글 ROM을 만듭니다. 원본과 결과 ROM은 배포하지 않습니다.

## 변경 사항

- 누락된 장 제목 3종을 한글화: **뉴욕 편·내부자 거래 편·사장 교체극 편**.
- **교토 편**을 띄어 쓰고 뉴욕 편과 같이 가운데 정렬.
- 제목 5종 네이티브 화면 추가, 공개 갤러리 54장.
- V0.8 대비 제목 4종과 체크섬만 변경. 대사 10,414항목·오프닝·배경·엔딩·크레딧은 바이트 동일.

아래는 V0.8에서 이어지는 누적 내용입니다.

- 등록 10,414항목 / 검수 승인 10,406항목 / 보존한 비대사 제어 8항목.
- 본편 대사의 의미·말투·이름·직함·조사·공용 문구·줄바꿈 재검토.
- 누락된 오프닝 인물 소개·임명장·대기 데모 대사 9곳 한글화.
- 줌아웃 로고의 순간 벌어짐, 타이틀 대기 후 그래픽 깨짐, 조기 건너뛰기 처리 보완.
- 원판 그림·영어·完과 중앙 한글화 크레딧 보존.
- 원본 검사와 결과 해시 검증을 포함한 설치 없는 Windows 패처 추가.
- [스크린샷 54장](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/blob/V0.81/docs/SCREENSHOTS.md), 적용 안내·변경 기록·검증 문서를 V0.81 기준으로 갱신.

## 적용 대상

| 구분 | 크기 | SHA-256 |
| --- | ---: | --- |
| 일본판 원본·헤더 없음 | 1,048,576 | `988eeb2c00dedecbf18f1eb22b5c462b604ac2863a9ead3dc2118c5fefb5d4d7` |
| 정상 한글 결과·헤더 없음 | 2,097,152 | `3ed1c3f092caa0cf6ae5dca73f06553e0f6a219416c481eb239ec2cfc29ce52f` |

512바이트 복사기 헤더는 본문 SHA-256 확인 후 자동 제거합니다. 이미 수정한 ROM은 원본 검사에서 거부합니다. SRAM은 백업하고, 업데이트 확인은 저장 상태를 불러오기보다 ROM을 완전히 다시 시작해 진행하세요.

## 배포 파일과 SHA-256

| 파일 | 크기(bytes) | SHA-256 |
| --- | ---: | --- |
| [KachouShimaKRPatcher-V0.81.exe](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/V0.81/KachouShimaKRPatcher-V0.81.exe) | 11,755,467 | `1099d9c0de93c61c1af7e3679963bca62ddf2db3d787fdd19cd85e8fb757b1b1` |
| [Kachou_Shima_Kousaku_KR_V0.81.ips](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/V0.81/Kachou_Shima_Kousaku_KR_V0.81.ips) | 464,871 | `37e564ef4d7787a5ee1e8ebea08c6b890e6551b17517549cee70d4843346b191` |
| [KachouShimaDialogueEditor-V0.81.exe](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/V0.81/KachouShimaDialogueEditor-V0.81.exe) | 34,502,210 | `400f70cc985a1bba1ff68c23a785ad9e15321193ae5406ceb6d3115ff4dff3d6` |
| [Kachou_Shima_Kousaku_KR_V0.81.zip](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/V0.81/Kachou_Shima_Kousaku_KR_V0.81.zip) | 11,796,588 | `b76d5dfaabd67c4f62308326eb705f8a247e8cc95617b4c9974f7a760c113050` |
| [release-manifest-V0.81.json](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/V0.81/release-manifest-V0.81.json) | 2,266 | `2a54bf86a4e860b264c4a25b0d824c7ca316eaa9803d5a45e504e769be073629` |

## 확인한 범위

제목 5종을 Snes9x에서, 뉴욕·교토를 bsnes에서도 확인했습니다. 장 진입은 원래 게임 코드를 사용하는 격리 진단으로 촬영했으며 일반 경로 전체 재생을 뜻하지 않습니다. 기존 49장에 제목 5장을 더했습니다. 10,414항목과 오프닝·배경·엔딩은 V0.8과 바이트가 같습니다. [장 제목 검증](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/blob/V0.81/docs/chapter_card_validation.json).

아래 오프닝 검증은 변경되지 않은 V0.8 데이터에 대한 기존 기록입니다.

Snes9x 연속 데모·bsnes 데모와 다음 타이틀, 시작 버튼·조기 건너뛰기·리셋을 확인했습니다. 561본문·150선택지·별도 오프닝의 제어 효과 차이 0, 페이지 넘김 차이 0입니다. 패처는 12단위 검사와 8실제 EXE 검사, 대본 도구는 8개 실제 수정·재생성 검사를 통과했습니다.

기존 15개 연결 결말과 대표 저장 검증은 동일한 본편·결말 데이터 대조와 함께 유지했습니다. 모든 선택 조합·모든 기기·15결말을 이번 버전으로 전부 새로 재생한 검사는 아닙니다. [검증 기록](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/blob/V0.81/docs/current_validation.json) · [전체 해시](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/blob/V0.81/docs/HASHES.md).

대본 도구는 검색·열람·CSV용으로 별도 제공합니다. ROM 재생성 기능은 원본과 개발 프로젝트가 있는 환경에서 사용합니다.
