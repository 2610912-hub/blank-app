import streamlit as st

# 1. 웹 화면 타이틀 및 기본 안내 설정
st.title("📖 시험 기간 공부 플래너")
st.write("각 과목의 공부 시간을 입력하고, 오늘 목표를 달성했는지 확인해 보세요!")

# 변수 및 목표 시간 설정
subjects = ["국어", "수학", "영어"]
target_hours = 2

st.subheader(f"🎯 오늘 각 과목의 목표 공부 시간: {target_hours}시간")

# 2. Streamlit 입력 위젯 구성
korean_hours = st.number_input("국어 공부 시간 (시간)", min_value=0, value=0, step=1)
math_hours = st.number_input("수학 공부 시간 (시간)", min_value=0, value=0, step=1)
english_hours = st.number_input("영어 공부 시간 (시간)", min_value=0, value=0, step=1)

# 사용자가 입력한 값을 순서대로 리스트로 묶습니다.
hours_list = [korean_hours, math_hours, english_hours]

# 3. 결과 분석 및 버튼 작동 로직
if st.button("목표 달성 여부 확인하기"):
    success_subjects = []
    
    # 2차시의 핵심 알고리즘(반복문 + 조건문)을 그대로 적용
    for i in range(len(subjects)):
        if hours_list[i] >= target_hours:
            success_subjects.append(subjects[i])
            
    # 4. 웹 화면 결과 출력
    st.markdown("---")
    st.subheader("📊 오늘의 공부 결과")
    
    if len(success_subjects) > 0:
        # 달성한 과목이 있을 때 (초록색 메시지 상자)
        subjects_text = ", ".join(success_subjects)
        st.success(f"🎉 목표({target_hours}시간)를 달성한 과목은 **[{subjects_text}]** 총 **{len(success_subjects)}개**입니다!")
    else:
        # 달성한 과목이 전혀 없을 때 (노란색 경고 상자)
        st.warning("⚠️ 아직 목표 시간을 달성한 과목이 없습니다. 조금만 더 힘내서 공부해 보아요!")
