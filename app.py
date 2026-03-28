import streamlit as st
import random
import time

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="Siêu Sao Toán Cấp 3", page_icon="⚡", layout="centered")

# --- DỮ LIỆU CÂU HỎI ---
questions_data = {
    "Dễ (Lớp 10-11)": [
        {"q": "Đạo hàm của x² là?", "options": ["x", "2x", "2", "x³"], "a": "2x", "exp": "Công thức: (xⁿ)' = n.xⁿ⁻¹"},
        {"q": "sin²x + cos²x bằng?", "options": ["0", "1", "2", "-1"], "a": "1", "exp": "Đây là hằng đẳng thức lượng giác cơ bản."},
        {"q": "Vectơ pháp tuyến của đường thẳng 2x - 3y + 1 = 0 là?", "options": ["(2;3)", "(2;-3)", "(-3;2)", "(3;2)"], "a": "(2;-3)", "exp": "Vectơ pháp tuyến n = (a;b) lấy từ hệ số của x và y."},
        {"q": "Tập xác định của y = 1/x là?", "options": ["R", "R\\{0}", "(0;+∞)", "R\\{1}"], "a": "R\\{0}", "exp": "Mẫu số phải khác 0."},
        {"q": "Đường thẳng đi qua 2 điểm phân biệt có bao nhiêu vectơ chỉ phương?", "options": ["1", "2", "Vô số", "0"], "a": "Vô số", "exp": "Các vectơ cùng phương với nhau đều là vectơ chỉ phương."},
        {"q": "Cấp số cộng có u1=1, d=2 thì u2 bằng?", "options": ["2", "3", "4", "5"], "a": "3", "exp": "u2 = u1 + d = 1 + 2 = 3."},
        {"q": "Giai thừa của 0 (0!) bằng?", "options": ["0", "1", "Không tồn tại", "10"], "a": "1", "exp": "Quy ước toán học: 0! = 1."},
        {"q": "Hàm số y = x³ đồng biến trên khoảng nào?", "options": ["(0;+∞)", "R", "(-∞;0)", "Không đồng biến"], "a": "R", "exp": "y' = 3x² ≥ 0 với mọi x thuộc R."},
        {"q": "Công thức diện tích hình tròn?", "options": ["2πR", "πR²", "4πR²", "πR"], "a": "πR²", "exp": "S = π.R²"},
        {"q": "log10(100) bằng?", "options": ["1", "2", "10", "100"], "a": "2", "exp": "Vì 10² = 100."}
    ],
    "Vừa (Lớp 11-12)": [
        {"q": "Đạo hàm của ln(x) là?", "options": ["1/x", "e^x", "-1/x", "ln(x)"], "a": "1/x", "exp": "Công thức đạo hàm hàm logarit tự nhiên."},
        {"q": "Nguyên hàm của sin(x) là?", "options": ["cos(x)+C", "-cos(x)+C", "tan(x)+C", "sin(x)+C"], "a": "-cos(x)+C", "exp": "Đạo hàm của cos(x) là -sin(x), nên nguyên hàm của sin(x) là -cos(x)."},
        {"q": "Tiệm cận đứng của y = (x+1)/(x-2) là?", "options": ["x=1", "y=1", "x=2", "y=2"], "a": "x=2", "exp": "Nghiệm của mẫu số x-2=0 là x=2."},
        {"q": "Cho log2(3) = a. Tính log2(6) theo a?", "options": ["a+1", "2a", "a+2", "a-1"], "a": "a+1", "exp": "log2(6) = log2(2*3) = log2(2) + log2(3) = 1 + a."},
        {"q": "Số cách chọn 2 học sinh từ 10 học sinh là?", "options": ["A(10,2)", "C(10,2)", "20", "10²"], "a": "C(10,2)", "exp": "Chọn không phân biệt thứ tự dùng Tổ hợp C."},
        {"q": "Đạo hàm của e^(2x) là?", "options": ["e^(2x)", "2.e^(2x)", "e^x", "1/2.e^(2x)"], "a": "2.e^(2x)", "exp": "(e^u)' = u'.e^u."},
        {"q": "Thể tích khối chóp có diện tích đáy B và chiều cao h?", "options": ["Bh", "1/2Bh", "1/3Bh", "3Bh"], "a": "1/3Bh", "exp": "V = 1/3 * đáy * cao."},
        {"q": "Nghiệm của phương trình 2^x = 8 là?", "options": ["2", "3", "4", "log2(3)"], "a": "3", "exp": "2³ = 8."},
        {"q": "Giá trị cực đại của y = -x² + 2x là?", "options": ["1", "0", "2", "-1"], "a": "1", "exp": "Đỉnh Parabol tại x=1, y=1."},
        {"q": "Hàm số y = sin(x) tuần hoàn với chu kỳ?", "options": ["π", "2π", "π/2", "3π"], "a": "2π", "exp": "Chu kỳ cơ bản của sin và cos là 2π."}
    ],
    "Khó (Vận dụng)": [
        {"q": "Số điểm cực trị của hàm f(x) có f'(x) = x(x-1)²(x+2)³ là?", "options": ["1", "2", "3", "4"], "a": "2", "exp": "Cực trị chỉ xảy ra tại nghiệm bội lẻ (x=0 và x=-2)."},
        {"q": "Nguyên hàm của ln(x) là?", "options": ["1/x", "x.ln(x)-x", "x.ln(x)+x", "ln²(x)/2"], "a": "x.ln(x)-x", "exp": "Sử dụng phương pháp nguyên hàm từng phần."},
        {"q": "Cho hình lập phương cạnh a. Khoảng cách giữa 2 đường thẳng chéo nhau của 2 mặt đối diện là?", "options": ["a", "a√2", "a√3", "a/2"], "a": "a", "exp": "Đó chính là cạnh của hình lập phương."},
        {"q": "Giá trị lớn nhất của y = sin(x) + cos(x) là?", "options": ["1", "2", "√2", "√3"], "a": "√2", "exp": "y = √2sin(x + π/4). Max là √2."},
        {"q": "Số nghiệm của pt log2|x| = 0 là?", "options": ["1", "2", "0", "Vô số"], "a": "2", "exp": "|x| = 1 nên x = 1 hoặc x = -1."}
    ]
}

