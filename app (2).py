import streamlit as st
import pandas as pd

# =====================================================================
# 1. НАСТРОЙКИ: замените на свои данные
# =====================================================================
AUTHOR = {
    "name": "Жунусова Дильназ Жомарткызы",
    "status": "Магистрант 2 курса, направление «Информатика и педагогика»",
    "university": "Евразийский национальный университет имени Л.Н. Гумилёва (ЕНУ)",
    "supervisor": "Научный руководитель: ФИО, уч. степень, должность",
    "email": "your.email@example.com",
    "github": "https://github.com/your-nickname",
    "telegram": "https://t.me/your_nickname",
}

THESIS = {
    "title": "Методика разработки адаптивной платформы с элементами персонализации "
             "и поддержки индивидуальной траектории обучения учащихся",
    "goal": "Разработать и научно обосновать методику создания адаптивной образовательной "
            "платформы, обеспечивающей персонализацию контента и построение индивидуальной "
            "траектории обучения.",
    "object": "Процесс обучения информатике с использованием цифровых образовательных платформ.",
    "subject": "Методика разработки адаптивной платформы с персонализацией и поддержкой "
               "индивидуальной траектории обучения.",
    "hypothesis": "Использование адаптивной платформы, построенной по предложенной методике, "
                  "повысит учебные результаты и мотивацию учащихся по сравнению с "
                  "традиционной организацией обучения.",
    "tasks": [
        "Проанализировать теоретические основы адаптивного обучения и персонализации.",
        "Выполнить обзор существующих адаптивных платформ и моделей учащегося.",
        "Разработать модель учащегося и модель предметной области (граф знаний).",
        "Создать алгоритм построения индивидуальной образовательной траектории.",
        "Реализовать прототип платформы и методические материалы.",
        "Провести педагогический эксперимент и оценить эффективность методики.",
    ],
    "novelty": "Предложена методика, объединяющая диагностику уровня знаний, учёт стиля "
               "обучения и граф зависимостей тем для автоматического построения траектории.",
    "stage": 60,  # готовность диссертации, %
}

STAGES = [
    ("Теоретический анализ и обзор литературы", 100),
    ("Проектирование модели учащегося и графа знаний", 80),
    ("Разработка прототипа платформы", 60),
    ("Педагогический эксперимент", 30),
    ("Обработка результатов и оформление диссертации", 10),
]

PUBLICATIONS = [
    {"year": 2025, "type": "Статья", "title": "Название статьи 1",
     "venue": "Журнал / сборник", "abstract": "Краткая аннотация статьи.", "link": ""},
    {"year": 2025, "type": "Доклад", "title": "Название доклада на конференции",
     "venue": "Название конференции, город", "abstract": "Краткая аннотация доклада.", "link": ""},
    {"year": 2024, "type": "Обзор", "title": "Аналитический обзор адаптивных платформ",
     "venue": "Курсовая / научная работа", "abstract": "Сравнение платформ по критериям адаптивности.", "link": ""},
]

MATERIALS = [
    {"topic": "Основы Python", "kind": "Урок", "level": "Начальный",
     "desc": "Переменные, типы данных, ввод-вывод.", "link": ""},
    {"topic": "Основы Python", "kind": "Практикум", "level": "Средний",
     "desc": "Циклы, условия и функции: набор задач.", "link": ""},
    {"topic": "Алгоритмы", "kind": "Презентация", "level": "Средний",
     "desc": "Сортировка и поиск, оценка сложности.", "link": ""},
    {"topic": "Базы данных", "kind": "Тест", "level": "Продвинутый",
     "desc": "Диагностический тест по SQL.", "link": ""},
]

# Модули для демо-траектории: тема -> (название, сложность 1-3, формат)
DEMO_MODULES = {
    "Алгоритмическое мышление": [
        ("Понятие алгоритма", 1, "видео"), ("Блок-схемы", 2, "практика"), ("Оценка сложности", 3, "текст")],
    "Программирование": [
        ("Переменные и типы", 1, "видео"), ("Циклы и условия", 2, "практика"), ("Рекурсия", 3, "текст")],
    "Данные и БД": [
        ("Таблицы и ключи", 1, "текст"), ("Запросы SELECT", 2, "практика"), ("Соединения JOIN", 3, "видео")],
    "Цифровая грамотность": [
        ("Безопасность в сети", 1, "видео"), ("Работа с таблицами", 2, "практика"), ("Анализ данных", 3, "текст")],
}

