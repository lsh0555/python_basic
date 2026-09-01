import csv
from datetime import datetime
from pathlib import Path

import streamlit as st


# 이 파일과 sample_expenses.csv를 같은 폴더에 둡니다.
CSV_PATH = Path(__file__).resolve().parent / "sample_expenses.csv"


def normalize_date(value):
    for date_format in ("%Y-%m-%d", "%Y%m%d"):
        try:
            return datetime.strptime(value, date_format).strftime("%Y-%m-%d")
        except ValueError:
            pass
    return value


def load_expenses():
    expenses = []

    try:
        with CSV_PATH.open("r", encoding="utf-8-sig", newline="") as file:
            for row in csv.DictReader(file):
                try:
                    row["amount"] = int(row["amount"])
                except (KeyError, ValueError, TypeError):
                    continue

                row["date"] = normalize_date(row.get("date", ""))
                expenses.append(row)
    except FileNotFoundError:
        pass

    return expenses


def save_expenses(expenses):
    fieldnames = ["date", "category", "description", "amount"]

    with CSV_PATH.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)


def category_summary(expenses):
    totals = {}
    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0) + expense["amount"]
    return totals


st.set_page_config(
    page_title="가계부",
    page_icon="🍂",
    layout="centered",
)

# 별도의 이미지 파일 없이 CSS와 이모지만으로 만든 밝은 가을 테마입니다.
st.markdown(
    """
    <style>
    :root {
        --cream: #fffaf0;
        --paper: #fffdf8;
        --pumpkin: #d86f35;
        --pumpkin-dark: #a74822;
        --maple: #8f3f2c;
        --brown: #513528;
        --sage: #718355;
        --peach: #f7dfc2;
    }

    .stApp {
        background: linear-gradient(145deg, #fff8e8 0%, #f9ead7 55%, #f5dcc5 100%);
        color: var(--brown);
    }

    /* 배경의 동그라미 대신 만든 낙엽 장식 */
    .stApp::before,
    .stApp::after {
        content: "";
        position: fixed;
        z-index: 0;
        width: 155px;
        height: 205px;
        pointer-events: none;
        opacity: .72;
        border-radius: 100% 0 100% 0;
        box-shadow: 0 12px 24px rgba(128, 65, 30, .12);
    }

    .stApp::before {
        top: -35px;
        left: 38px;
        transform: rotate(-32deg);
        background:
            linear-gradient(43deg, transparent 48.5%, rgba(131, 75, 38, .42) 49%, rgba(131, 75, 38, .42) 51%, transparent 51.5%),
            linear-gradient(135deg, #f4c975 0%, #dc873f 58%, #b9582f 100%);
    }

    .stApp::after {
        top: 105px;
        right: 58px;
        width: 135px;
        height: 180px;
        transform: rotate(54deg);
        background:
            linear-gradient(43deg, transparent 48.5%, rgba(119, 63, 35, .42) 49%, rgba(119, 63, 35, .42) 51%, transparent 51.5%),
            linear-gradient(135deg, #e5a56e 0%, #c76b3f 58%, #98422c 100%);
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    .block-container {
        position: relative;
        z-index: 1;
        max-width: 860px;
        padding-top: 2.2rem;
        padding-bottom: 3rem;
    }

    .autumn-hero {
        padding: 2rem 1.5rem 1.65rem;
        margin-bottom: 1.5rem;
        text-align: center;
        color: var(--brown);
        background: rgba(255, 253, 248, 0.92);
        border: 2px solid #edc89d;
        border-radius: 28px;
        box-shadow: 0 12px 30px rgba(119, 67, 38, 0.13);
    }

    .autumn-hero h1 {
        margin: 0;
        color: var(--maple);
        font-size: 2.35rem;
        letter-spacing: -0.06rem;
    }

    .autumn-hero p {
        margin: .55rem 0 0;
        color: #80604e;
        font-size: 1.02rem;
    }

    h2, h3, label, p, span, [data-testid="stMarkdownContainer"] {
        color: var(--brown);
    }

    h3 {
        color: var(--maple) !important;
        margin-top: 1.25rem !important;
    }

    [data-testid="stForm"],
    [data-testid="stMetric"],
    [data-testid="stDataFrame"],
    [data-testid="stTable"] {
        background: rgba(255, 253, 248, 0.94);
        border: 1px solid #e9c79f;
        border-radius: 20px;
        box-shadow: 0 8px 22px rgba(113, 68, 39, 0.09);
    }

    [data-testid="stForm"] {
        padding: 1.2rem 1.25rem .7rem;
    }

    [data-testid="stMetric"] {
        padding: 1rem 1.25rem;
        border-left: 7px solid var(--pumpkin);
    }

    [data-testid="stMetricValue"] {
        color: var(--maple);
    }

    input, [data-baseweb="input"] > div {
        background: #fffaf2 !important;
        color: var(--brown) !important;
        border-radius: 12px !important;
    }

    input::placeholder {
        color: #aa8976 !important;
    }

    .stButton > button,
    .stFormSubmitButton > button {
        min-height: 2.8rem;
        color: white !important;
        background: linear-gradient(135deg, var(--pumpkin), var(--pumpkin-dark));
        border: 0;
        border-radius: 999px;
        box-shadow: 0 6px 14px rgba(167, 72, 34, 0.22);
        font-weight: 700;
        transition: transform .15s ease, box-shadow .15s ease;
    }

    .stButton > button:hover,
    .stFormSubmitButton > button:hover {
        color: white !important;
        transform: translateY(-2px);
        box-shadow: 0 9px 18px rgba(167, 72, 34, 0.28);
    }

    hr {
        border-color: #dfb98d !important;
    }

    .autumn-footer {
        margin-top: 2rem;
        text-align: center;
        color: #8b6a57;
        font-size: .9rem;
    }
    </style>

    <div class="autumn-hero">
        <div style="font-size: 2rem; margin-bottom: .3rem;">🍂 🐻 🐝</div>
        <h1>가계부</h1>
        <p>차곡차곡 기록하며 알뜰한 하루를 모아보세요.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# 입력할 때마다 화면이 다시 실행되므로 목록을 session_state에 보관합니다.
if "expenses" not in st.session_state:
    st.session_state.expenses = load_expenses()

expenses = st.session_state.expenses

st.subheader("🧺 새 지출 담기")
with st.form("expense_form", clear_on_submit=True):
    date = st.date_input("날짜")
    category = st.text_input("카테고리", placeholder="예: 식비")
    description = st.text_input("내용", placeholder="예: 점심")
    amount = st.number_input("금액", min_value=1, step=100, format="%d")
    submitted = st.form_submit_button("지출 추가", type="primary")

if submitted:
    category = category.strip()
    description = description.strip()

    if not category or not description:
        st.error("카테고리와 내용을 모두 입력해 주세요.")
    else:
        expenses.append(
            {
                "date": date.strftime("%Y-%m-%d"),
                "category": category,
                "description": description,
                "amount": int(amount),
            }
        )
        st.success("추가했습니다. 아래 저장 버튼을 눌러 CSV에 저장하세요.")

st.divider()
st.metric("🍂 지금까지 쓴 금액", f"{sum(item['amount'] for item in expenses):,}원")

st.subheader("📒 지출 내역")
if expenses:
    table_rows = [
        {
            "날짜": item["date"],
            "카테고리": item["category"],
            "내용": item["description"],
            "금액": f"{item['amount']:,}원",
        }
        for item in expenses
    ]
    st.dataframe(table_rows, use_container_width=True, hide_index=True)
else:
    st.info("등록된 지출이 없습니다.")

st.subheader("🐝 카테고리별 합계")
totals = category_summary(expenses)
if totals:
    st.table(
        [
            {"카테고리": category, "합계": f"{amount:,}원"}
            for category, amount in totals.items()
        ]
    )
else:
    st.info("표시할 요약이 없습니다.")

if st.button("CSV 파일에 저장"):
    try:
        save_expenses(expenses)
        st.success(f"{CSV_PATH.name}에 저장했습니다.")
    except OSError as error:
        st.error(f"저장하지 못했습니다: {error}")