# 과장 시마 고사쿠 슈퍼 비즈니스 어드벤처 한글 패치

**V0.8 · 2026-10-17 · 한글화 기타 깎는 노인**

슈퍼패미컴 일본판 《과장 시마 고사쿠 슈퍼 비즈니스 어드벤처》의 비공식 한글 패치입니다. 회사원 시마 고사쿠의 업무와 인간관계를 대사와 선택지로 따라가는 게임입니다.

**[V0.8 다운로드](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/tag/V0.8) · [Windows 패처 포함 ZIP](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/V0.8/Kachou_Shima_Kousaku_KR_V0.8.zip) · [스크린샷 49장](docs/SCREENSHOTS.md) · [파일별 전체 해시](docs/HASHES.md)**

## V0.8 주요 내용

- 등록 10,414항목을 기준으로 검수 승인 10,406항목, 보존한 비대사 제어 8항목입니다. 본편 대사의 의미·말투·인명·직함·조사·공용 문구와 줄바꿈을 재검토했습니다.
- 오프닝에서 빠져 있던 **인물 소개문·임명장·별도 대기 데모 대사 9곳**을 한글화했습니다.
- 줌아웃 끝에서 로고가 잠깐 좌우로 벌어지는 현상과, 타이틀에서 기다리면 그래픽이 깨지는 현상을 수정했습니다. 시작 버튼으로 오프닝을 건너뛰는 경로도 보완했습니다.
- 원판 그림과 원래 영어 문구를 유지합니다. 원판 **完**과 아래 중앙 정렬한 **한글화 기타 깎는 노인**도 유지합니다.
- **설치 없는 Windows 64비트 패처**를 제공합니다. 원본 SHA-256 검사, 복사기 헤더 처리, 내장 IPS 적용, 저장 파일의 SHA-256 검사를 한 번에 수행합니다.

## 다운로드와 적용

1. [패처 포함 ZIP](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/V0.8/Kachou_Shima_Kousaku_KR_V0.8.zip)을 받아 압축을 풉니다.
2. `KachouShimaKRPatcher-V0.8.exe`를 실행하고 일본판 원본 `.sfc` 또는 `.smc`를 선택합니다. ROM이 ZIP 안에 있으면 먼저 압축을 풉니다.
3. 저장할 이름을 확인하고 **한글 패치 적용**을 누릅니다.
4. 완료 메시지에 해시 검증 통과가 표시되면 새로 생성한 한글 ROM을 실행합니다.

원본과 이미 존재하는 출력 파일을 덮어쓰지 않습니다. 지원하는 일본판 본문에 512바이트 복사기 헤더가 붙어 있으면 본문을 검증하고 헤더를 자동 제거합니다. 이전 패치가 적용된 ROM에는 원본용 IPS를 중복 적용하지 않습니다.

