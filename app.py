import streamlit as st
import random

# Cấu hình giao diện
st.set_page_config(page_title="Phù Thủy Toán Cấp 3", page_icon="🧙‍♂️")

# Khởi tạo dữ liệu câu hỏi (Toán cấp 3)
questions = [
    {"q": "Đạo hàm của sin(x) là gì?", "a": "cos(x)", "level": "Lớp 11"},
    {"q": "Nguyên hàm của 1/x là gì?", "a": "ln|x|", "level": "Lớp 12"},
    {"q": "log2(8) bằng bao nhiêu?", "a": "3", "level": "Lớp 12"},
    {"q": "Số phức i bình phương bằng bao nhiêu?", "a": "-1", "level": "Lớp 12"},
    {"q": "Giá trị của cos(60°) là bao nhiêu?", "a": "0.5", "level": "Lớp 10"},
    {"q": "Đạo hàm của e^x là gì?", "a": "e^x", "level": "Lớp 12"}
]

# Khởi tạo trạng thái game
if 'hp' not in st.session_state:
    st.session_state.hp = 3
    st.session_state.score = 0
    st.session_state.current_q = random.choice(questions)

def reset_game():
    st.session_state.hp = 3
    st.session_state.score = 0
    st.session_state.current_q = random.choice(questions)

# Giao diện chính
st.title("🧙‍♂️ Math Wizard: Calculus Conquest")
st.sidebar.header("Trạng thái nhân vật")
st.sidebar.metric("Máu (HP)", "❤️" * st.session_state.hp)
st.sidebar.metric("Điểm kinh nghiệm (EXP)", st.session_state.score)

if st.session_state.hp <= 0:
    st.error("💥 Bạn đã hết máu! Quái vật toán học đã thắng.")
    if st.button("Hồi sinh (Chơi lại)"):
        reset_game()
        st.rerun()
else:
    q = st.session_state.current_q
    st.info(f"**Chủ đề:** {q['level']}")
    st.markdown(f"### Quái vật thách đố: \n > {q['q']}")
    
    answer = st.text_input("Nhập phép thuật (đáp án) của bạn:", key="ans_input").strip().lower()

    if st.button("Phóng phép! ✨"):
        if answer == q['a'].lower():
            st.balloons()
            st.success("Chính xác! Bạn đã gây sát thương lên quái vật!")
            st.session_state.score += 10
            st.session_state.current_q = random.choice(questions)
            st.rerun()
        else:
            st.session_state.hp -= 1
            st.warning(f"Phép thuật thất bại! Bạn bị mất 1 ❤️. Đáp án đúng là: {q['a']}")
            if st.session_state.hp > 0:
                st.session_state.current_q = random.choice(questions)
                st.rerun()

st.divider()
st.caption("Mẹo: Nhập đúng định dạng như 'cos(x)', 'e^x', hoặc số thập phân '0.5'.")