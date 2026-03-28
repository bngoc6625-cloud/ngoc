import streamlit as st
import random
import time

# --- CẤU HÌNH ---
st.set_page_config(page_title="Siêu Sao Toán Cấp 3", page_icon="⚡")

# Dữ liệu câu hỏi (Giữ nguyên như bản trước hoặc thêm bớt tùy bạn)
questions_data = {
    "Dễ (10 câu)": [
        {"q": "Đạo hàm của x² là?", "options": ["x", "2x", "2", "x³"], "a": "2x", "exp": "(xⁿ)' = n.xⁿ⁻¹"},
        {"q": "sin²x + cos²x bằng?", "options": ["0", "1", "2", "-1"], "a": "1", "exp": "Hằng đẳng thức cơ bản."},
        {"q": "log10(100) bằng?", "options": ["1", "2", "10", "100"], "a": "2", "exp": "10² = 100."},
        {"q": "Vectơ n=(2;-3) là VTPT của đường nào?", "options": ["2x-3y=0", "3x+2y=0", "2x+3y=0", "x-y=0"], "a": "2x-3y=0", "exp": "Hệ số x, y chính là tọa độ n."},
        {"q": "Diện tích mặt cầu bán kính R?", "options": ["4πR²", "πR²", "4/3πR³", "2πR"], "a": "4πR²", "exp": "S = 4πR²."},
        {"q": "Cấp số cộng u1=2, d=3. Tìm u2?", "options": ["5", "6", "4", "1"], "a": "5", "exp": "u2 = u1 + d."},
        {"q": "Đạo hàm của sin(x)?", "options": ["cos(x)", "-cos(x)", "tan(x)", "1"], "a": "cos(x)", "exp": "(sin)' = cos."},
        {"q": "Tiệm cận ngang của y=(x-1)/(x+1)?", "options": ["y=1", "y=-1", "x=1", "x=-1"], "a": "y=1", "exp": "Lấy hệ số x chia nhau."},
        {"q": "Nghiệm của 2^x = 4?", "options": ["1", "2", "3", "0"], "a": "2", "exp": "2² = 4."},
        {"q": "0! bằng bao nhiêu?", "options": ["0", "1", "10", "Vô cùng"], "a": "1", "exp": "Quy ước 0! = 1."}
    ],
    "Vừa (10 câu)": [
        {"q": "Đạo hàm ln(x)?", "options": ["1/x", "e^x", "ln(x)", "1"], "a": "1/x", "exp": "(lnx)' = 1/x."},
        {"q": "Nguyên hàm của cos(x)?", "options": ["sin(x)+C", "-sin(x)+C", "cos(x)", "1"], "a": "sin(x)+C", "exp": "Nguyên hàm cos là sin."},
        {"q": "Số cách chọn 2 từ 5 người?", "options": ["10", "20", "5", "2"], "a": "10", "exp": "C(5,2) = 10."},
        {"q": "Đạo hàm e^(2x)?", "options": ["2e^(2x)", "e^(2x)", "e^x", "2"], "a": "2e^(2x)", "exp": "(e^u)' = u'.e^u."},
        {"q": "V khối chóp?", "options": ["1/3Bh", "Bh", "1/2Bh", "3Bh"], "a": "1/3Bh", "exp": "V = 1/3 S_đáy * h."},
        {"q": "log2(8)?", "options": ["3", "4", "2", "8"], "a": "3", "exp": "2³=8."},
        {"q": "Hàm số y=x³ đồng biến trên?", "options": ["R", "(0;inf)", "(-inf;0)", "Không"], "a": "R", "exp": "y'=3x² >= 0."},
        {"q": "Chu kỳ của hàm sin(x)?", "options": ["2π", "π", "π/2", "0"], "a": "2π", "exp": "Chu kỳ sin là 2π."},
        {"q": "Đỉnh của y=x²-2x?", "options": ["(1;-1)", "(1;1)", "(0;0)", "(-1;1)"], "a": "(1;-1)", "exp": "x = -b/2a."},
        {"q": "Cấp số nhân u1=1, q=2. u3=?", "options": ["4", "3", "2", "1"], "a": "4", "exp": "u3 = u1*q²."}
    ],
    "Khó (5 câu)": [
        {"q": "Số cực trị f'(x)=x(x-1)²?", "options": ["1", "2", "3", "0"], "a": "1", "exp": "Chỉ đổi dấu qua x=0."},
        {"q": "Nguyên hàm ln(x)?", "options": ["xlnx-x", "1/x", "xlnx+x", "ln²x"], "a": "xlnx-x", "exp": "Nguyên hàm từng phần."},
        {"q": "Max y=sinx+cosx?", "options": ["√2", "1", "2", "√3"], "a": "√2", "exp": "y = √2sin(x+45°)."},
        {"q": "Nghiệm log2|x|=0?", "options": ["2", "1", "0", "Vô số"], "a": "2", "exp": "x=1 hoặc x=-1."},
        {"q": "Khoảng cách 2 mặt đối diện lập phương cạnh a?", "options": ["a", "a√2", "a√3", "a/2"], "a": "a", "exp": "Bằng độ dài cạnh."}
    ]
}

