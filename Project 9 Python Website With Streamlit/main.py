import streamlit as st

# Page configuration
st.set_page_config(page_title="Interactive Quiz", layout="wide")

# Title of the app
st.title("🎓 Interactive Quiz App")

# Introduction text
st.markdown("""
    Welcome to the Interactive Quiz! Choose your quiz topic, attempt the questions, and see your results at the end.
""")

# Quiz questions and answers
quiz_data = {
    'Science': [
        {'question': 'What is the chemical symbol for water?', 'options': ['H2O', 'O2', 'CO2', 'H2'], 'answer': 'H2O'},
        {'question': 'What is the boiling point of water?', 'options': ['90°C', '100°C', '110°C', '120°C'], 'answer': '100°C'},
        {'question': 'Who developed the theory of relativity?', 'options': ['Isaac Newton', 'Albert Einstein', 'Nikola Tesla', 'Galileo Galilei'], 'answer': 'Albert Einstein'}
    ],
    'History': [
        {'question': 'Who was the first President of the United States?', 'options': ['George Washington', 'Abraham Lincoln', 'Thomas Jefferson', 'John Adams'], 'answer': 'George Washington'},
        {'question': 'In which year did World War II end?', 'options': ['1940', '1942', '1945', '1950'], 'answer': '1945'},
        {'question': 'What year did the Titanic sink?', 'options': ['1910', '1912', '1914', '1916'], 'answer': '1912'}
    ],
    'Technology': [
        {'question': 'Who is the founder of Microsoft?', 'options': ['Bill Gates', 'Steve Jobs', 'Mark Zuckerberg', 'Larry Page'], 'answer': 'Bill Gates'},
        {'question': 'What does HTML stand for?', 'options': ['HyperText Markup Language', 'Hyper Transfer Markup Language', 'HyperText Machine Language', 'HighText Markup Language'], 'answer': 'HyperText Markup Language'},
        {'question': 'Which company developed the iPhone?', 'options': ['Samsung', 'Microsoft', 'Apple', 'Google'], 'answer': 'Apple'}
    ]
}

# Dropdown to choose the quiz topic
topic = st.selectbox("Choose a quiz topic", list(quiz_data.keys()))

# Initialize score
score = 0
questions = quiz_data[topic]

# Iterate through the questions
for idx, q in enumerate(questions):
    st.subheader(f"Q{idx+1}: {q['question']}")
    user_answer = st.radio("Choose an option:", q['options'], key=f"question_{idx}")

    # Check if the user's answer is correct
    if user_answer == q['answer']:
        score += 1

# Submit button to display the results
if st.button("Submit Quiz"):
    st.markdown(f"### Your Score: {score}/{len(questions)}")
    if score == len(questions):
        st.success("🎉 Perfect score! Well done!")
    elif score > len(questions) // 2:
        st.success("Good job!")
    else:
        st.warning("Better luck next time! Keep trying!")
