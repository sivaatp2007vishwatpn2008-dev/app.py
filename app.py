import streamlit as st

# ---------------------------
# Functions
# ---------------------------
def grade(a):
    if 90 <= a <= 100:
        return "Your Predicted Grade: A+ or O"
    elif 80 <= a < 90:
        return "Your Predicted Grade: A or A+"
    elif 70 <= a < 80:
        return "Your Predicted Grade: B+ or A"
    elif 60 <= a < 70:
        return "Your Predicted Grade: B or B+"
    elif 50 <= a < 60:
        return "Your Predicted Grade: C or B"
    elif a < 50:
        return "Your Predicted Grade: U"
    else:
        return "Invalid Input"

def calc_academic_level(p, q, r, s, present, total):
    set1 = p + (q * 0.6)
    set2 = r + (s * 0.6)
    avg_marks = round((set1 + set2) / 2)
    att_per = round((present / total) * 100)
    return round((avg_marks + att_per) / 2)

def calc_attendance_percentage(present, total):
    return round((present / total) * 100)

def calc_internal_marks(p, q, r, s):
    set1 = p + (q * 0.6)
    set2 = r + (s * 0.6)
    int1 = round(set1 * 0.2)
    int2 = round(set2 * 0.2)
    total_int = int1 + int2
    return int1, int2, total_int

# ---------------------------
# Streamlit UI
# ---------------------------
st.set_page_config(page_title="Student Helper App", page_icon="🎓", layout="centered")
st.markdown("<h1 style='text-align:center; color:#4CAF50;'>🎓 Student Helper App</h1>", unsafe_allow_html=True)

name = st.text_input("👤 Enter your Name").upper()

task = st.selectbox(
    "📌 Choose a Task",
    ["--Select--", "Calculate Academic Level", "Future Grade Prediction", "Calculate Attendance Percentage", "Calculate Internal Marks"]
)

st.markdown("---")

if task == "Calculate Academic Level":
    st.subheader("📊 Academic Level Calculator")
    col1, col2 = st.columns(2)
    with col1:
        p = st.number_input("Internal (IAT) mark /40", min_value=0, max_value=40)
        q = st.number_input("IAT mark /100", min_value=0, max_value=100)
    with col2:
        r = st.number_input("Internal (Model) mark /40", min_value=0, max_value=40)
        s = st.number_input("Model mark /100", min_value=0, max_value=100)

    present = st.number_input("No. of Present Classes", min_value=0)
    total = st.number_input("Total Classes", min_value=1)

    if st.button("Calculate Academic Level"):
        academic_level = calc_academic_level(p, q, r, s, present, total)
        st.success(f"{name}, Your Academic Level: {academic_level}%")

elif task == "Future Grade Prediction":
    st.subheader("🔮 Future Grade Predictor")
    method = st.radio("Do you know your Academic Level?", ["Yes", "No"])

    if method == "Yes":
        g = st.number_input("Enter your Academic Level", min_value=0, max_value=100)
        add = []
        for i in range(1, 5):
            coach = st.number_input(f"Coaching Class Marks - Phase {i}", min_value=0, max_value=100)
            add.append(coach)
        if st.button("Predict Grade"):
            avg_coach = round(sum(add) / 4)
            final_level = round((g + avg_coach) / 2)
            st.info(grade(final_level))
            st.success(f"All the best {name} !!")

    elif method == "No":
        st.write("First, enter your internal and attendance details:")
        col1, col2 = st.columns(2)
        with col1:
            p = st.number_input("Internal (IAT) mark /40", min_value=0, max_value=40)
            q = st.number_input("IAT mark /100", min_value=0, max_value=100)
        with col2:
            r = st.number_input("Internal (Model) mark /40", min_value=0, max_value=40)
            s = st.number_input("Model mark /100", min_value=0, max_value=100)

        present = st.number_input("No. of Present Classes", min_value=0)
        total = st.number_input("Total Classes", min_value=1)

        add = []
        for i in range(1, 5):
            coach = st.number_input(f"Coaching Class Marks - Phase {i}", min_value=0, max_value=100)
            add.append(coach)

        if st.button("Predict Grade"):
            academic_level = calc_academic_level(p, q, r, s, present, total)
            avg_coach = round(sum(add) / 4)
            final_level = round((academic_level + avg_coach) / 2)
            st.info(grade(final_level))
            st.success(f"All the best {name} !!")

elif task == "Calculate Attendance Percentage":
    st.subheader("📅 Attendance Percentage Calculator")
    present = st.number_input("No. of Present Classes", min_value=0)
    total = st.number_input("Total Classes", min_value=1)
    if st.button("Calculate Attendance"):
        att_per = calc_attendance_percentage(present, total)
        st.success(f"{name}, Your Attendance Percentage: {att_per}%")

elif task == "Calculate Internal Marks":
    st.subheader("📝 Internal Marks Calculator")
    col1, col2 = st.columns(2)
    with col1:
        p = st.number_input("Internal (IAT) mark /40", min_value=0, max_value=40)
        q = st.number_input("IAT mark /100", min_value=0, max_value=100)
    with col2:
        r = st.number_input("Internal (Model) mark /40", min_value=0, max_value=40)
        s = st.number_input("Model mark /100", min_value=0, max_value=100)

    if st.button("Calculate Internal Marks"):
        int1, int2, total_int = calc_internal_marks(p, q, r, s)
        st.info(f"Your Internal mark (IAT) /20 is: {int1}")
        st.info(f"Your Internal mark (Model) /20 is: {int2}")
        st.success(f"Your Internal mark (End semester) is: {total_int}")
        st.markdown("<h4 style='color:purple;'>Thanks for Coming! COME AGAIN !!!</h4>", unsafe_allow_html=True)