# --- QUẢN LÝ TRẠNG THÁI ---
if 'state' not in st.session_state:
    st.session_state.state = "MENU"
    st.session_state.score = 0
    st.session_state.current_idx = 0
    st.session_state.wrong_list = []

def start_game(level):
    st.session_state.questions = list(questions_data[level])
    random.shuffle(st.session_state.questions)
    st.session_state.score = 0
    st.session_state.current_idx = 0
    st.session_state.wrong_list = []
    st.session_state.state = "PLAYING"

# --- GIAO DIỆN ---
if st.session_state.state == "MENU":
    st.title("🏹 Đấu Trường Toán Học Cấp 3")
    st.write("Chọn mức độ để bắt đầu (10 giây/câu):")
    c1, c2, c3 = st.columns(3)
    if c1.button("Dễ (10 câu)"): start_game("Dễ (10 câu)")
    if c2.button("Vừa (10 câu)"): start_game("Vừa (10 câu)")
    if c3.button("Khó (5 câu)"): start_game("Khó (5 câu)")

elif st.session_state.state == "PLAYING":
    q = st.session_state.questions[st.session_state.current_idx]
    
    st.subheader(f"Câu {st.session_state.current_idx + 1}/{len(st.session_state.questions)}")
    st.info(f"### {q['q']}")
    
    # Hiển thị đáp án (Dùng Form để tránh bị load lại khi chưa chọn)
    with st.container():
        cols = st.columns(2)
        for i, opt in enumerate(q['options']):
            if cols[i%2].button(opt, key=f"opt_{i}", use_container_width=True):
                if opt == q['a']:
                    st.success("Chính xác! ✨")
                    st.session_state.score += 1
                else:
                    st.error(f"Sai rồi! Đáp án: {q['a']}")
                    st.write(f"🔍 Giải thích: {q['exp']}")
                    st.session_state.wrong_list.append(q)
                    time.sleep(2) # Cho xem giải thích 2 giây
                
                st.session_state.current_idx += 1
                if st.session_state.current_idx >= len(st.session_state.questions):
                    st.session_state.state = "RESULT"
                st.rerun()

elif st.session_state.state == "RESULT":
    st.title("🏁 Kết Quả")
    s = st.session_state.score
    st.metric("Điểm của bạn", f"{s} câu đúng")
    
    if s >= 22: st.success("🌟 Bạn thật là đẳng cấp!")
    elif s < 15: st.warning("📚 Bạn cần ôn tập kĩ hơn.")
    else: st.info("Khá tốt! Cố gắng thêm chút nữa nhé.")

    if st.button("Làm lại"): st.session_state.state = "MENU"; st.rerun()
    if st.button("Xem lại câu sai"): st.session_state.state = "REVIEW"; st.rerun()

elif st.session_state.state == "REVIEW":
    st.title("📝 Ôn tập câu sai")
    for w in st.session_state.wrong_list:
        with st.expander(w['q']):
            st.write(f"✅ Đáp án đúng: **{w['a']}**")
            st.write(f"📖 Giải thích: {w['exp']}")
    if st.button("Về Menu"): st.session_state.state = "MENU"; st.rerun()