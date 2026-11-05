import streamlit as st
import pandas as pd

# =====================================================================
# 1. БАПТАУЛАР: өз деректеріңізге ауыстырыңыз
# =====================================================================
AUTHOR = {
    "name": "Тегі Аты Әкесінің аты",
    "status": "2 курс магистранты, «Информатика және педагогика» мамандығы",
    "university": "Университет атауы",
    "supervisor": "Ғылыми жетекші: аты-жөні, ғылыми дәрежесі, лауазымы",
    "email": "your.email@example.com",
    "github": "https://github.com/your-nickname",
    "telegram": "https://t.me/your_nickname",
}

THESIS = {
    "title": "Оқушылардың дара оқу траекториясын қолдайтын және персонализация "
             "элементтері бар адаптивті платформа әзірлеу әдістемесі",
    "goal": "Оқу контентін персонализациялауды және дара оқу траекториясын құруды "
            "қамтамасыз ететін адаптивті білім беру платформасын құру әдістемесін "
            "әзірлеу және ғылыми негіздеу.",
    "object": "Цифрлық білім беру платформаларын қолдана отырып информатиканы оқыту процесі.",
    "subject": "Персонализациясы бар және дара оқу траекториясын қолдайтын адаптивті "
               "платформа әзірлеу әдістемесі.",
    "hypothesis": "Ұсынылған әдістеме бойынша құрылған адаптивті платформаны қолдану "
                  "дәстүрлі оқытумен салыстырғанда оқушылардың оқу нәтижелері мен "
                  "уәждемесін арттырады.",
    "tasks": [
        "Адаптивті оқыту мен персонализацияның теориялық негіздерін талдау.",
        "Қолданыстағы адаптивті платформалар мен оқушы модельдеріне шолу жасау.",
        "Оқушы моделін және пәндік аймақ моделін (білім графын) әзірлеу.",
        "Дара білім беру траекториясын құру алгоритмін жасау.",
        "Платформа прототипін және әдістемелік материалдарды іске асыру.",
        "Педагогикалық эксперимент өткізіп, әдістеменің тиімділігін бағалау.",
    ],
    "novelty": "Білім деңгейін диагностикалауды, оқу стилін есепке алуды және тақырыптар "
               "арасындағы тәуелділік графын біріктіретін, оқу траекториясын автоматты "
               "түрде құруға арналған әдістеме ұсынылды.",
    "stage": 60,  # диссертацияның дайындығы, %
}

STAGES = [
    ("Теориялық талдау және әдебиетке шолу", 100),
    ("Оқушы моделін және білім графын жобалау", 80),
    ("Платформа прототипін әзірлеу", 60),
    ("Педагогикалық эксперимент", 30),
    ("Нәтижелерді өңдеу және диссертацияны рәсімдеу", 10),
]

PUBLICATIONS = [
    {"year": 2025, "type": "Мақала", "title": "1-мақаланың атауы",
     "venue": "Журнал / жинақ атауы", "abstract": "Мақаланың қысқаша аннотациясы.", "link": ""},
    {"year": 2025, "type": "Баяндама", "title": "Конференциядағы баяндама атауы",
     "venue": "Конференция атауы, қала", "abstract": "Баяндаманың қысқаша аннотациясы.", "link": ""},
    {"year": 2024, "type": "Шолу", "title": "Адаптивті платформаларға талдамалық шолу",
     "venue": "Ғылыми жұмыс", "abstract": "Платформаларды бейімделгіштік критерийлері бойынша салыстыру.", "link": ""},
]

MATERIALS = [
    {"topic": "Python негіздері", "kind": "Сабақ", "level": "Бастапқы",
     "desc": "Айнымалылар, деректер типтері, енгізу-шығару.", "link": ""},
    {"topic": "Python негіздері", "kind": "Практикум", "level": "Орта",
     "desc": "Циклдар, шарттар және функциялар: есептер жинағы.", "link": ""},
    {"topic": "Алгоритмдер", "kind": "Презентация", "level": "Орта",
     "desc": "Сұрыптау және іздеу, күрделілікті бағалау.", "link": ""},
    {"topic": "Деректер қоры", "kind": "Тест", "level": "Жоғары",
     "desc": "SQL бойынша диагностикалық тест.", "link": ""},
]

# Демо-траекторияға арналған модульдер: тақырып -> (атауы, күрделілігі 1-3, форматы)
DEMO_MODULES = {
    "Алгоритмдік ойлау": [
        ("Алгоритм ұғымы", 1, "бейне"), ("Блок-сызбалар", 2, "практика"), ("Күрделілікті бағалау", 3, "мәтін")],
    "Бағдарламалау": [
        ("Айнымалылар және типтер", 1, "бейне"), ("Циклдар мен шарттар", 2, "практика"), ("Рекурсия", 3, "мәтін")],
    "Деректер және ДҚ": [
        ("Кестелер мен кілттер", 1, "мәтін"), ("SELECT сұраныстары", 2, "практика"), ("JOIN байланыстары", 3, "бейне")],
    "Цифрлық сауаттылық": [
        ("Желідегі қауіпсіздік", 1, "бейне"), ("Кестелермен жұмыс", 2, "практика"), ("Деректерді талдау", 3, "мәтін")],
}
FORMATS = ["бейне", "практика", "мәтін"]

