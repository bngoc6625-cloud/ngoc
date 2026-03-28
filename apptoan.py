import streamlit as st
import random

# Cấu hình trang
st.set_page_config(page_title="Math Quiz Pro", page_icon="🎓")

# Danh sách câu hỏi trắc nghiệm Toán cấp 3
if 'questions' not in st.session_state:
    st.session_state.questions = [
        {"q": "Đạo hàm của ln(x) là gì?", "options": ["1/x", "-1/x", "e^x", "ln(x)"], "a": "1/x"},
        {"q": "Giá trị của sin(π/2) là?", "options": ["0", "1", "-1", "1/2"], "a": "1"},
        {"q": "Nguyên hàm của cos(x) là?", "options": ["sin(x) + C", "-sin(x) + C", "tan(x) + C", "cos^2(x)"], "a": "sin(x) + C"},
        {"q": "Số phức z = 3 + 4i có môđun là?", "options": ["5", "7", "25", "1"], "a": "5"},
        {"q": "Tập xác định của hàm số y = log(x) là?", "options": ["(0; +∞)", "[0; +∞)", "R", "R\\{0}"], "a": "(0; +∞)"},
        {"q": "Đường tiệm cận ngang của y = (2x+1)/(x-1) là?", "options": ["y = 2", "y = 1", "x = 1", "y = -1"], "a": "y = 2"},
        {"q": "Công thức tính thể tích khối cầu bán kính R là?", "options": ["4/3πR³", "πR²", "4πR²", "1/3πR³"], "a": "4/3πR³"},
        {"q": "Cho log2(x) = 3. Giá trị của x là?", "options": ["8", "6", "9", "5"], "a": "8"}
    ]

# Khởi tạo trạng thái
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_idx' not in st.session_state:
    st.session_state.current_idx = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

def reset_game():
    st.session_state.score = 0
    st.session_state.current_idx = 0
    st.session_state.game_over = False
    random.shuffle(st.session_state.questions)

# Giao diện
st.title("🏆 Thử Thách Trắc Nghiệm Toán Cấp 3")

if st.session_state.game_over:
    st.balloons()
    st.header("Chúc mừng! 🎉")
    st.write(f"Bạn đã hoàn thành bộ câu hỏi với số điểm: **{st.session_state.score}/{len(st.session_state.questions)}**")
    if st.button("Chơi lại từ đầu"):
        reset_game()
        st.rerun()
else:
    # Lấy câu hỏi hiện tại
    q_item = st.session_state.questions[st.session_state.current_idx]
    
    # Hiển thị tiến trình
    progress = (st.session_state.current_idx) / len(st.session_state.questions)
    st.progress(progress)
    st.write(f"Câu hỏi {st.session_state.current_idx + 1}/{len(st.session_state.questions)}")
    
    st.info(f"### {q_item['q']}")

    # Tạo các nút bấm cho từng đáp án
    cols = st.columns(2)
    for i, option in enumerate(q_item['options']):
        with cols[i % 2]:
            if st.button(option, use_container_width=True):
                if option == q_item['a']:
                    st.toast("Chính xác! 🌟", icon="✅")
                    st.session_state.score += 1
                else:
                    st.toast(f"Sai rồi! Đáp án đúng là {q_item['a']}", icon="❌")
                
                # Chuyển sang câu tiếp theo
                if st.session_state.current_idx < len(st.session_state.questions) - 1:
                    st.session_state.current_idx += 1
                else:
                    st.session_state.game_over = True
                st.rerun()

st.sidebar.markdown("---")
st.sidebar.write("💡 **Mẹo:** Đọc kỹ đề trước khi chọn nhé!")