# =====================================================================
# 2. ОФОРМЛЕНИЕ
# =====================================================================
st.set_page_config(page_title="Портфолио магистранта", page_icon="🎓", layout="wide")

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
PAGES = ["🏠 Главная", "📖 О диссертации", "📚 Публикации и исследования",
         "🧩 Учебные материалы", "🧭 Демо: индивидуальная траектория", "✉️ Контакты"]

with st.sidebar:
    st.title("🎓 Портфолио")
    page = st.radio("Раздел", PAGES, label_visibility="collapsed")
    st.divider()
    st.caption(AUTHOR["name"])
    st.caption(AUTHOR["university"])


def tag(text):
    return f'<span class="tag">{text}</span>'


# ---------------------------------------------------------------- Главная
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
    c1.metric("Публикации и доклады", len(PUBLICATIONS))
    c2.metric("Учебные материалы", len(MATERIALS))
    c3.metric("Готовность диссертации", f"{THESIS['stage']}%")

    st.info("🤖 В проекте используется машинное обучение (Random Forest) и адаптивное тестирование.")
    st.page_link("pages/1_Adaptive_Test.py", label="Пройти адаптивный тест", icon="🧭")
    st.page_link("pages/2_AI.py", label="ИИ-рекомендации", icon="🤖")

    st.subheader("Цель исследования")
    st.write(THESIS["goal"])

    st.subheader("Этапы работы")
    for name, pct in STAGES:
        st.write(name)
        st.progress(pct / 100)

# ------------------------------------------------------- О диссертации
elif page == PAGES[1]:
    st.header("О диссертации")
    st.subheader("Тема")
    st.write(THESIS["title"])

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Объект исследования**")
        st.write(THESIS["object"])
        st.markdown("**Предмет исследования**")
        st.write(THESIS["subject"])
    with col2:
        st.markdown("**Гипотеза**")
        st.write(THESIS["hypothesis"])
        st.markdown("**Научная новизна**")
        st.write(THESIS["novelty"])

    st.subheader("Задачи исследования")
    for i, t in enumerate(THESIS["tasks"], 1):
        st.write(f"{i}. {t}")

    st.subheader("Архитектура адаптивной платформы")
    st.graphviz_chart("""
    digraph G {
        rankdir=LR; node [shape=box, style="rounded,filled", fillcolor="#dbeafe"];
        "Учащийся" -> "Диагностика";
        "Диагностика" -> "Модель учащегося";
        "Модель учащегося" -> "Движок адаптации";
        "Граф знаний" -> "Движок адаптации";
        "Банк материалов" -> "Движок адаптации";
        "Движок адаптации" -> "Индивидуальная траектория";
        "Индивидуальная траектория" -> "Учащийся";
        "Индивидуальная траектория" -> "Аналитика" -> "Модель учащегося";
    }
    """)

# ----------------------------------------------------------- Публикации
elif page == PAGES[2]:
    st.header("Публикации и исследования")
    years = sorted({p["year"] for p in PUBLICATIONS}, reverse=True)
    types = sorted({p["type"] for p in PUBLICATIONS})
    c1, c2 = st.columns(2)
    sel_years = c1.multiselect("Год", years, default=years)
    sel_types = c2.multiselect("Тип", types, default=types)

    for p in sorted(PUBLICATIONS, key=lambda x: -x["year"]):
        if p["year"] in sel_years and p["type"] in sel_types:
            st.markdown(
                f'<div class="card">{tag(p["type"])}{tag(p["year"])}'
                f'<h4 style="margin:.5rem 0 .2rem 0">{p["title"]}</h4>'
                f'<i>{p["venue"]}</i><p>{p["abstract"]}</p></div>',
                unsafe_allow_html=True)
            if p["link"]:
                st.link_button("Открыть", p["link"])

    with st.expander("Список литературы в формате ГОСТ (шаблон)"):
        for i, p in enumerate(PUBLICATIONS, 1):
            st.write(f"{i}. {AUTHOR['name']}. {p['title']} // {p['venue']}. {p['year']}.")