# =====================================================================
# 2. ӘСЕМДЕУ
# =====================================================================
st.set_page_config(page_title="Магистрант портфолиосы", page_icon="🎓", layout="wide")

st.markdown("""
<style>
.hero {padding: 1.6rem 1.8rem; border-radius: 14px;
       background: linear-gradient(135deg,#1e3a8a,#3b82f6); color:#fff; margin-bottom:1rem;}
.hero h1 {color:#fff; font-size:1.7rem; margin:0 0 .5rem 0;}
.hero p {margin:.15rem 0; opacity:.95;}
.card {border:1px solid rgba(128,128,128,.3); border-radius:12px; padding:1rem 1.2rem;
       margin-bottom:.8rem;}
.tag {display:inline-block; padding:2px 10px; border-radius:20px; font-size:.78rem;
      background:rgba(59,130,246,.15); margin-right:6px;}
</style>
""", unsafe_allow_html=True)

# =====================================================================
# 3. НАВИГАЦИЯ
# =====================================================================
PAGES = ["🏠 Басты бет", "📖 Диссертация туралы", "📚 Жарияланымдар мен зерттеулер",
         "🧩 Оқу материалдары", "🧭 Демо: дара траектория", "✉️ Байланыс"]

with st.sidebar:
    st.title("🎓 Портфолио")
    page = st.radio("Бөлім", PAGES, label_visibility="collapsed")
    st.divider()
    st.caption(AUTHOR["name"])
    st.caption(AUTHOR["university"])


def tag(text):
    return f'<span class="tag">{text}</span>'


