# 과장 시마 고사쿠 슈퍼 비즈니스 어드벤처 한글 패치 V0.2

《과장 시마 고사쿠》는 회사원 시마 고사쿠의 업무와 인간관계를 선택지로 따라가는 슈퍼패미컴 어드벤처 게임입니다. 일본판의 대사·선택지와 일부 화면 글씨를 한국어로 옮긴 비공식 IPS 패치입니다. 원래 영어인 문구는 영어로 유지합니다.

> **2026-10-10 공개 테스트 빌드 — 테스트가 많이 부족합니다.** 등록 대사 4,879칸 중 3,233칸만 검수 승인했고 1,646칸이 미승인입니다. 일본어 원문이 비어 있는 칸 205개와 원판 시간차 표시 호출이 빠진 곳 64개가 남아 있습니다. 문맥·말투·화자·글자 위치·그래픽 오류가 있을 수 있으며 모든 분기, 저장 파일, 에뮬레이터를 확인하지 못했습니다.

이번 갱신에서 초반 독백과 선택지 문구를 다듬고, 후반 독백의 누락된 시간차 점 표시 여섯 곳을 복원했습니다. 녹음 속 “야베 군…”의 화자는 아직 확정하지 못해 검수 승인에서 제외했습니다. 대본을 주소별로 검색·수정하고 CSV로 내보내거나 가져오는 Windows 프로그램 `KachouShimaDialogueEditor.exe`도 함께 제공합니다.

| 타이틀 | 이야기 도입 |
| --- | --- |
| ![타이틀](https://raw.githubusercontent.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/main/screenshots/title.png) | ![도입](https://raw.githubusercontent.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/main/screenshots/opening-narration.png) |
| 선택지 | 불러오기 |
| ![선택지](https://raw.githubusercontent.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/main/screenshots/opening-choice.png) | ![불러오기](https://raw.githubusercontent.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/main/screenshots/load-screen.png) |
| 이어하기 | 독백 |
| ![이어하기](https://raw.githubusercontent.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/main/screenshots/load-popup.png) | ![독백](https://raw.githubusercontent.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/main/screenshots/timed-dialogue.png) |

헤더 없는 일본판 원본 ROM(SHA-256 `988eeb2c00dedecbf18f1eb22b5c462b604ac2863a9ead3dc2118c5fefb5d4d7`)에 `Kachou_Shima_Kousaku_KR_V0.2.ips`를 적용하세요. 원본 ROM과 패치 완료 ROM은 배포하지 않습니다. 기존 SRAM은 백업하고 새 게임으로 먼저 확인해 주세요.

GitHub가 자동으로 표시하는 `Source code (zip/tar.gz)`는 옛 V0.2 태그의 스냅샷입니다. **이번 빌드는 아래 첨부 IPS와 EXE를 사용하세요.**

| 파일 | SHA-256 |
| --- | --- |
| V0.2 IPS | `b88ba1859862272934ab2fde3b2c9dbea987f74e37ad4e75db45807ced99c972` |
| 대본 수정 EXE | `b31e4b7ede04988c1545443f73c26e8ca82c87341f4311ff79327ac6764074eb` |
| 패치 결과 ROM | `adeccae271103783dfe68df0c8c8cf730a9dd7dd078af09383eff55595ed5394` |

확인한 범위는 IPS 적용 결과의 바이트 일치, 등록 대사 4,879칸의 화면 넘김 수 일치, 새 게임의 일부 원판·한글판 화면 대조, DATA 2 재시작 후 A/X 경로의 거리 배경 각 39프레임 일치, 대본 수정 EXE 자체 검사·CSV 왕복·창 실행입니다. [검증 기록](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/blob/main/docs/current_validation.json)에 범위와 남은 작업을 적었습니다.
