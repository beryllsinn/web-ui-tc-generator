import csv
import os
from datetime import datetime
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from playwright.sync_api import sync_playwright

# ✅ STEP 1: 웹사이트에서 텍스트 추출
def extract_text_from_url(url: str) -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto(url, timeout=10000)
            page.wait_for_timeout(3000)
            full_text = page.inner_text("body")
        except Exception as e:
            print(f"[❌ Error] 페이지 로드 실패: {e}")
            full_text = ""
        finally:
            browser.close()
        return full_text

# ✅ STEP 2: GPT 모델 연결 (환경변수로 키 관리)
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY 환경변수가 설정되어 있지 않습니다.")

llm = ChatOpenAI(
    model="gpt-3.5-turbo",  # 또는 "gpt-4"
    temperature=0.3,
    openai_api_key=api_key
)

# ✅ STEP 3: 대상 웹페이지 URL
url = "https://www.naver.com"
page_text = extract_text_from_url(url)

# ✅ STEP 4: 테스트케이스 생성 프롬프트
prompt = f"""
당신은 소프트웨어 QA 전문가입니다.
아래 웹페이지의 UI 구성과 주요 요소를 기반으로 테스트케이스를 작성하세요.

## 페이지 텍스트 요약
{page_text[:3000]}

## 테스트케이스 작성 시 반드시 아래 확인사항을 모두 고려하여 작성해주세요.

1. 컴포넌트 디자인 요소 확인 (레이아웃, 색상, 폰트, 아이콘 등)
2. 반응형 분기점 확인 (width 900px 기준)
3. 컴포넌트 작동 여부 (클릭, 입력, 드롭다운, 스크롤, 앱바 등)
4. 컴포넌트 상태 (active/inactive, enabled/disabled 등)
5. 동적 데이터 노출 여부
6. 입력값 유효성 검사 반응

요청: "테스트 ID, 입력값, 예상 결과" 형식으로 10개 이상의 테스트케이스를 작성하세요.
"""

# ✅ STEP 5: GPT 호출
try:
    response = llm([
        SystemMessage(content="당신은 QA 전문가입니다."),
        HumanMessage(content=prompt)
    ])
    test_cases = response.content
except Exception as e:
    print(f"[❌ GPT 호출 실패] {e}")
    exit()

# ✅ STEP 6: 결과 CSV 저장
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
csv_filename = f"web_ui_test_cases_{timestamp}.csv"

with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["테스트 ID", "입력값", "예상 결과"])
    for i, line in enumerate(test_cases.split("\n")):
        if line.strip():
            parts = line.split(":")
            value = parts[1].strip() if len(parts) > 1 else line.strip()
            writer.writerow([f"TC_{i+1:03}", value, ""])

print(f"✅ 테스트 케이스가 '{csv_filename}' 파일로 저장되었습니다.")