# ------------------------------------------------------------ Басты бет
if page == PAGES[0]:
    st.markdown(f"""
    <div class="hero">
      <h1>{THESIS['title']}</h1>
      <p><b>{AUTHOR['name']}</b></p>
      <p>{AUTHOR['status']}</p>
      <p>{AUTHOR['university']} · {AUTHOR['supervisor']}</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    c1.metric("Жарияланымдар мен баяндамалар", len(PUBLICATIONS))
    c2.metric("Оқу материалдары", len(MATERIALS))
    c3.metric("Диссертация дайындығы", f"{THESIS['stage']}%")

    st.subheader("Зерттеу мақсаты")
    st.write(THESIS["goal"])

    st.subheader("Жұмыс кезеңдері")
    for name, pct in STAGES:
        st.write(name)
        st.progress(pct / 100)

# ------------------------------------------------------ Диссертация туралы
elif page == PAGES[1]:
    st.header("Диссертация туралы")
    st.subheader("Тақырып")
    st.write(THESIS["title"])

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Зерттеу объектісі**")
        st.write(THESIS["object"])
        st.markdown("**Зерттеу пәні**")
        st.write(THESIS["subject"])
    with col2:
        st.markdown("**Гипотеза**")
        st.write(THESIS["hypothesis"])
        st.markdown("**Ғылыми жаңалығы**")
        st.write(THESIS["novelty"])

    st.subheader("Зерттеу міндеттері")
    for i, t in enumerate(THESIS["tasks"], 1):
        st.write(f"{i}. {t}")

    st.subheader("Адаптивті платформа архитектурасы")
    st.graphviz_chart("""
    digraph G {
        rankdir=LR; node [shape=box, style="rounded,filled", fillcolor="#dbeafe"];
        "Оқушы" -> "Диагностика";
        "Диагностика" -> "Оқушы моделі";
        "Оқушы моделі" -> "Бейімделу механизмі";
        "Білім графы" -> "Бейімделу механизмі";
        "Материалдар қоры" -> "Бейімделу механизмі";
        "Бейімделу механизмі" -> "Дара траектория";
        "Дара траектория" -> "Оқушы";
        "Дара траектория" -> "Аналитика" -> "Оқушы моделі";
    }
    """)

# ------------------------------------------------------------ Жарияланымдар
elif page == PAGES[2]:
    st.header("Жарияланымдар мен зерттеулер")
    years = sorted({p["year"] for p in PUBLICATIONS}, reverse=True)
    types = sorted({p["type"] for p in PUBLICATIONS})
    c1, c2 = st.columns(2)
    sel_years = c1.multiselect("Жыл", years, default=years)
    sel_types = c2.multiselect("Түрі", types, default=types)

    for p in sorted(PUBLICATIONS, key=lambda x: -x["year"]):
        if p["year"] in sel_years and p["type"] in sel_types:
            st.markdown(
                f'<div class="card">{tag(p["type"])}{tag(p["year"])}'
                f'<h4 style="margin:.5rem 0 .2rem 0">{p["title"]}</h4>'
                f'<i>{p["venue"]}</i><p>{p["abstract"]}</p></div>',
                unsafe_allow_html=True)
            if p["link"]:
                st.link_button("Ашу", p["link"])

    with st.expander("Әдебиеттер тізімі (үлгі)"):
        for i, p in enumerate(PUBLICATIONS, 1):
            st.write(f"{i}. {AUTHOR['name']}. {p['title']} // {p['venue']}. {p['year']}.")

# ------------------------------------------------------------ Оқу материалдары
elif page == PAGES[3]:
    st.header("Оқу материалдары")
    df = pd.DataFrame(MATERIALS)
    ALL = "Барлығы"
    c1, c2, c3 = st.columns(3)
    topic = c1.selectbox("Тақырып", [ALL] + sorted(df["topic"].unique()))
    kind = c2.selectbox("Формат", [ALL] + sorted(df["kind"].unique()))
    level = c3.selectbox("Деңгей", [ALL] + sorted(df["level"].unique()))

    view = df.copy()
    if topic != ALL:
        view = view[view["topic"] == topic]
    if kind != ALL:
        view = view[view["kind"] == kind]
    if level != ALL:
        view = view[view["level"] == level]

    if view.empty:
        st.info("Таңдалған сүзгілер бойынша материал жоқ.")
    for _, m in view.iterrows():
        st.markdown(
            f'<div class="card">{tag(m["kind"])}{tag(m["level"])}'
            f'<h4 style="margin:.5rem 0 .2rem 0">{m["topic"]}</h4>{m["desc"]}</div>',
            unsafe_allow_html=True)
        if m["link"]:
            st.link_button("Материалға өту", m["link"])

    st.subheader("Материалмен файл жүктеу")
    st.caption("Демонстрация: файл тек ағымдағы сессияда ғана қолжетімді.")
    f = st.file_uploader("PDF, DOCX, PPTX", type=["pdf", "docx", "pptx"])
    if f:
        st.success(f"«{f.name}» файлы жүктелді.")
        st.download_button("Қайта жүктеп алу", f.getvalue(), file_name=f.name)

# ------------------------------------------------------------------- Демо
elif page == PAGES[4]:
    st.header("Демо: дара оқу траекториясын құру")
    st.write("Адаптивті механизм жұмысының жеңілдетілген моделі: оқушының өзіндік бағасы, "
             "оқу стилі және уақыты бойынша жүйе модульдерді таңдап, ретке келтіреді.")

    with st.form("profile"):
        name = st.text_input("Оқушының аты", "Оқушы")
        st.markdown("**Деңгейіңізді бағалаңыз (0 — білмеймін, 10 — сенімді меңгердім)**")
        scores = {t: st.slider(t, 0, 10, 4) for t in DEMO_MODULES}
        style = st.radio("Қалаулы формат", FORMATS, horizontal=True)
        hours = st.slider("Аптасына сағат саны", 1, 15, 5)
        ok = st.form_submit_button("Траектория құру")

    if ok:
        rows = []
        for topic, mods in DEMO_MODULES.items():
            s = scores[topic]
            target = 1 if s < 4 else 2 if s < 7 else 3   # мақсатты күрделілік
            for title, diff, fmt in mods:
                gap = max(0, 10 - s)                      # әлсіз тақырыптың басымдығы
                fit = 3 - abs(diff - target)              # күрделілікке сәйкестік
                bonus = 1.5 if fmt == style else 0        # оқу стилін есепке алу
                rows.append({"Тақырып": topic, "Модуль": title, "Күрделілік": diff,
                             "Формат": fmt, "Басымдық": round(gap * 0.4 + fit + bonus, 2)})
        plan = (pd.DataFrame(rows).sort_values("Басымдық", ascending=False)
                .head(max(3, hours)).reset_index(drop=True))
        plan.index += 1
        plan["Уақыт, сағ"] = 1

        st.success(f"Дара траектория: {name}")
        st.dataframe(plan, use_container_width=True)
        st.subheader("Білім профилі")
        st.bar_chart(pd.Series(scores, name="Деңгей"))
        st.caption(f"Барлығы {len(plan)} модуль · шамамен {plan['Уақыт, сағ'].sum()} сағат.")

# ----------------------------------------------------------------- Байланыс
else:
    st.header("Байланыс")
    st.write(f"**{AUTHOR['name']}**")
    st.write(AUTHOR["status"])
    st.write(AUTHOR["supervisor"])
    st.write(f"📧 {AUTHOR['email']}")
    c1, c2 = st.columns(2)
    c1.link_button("GitHub", AUTHOR["github"])
    c2.link_button("Telegram", AUTHOR["telegram"])

    st.subheader("Кері байланыс")
    with st.form("feedback"):
        n = st.text_input("Атыңыз")
        msg = st.text_area("Материалдар туралы хабарлама немесе пікір")
        if st.form_submit_button("Жіберу") and msg:
            st.success("Рахмет! Хабарлама алынды (демо нұсқада сақталмайды).")