| 다운로드 | 내용 |
| --- | --- |
| [패처 포함 ZIP](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/V0.8/Kachou_Shima_Kousaku_KR_V0.8.zip) | 패처 EXE·IPS·적용 안내·해시·폰트 고지 |
| [패처 EXE](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/V0.8/KachouShimaKRPatcher-V0.8.exe) | IPS 내장, 별도 Python 설치 불필요 |
| [IPS 파일](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/V0.8/Kachou_Shima_Kousaku_KR_V0.8.ips) | 다른 IPS 도구로 직접 적용할 때 사용 |
| [대본 도구](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/V0.8/KachouShimaDialogueEditor-V0.8.exe) | 대본 검색·열람·CSV 내보내기/가져오기 |
| [SHA256SUMS.txt](https://github.com/OldManCraveGuitars-bit/SFC-Kachou-Shima-Kousaku-Super-Business-Adventure-KR/releases/download/V0.8/SHA256SUMS.txt) | 배포 파일의 SHA-256 |

원본 ROM과 패치 완료 ROM은 배포하지 않습니다. GitHub의 `Source code`에는 이 버전의 IPS·패처 소스·문서·스크린샷이 들어 있습니다. 실행할 Windows EXE는 위 릴리스 첨부 파일로 받으세요.

## 원본과 결과 확인

| 파일 | 크기(bytes) | SHA-256 |
| --- | ---: | --- |
| 일본판 원본 ROM | 1,048,576 | `988eeb2c00dedecbf18f1eb22b5c462b604ac2863a9ead3dc2118c5fefb5d4d7` |
| V0.8 IPS | 465,823 | `b76f7b1e1136cfb6d5beada07d53b501fdf66f9a740d36f63b4510e7e959dfe9` |
| 정상 패치 결과 ROM | 2,097,152 | `92f03ebb46760334a2d26daa21b74816031a4b0897987d32a5b2ed9db6330d06` |

원본 이름: `Kachou Shima Kousaku (Japan)` · 헤더 없는 1MB 원본 → 헤더 없는 2MB 결과. [SHA-1·MD5·CRC32와 전체 파일 해시](docs/HASHES.md), [기계 판독용 목록](docs/release_manifest.json)을 함께 제공합니다.

## 화면

오프닝·본편·선택지를 포함한 **[전체 49장 갤러리](docs/SCREENSHOTS.md)** 입니다. 아래는 대표 화면입니다.

| 한글 메인 타이틀 | 한글 임명장 |
| --- | --- |
| ![한글 메인 타이틀](screenshots/v0.8/01-opening.png) | ![한글 임명장](screenshots/v0.8/03-opening.png) |

| 인물 소개 · 이름과 소속 | 대기 데모 · 부하 직원 |
| --- | --- |
| ![인물 소개 · 이름과 소속](screenshots/v0.8/04-opening.png) | ![대기 데모 · 부하 직원](screenshots/v0.8/08-opening.png) |

| 대기 데모 · 상사 지시 | 대기 데모 · 동료 |
| --- | --- |
| ![대기 데모 · 상사 지시](screenshots/v0.8/09-opening.png) | ![대기 데모 · 동료](screenshots/v0.8/10-opening.png) |

| 업무 선택지 | 본편 대사 |
| --- | --- |
| ![업무 선택지](screenshots/v0.8/15-chapter-0.png) | ![본편 대사](screenshots/v0.8/21-chapter-3.png) |

| 본편 대사 | 교토 지사 소개 |
| --- | --- |
| ![본편 대사](screenshots/v0.8/26-chapter-4.png) | ![교토 지사 소개](screenshots/v0.8/33-chapter-5.png) |

| 비즈니스 칼럼 | 인물 직함 표기 |
| --- | --- |
| ![비즈니스 칼럼](screenshots/v0.8/38-chapter-5.png) | ![인물 직함 표기](screenshots/v0.8/48-chapter-6.png) |

## 검증 범위

- 원본에 IPS를 적용한 결과가 위의 최종 ROM SHA-256과 일치합니다.
- **561본문·150선택지표·별도 오프닝 대본**의 화자·대기·장면·페이지 명령을 대조했고 차이 0건입니다. 등록 10,414항목의 페이지 넘김 불일치도 0건입니다.
- Snes9x 22,000프레임의 연속 데모와 bsnes 12,000프레임의 데모·다음 타이틀, 시작 버튼·조기 건너뛰기·리셋을 확인했습니다.
- 기존에 확인한 15개 연결 결말과 대표 SRAM 저장 검증은 본편·결말 데이터의 동일성 대조와 함께 유지했습니다. 이번 오프닝 수정본으로 15결말을 모두 새로 재생한 검사는 아닙니다.
- 대본 도구는 10,414항목을 내장하며, 실제 8개 대사의 수정·저장·ROM 재생성·재추출을 확인했습니다. 전용 패처는 단위 검사 12개와 실제 EXE 검사 8개를 통과했습니다.

모든 선택 조합과 모든 휴대 기기에서의 동작을 보장하는 검사는 아닙니다. [검증 기록](docs/current_validation.json)과 [스크린샷 출처](docs/screenshot_manifest.json)에 범위를 명시했습니다.

## 저장 파일과 대본 도구

업데이트 전에는 `.srm` SRAM을 백업해 주세요. 변경 전의 에뮬레이터 저장 상태에는 화면 메모리가 남을 수 있으므로, 업데이트 확인은 ROM을 완전히 다시 시작한 뒤 진행하는 편이 좋습니다.

대본 도구는 일본어 원문·한글·문맥·화자·말투·원판 바이트·줄바꿈을 검색하고 CSV로 내보내거나 가져올 수 있습니다. **수정한 대본으로 ROM을 다시 만드는 기능은 원본 ROM과 개발 프로젝트가 있는 환경에서 사용합니다.** 패처 ZIP은 일반 사용자용 적용 묶음입니다.

## 패처 소스

Python CLI는 외부 패키지 없이 실행할 수 있습니다. Python 3.10 이상에서 저장소 소스를 내려받은 뒤 실행합니다.

```sh
python3 patcher/patcher.py --input "original.sfc" --output "Shima_KR_V0.8.sfc"
```

Windows EXE 빌드: [`patcher/build_windows.ps1`](patcher/build_windows.ps1). 검사 코드는 [`tests/`](tests/)에 있습니다.

## 제작·변경 기록

**한글화: 기타 깎는 노인** · [변경 기록](CHANGELOG.md) · [V0.8 릴리스 노트](RELEASE_NOTES_V0.8.md) · [배포 및 권리 안내](NOTICE.md)

게임·원작·등장인물·원본 그림과 음악의 권리는 각 권리자에게 있습니다. 이 작업은 비공식 팬 한글화입니다. 사용한 폰트의 저작권 표기와 OFL 전문은 [`licenses/`](licenses/)에 있습니다.