# ------------------------------------------------------------ Материалы
elif page == PAGES[3]:
    st.header("Учебные материалы")
    df = pd.DataFrame(MATERIALS)
    c1, c2, c3 = st.columns(3)
    topic = c1.selectbox("Тема", ["Все"] + sorted(df["topic"].unique()))
    kind = c2.selectbox("Формат", ["Все"] + sorted(df["kind"].unique()))
    level = c3.selectbox("Уровень", ["Все"] + sorted(df["level"].unique()))

    view = df.copy()
    if topic != "Все":
        view = view[view["topic"] == topic]
    if kind != "Все":
        view = view[view["kind"] == kind]
    if level != "Все":
        view = view[view["level"] == level]

    if view.empty:
        st.info("По выбранным фильтрам материалов нет.")
    for _, m in view.iterrows():
        st.markdown(
            f'<div class="card">{tag(m["kind"])}{tag(m["level"])}'
            f'<h4 style="margin:.5rem 0 .2rem 0">{m["topic"]}</h4>{m["desc"]}</div>',
            unsafe_allow_html=True)
        if m["link"]:
            st.link_button("Перейти к материалу", m["link"])

    st.subheader("Загрузить файл с материалом")
    st.caption("Демонстрация: файл будет доступен только в текущей сессии.")
    f = st.file_uploader("PDF, DOCX, PPTX", type=["pdf", "docx", "pptx"])
    if f:
        st.success(f"Файл «{f.name}» загружен.")
        st.download_button("Скачать обратно", f.getvalue(), file_name=f.name)

# ---------------------------------------------------------------- Демо
elif page == PAGES[4]:
    st.header("Демо: построение индивидуальной траектории")
    st.write("Упрощённая модель работы адаптивного движка: по самооценке учащегося, "
             "стилю обучения и времени система подбирает модули и их порядок.")

    with st.form("profile"):
        name = st.text_input("Имя учащегося", "Учащийся")
        st.markdown("**Оцените свой уровень (0 — не знаю, 10 — уверенно владею)**")
        scores = {t: st.slider(t, 0, 10, 4) for t in DEMO_MODULES}
        style = st.radio("Предпочитаемый формат", ["видео", "практика", "текст"], horizontal=True)
        hours = st.slider("Часов в неделю", 1, 15, 5)
        ok = st.form_submit_button("Построить траекторию")

    if ok:
        rows = []
        for topic, mods in DEMO_MODULES.items():
            s = scores[topic]
            # целевая сложность: чем выше уровень, тем сложнее модуль
            target = 1 if s < 4 else 2 if s < 7 else 3
            for title, diff, fmt in mods:
                gap = max(0, 10 - s)                 # приоритет слабых тем
                fit = 3 - abs(diff - target)         # соответствие сложности
                bonus = 1.5 if fmt == style else 0   # учёт стиля обучения
                rows.append({"Тема": topic, "Модуль": title, "Сложность": diff,
                             "Формат": fmt, "Приоритет": round(gap * 0.4 + fit + bonus, 2)})
        plan = (pd.DataFrame(rows).sort_values("Приоритет", ascending=False)
                .head(max(3, hours)).reset_index(drop=True))
        plan.index += 1
        plan["Время, ч"] = 1

        st.success(f"Индивидуальная траектория для: {name}")
        st.dataframe(plan, use_container_width=True)
        st.subheader("Профиль знаний")
        st.bar_chart(pd.Series(scores, name="Уровень"))
        st.caption(f"Всего модулей: {len(plan)} · ориентировочно {plan['Время, ч'].sum()} ч.")

# ------------------------------------------------------------- Контакты
else:
    st.header("Контакты")
    st.write(f"**{AUTHOR['name']}**")
    st.write(AUTHOR["status"])
    st.write(AUTHOR["supervisor"])
    st.write(f"📧 {AUTHOR['email']}")
    c1, c2 = st.columns(2)
    c1.link_button("GitHub", AUTHOR["github"])
    c2.link_button("Telegram", AUTHOR["telegram"])

    st.subheader("Обратная связь")
    with st.form("feedback"):
        n = st.text_input("Ваше имя")
        msg = st.text_area("Сообщение или отзыв о материалах")
        if st.form_submit_button("Отправить") and msg:
            st.success("Спасибо! Сообщение получено (в демо-версии не сохраняется).")