# --- KHỞI TẠO BIẾN HỆ THỐNG ---
for key in ['score', 'current_idx', 'wrong_answers', 'level', 'game_state', 'timer']:
    if key not in st.session_state:
        st.session_state.score = 0
        st.session_state.current_idx = 0
        st.session_state.wrong_answers = []
        st.session_state.level = "Dễ (Lớp 10-11)"
        st.session_state.game_state = "START" # START, PLAYING, RESULT, REVIEW

# --- HÀM XỬ LÝ ---
def start_game(lvl):
    st.session_state.level = lvl
    st.session_state.score = 0
    st.session_state.current_idx = 0
    st.session_state.wrong_answers = []
    st.session_state.game_state = "PLAYING"
    random.shuffle(questions_data[lvl])

def play_sound(type):
    if type == "correct":
        st.toast("Đúng rồi! ✨", icon="✅")
    else:
        st.toast("Sai mất rồi! ❌", icon="🚨")

# --- GIAO DIỆN ---
if st.session_state.game_state == "START":
    st.title("🏹 Đấu Trường Toán Học Cấp 3")
    st.write("Hãy chọn mức độ để bắt đầu thử thách (10 giây/câu):")
    col1, col2, col3 = st.columns(3)
    if col1.button("Dễ (10 câu)"): start_game("Dễ (Lớp 10-11)")
    if col2.button("Vừa (10 câu)"): start_game("Vừa (Lớp 11-12)")
    if col3.button("Khó (5 câu)"): start_game("Khó (Vận dụng)")

elif st.session_state.game_state == "PLAYING":
    q_list = questions_data[st.session_state.level]
    q = q_list[st.session_state.current_idx]
    
    st.subheader(f"Mức độ: {st.session_state.level}")
    st.write(f"Câu hỏi {st.session_state.current_idx + 1}/{len(q_list)}")
    
    # Thanh thời gian (10 giây)
    placeholder = st.empty()
    for t in range(10, -1, -1):
        placeholder.metric("⏳ Thời gian còn lại", f"{t}s")
        time.sleep(1)
        if t == 0:
            st.warning("Hết giờ!")
            st.session_state.wrong_answers.append(q)
            st.session_state.current_idx += 1
            st.rerun()
        
        # Hiển thị câu hỏi và nút bấm
        st.info(f"### {q['q']}")
        cols = st.columns(2)
        ans_clicked = False
        for i, opt in enumerate(q['options']):
            if cols[i%2].button(opt, key=f"btn_{i}"):
                ans_clicked = True
                if opt == q['a']:
                    st.session_state.score += 1
                    play_sound("correct")
                else:
                    st.session_state.wrong_answers.append(q)
                    st.error(f"Sai! {q['exp']}")
                    play_sound("wrong")
                    time.sleep(2)
                
                st.session_state.current_idx += 1
                break
        
        if ans_clicked:
            if st.session_state.current_idx >= len(q_list):
                st.session_state.game_state = "RESULT"
            st.rerun()

elif st.session_state.game_state == "RESULT":
    st.title("🏁 Kết quả bài thi")
    total_score = st.session_state.score
    st.header(f"Điểm của bạn: {total_score} câu đúng")
    
    if total_score >= 22: # Đây là điều kiện cho tổng nhiều lượt chơi hoặc bạn tự chỉnh lại
        st.success("🌟 Bạn thật là đẳng cấp!")
    elif total_score < 15:
        st.warning("📚 Bạn cần ôn tập kĩ hơn.")
    
    col1, col2 = st.columns(2)
    if col1.button("Chơi lại từ đầu"):
        st.session_state.game_state = "START"
        st.rerun()
    if col2.button("Ôn tập câu sai"):
        st.session_state.game_state = "REVIEW"
        st.rerun()

elif st.session_state.game_state == "REVIEW":
    st.title("📝 Ôn tập câu sai")
    if not st.session_state.wrong_answers:
        st.write("Tuyệt vời! Bạn không sai câu nào.")
    else:
        for i, w in enumerate(st.session_state.wrong_answers):
            with st.expander(f"Câu hỏi: {w['q']}"):
                st.write(f"**Đáp án đúng:** {w['a']}")
                st.write(f"**Giải thích:** {w['exp']}")
    
    if st.button("Quay lại Menu"):
        st.session_state.game_state = "START"
        st.rerun()