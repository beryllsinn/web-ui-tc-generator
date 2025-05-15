````markdown
# 🧪 Web UI 테스트케이스 자동 생성기

LangChain + GPT + Playwright 기반  
**웹 UI 구성 요소를 분석하여 테스트케이스(Test Case)를 자동 생성하고 CSV로 저장하는 Python 프로젝트**입니다.

---

## 📌 주요 기능

- ✅ 웹 페이지의 실제 UI 텍스트를 실시간으로 추출
- ✅ LangChain + GPT를 통해 테스트케이스 자동 생성
- ✅ 컴포넌트 구조, 반응형, 유효성 등 UI 테스트 기준 반영
- ✅ 생성된 테스트케이스를 CSV 파일로 저장
- ✅ 확장 가능한 프롬프트 기반 구조

---

## 💡 기술 스택

| 구성 요소 | 설명 |
|-----------|------|
| **LangChain** | GPT 호출을 체인으로 관리 |
| **OpenAI GPT-3.5** | 테스트케이스 생성 |
| **Playwright** | URL 내 웹페이지의 전체 텍스트 수집 |
| **Python** | 전체 로직 구현 |
| **CSV** | 결과 저장 포맷 |

---

## 🚀 실행 방법

### 1. 패키지 설치

```bash
pip install -r requirements.txt
python -m playwright install
````

### 2. 환경변수 설정

```bash
export OPENAI_API_KEY=your-openai-key  # macOS/Linux
set OPENAI_API_KEY=your-openai-key     # Windows
```

### 3. 실행

```bash
python main.py
```

> 실행 후 `web_ui_test_cases_YYYYMMDD_HHMMSS.csv` 파일이 생성됩니다.

---

## 📂 프로젝트 구조

```
.
├── main.py              # 전체 자동화 코드
├── requirements.txt     # 설치해야 할 패키지 목록
├── README.md            # 현재 문서
└── .gitignore           # 불필요 파일 제외 설정
```

---

## 📌 프롬프트 기준 (내부에 적용됨)

* 컴포넌트 디자인 요소 (레이아웃, 색상 등)
* 반응형 분기점
* 작동 여부 (버튼, 스크롤, 입력 등)
* 상태(active/disabled 등)
* 동적 데이터 노출 여부
* 유효성 검사 반응

---

## 🧠 향후 개선 아이디어

* [ ] Slack 슬래시 명령어 연동
* [ ] Prompt 템플릿 버전 관리 (`.md` / `.yaml`)
* [ ] 다국어 테스트케이스 대응
* [ ] RAG 기반 기획서 + 화면 동시 분석

---

## 🧷 라이선스

MIT License

```

---
