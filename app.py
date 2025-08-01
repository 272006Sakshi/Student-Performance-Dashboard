import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------
# 📌 Helper Functions
# ----------------------------

def assign_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

def calculate_metrics(data):
    subjects = ['Math', 'Science', 'English', 'History', 'Computer']
    data['Total'] = data[subjects].sum(axis=1)
    data['Average'] = data['Total'] / len(subjects)
    data['Grade'] = data['Average'].apply(assign_grade)
    return data

def highlight_topper(data):
    topper = data[data['Total'] == data['Total'].max()].iloc[0]
    return f"{topper['Name']} (Total: {topper['Total']})"


# ----------------------------
# 🎯 Streamlit App Starts
# ----------------------------

st.set_page_config(page_title="Student Performance Dashboard", layout="wide")

st.title("📊 Student Performance Dashboard")

# File uploader
uploaded_file = st.file_uploader("Upload Student CSV File", type=["csv"])

if uploaded_file:
    # Load dataset
    data = pd.read_csv(uploaded_file)
    
    # Calculate additional metrics
    data = calculate_metrics(data)
    
    st.subheader("📄 Student Data Table")
    st.dataframe(data.style.format({"Average": "{:.2f}"}), use_container_width=True)

    # -----------------------
    # 📌 Charts and Analysis
    # -----------------------
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📊 Subject-wise Average")
        subjects = ['Math', 'Science', 'English', 'History', 'Computer']
        subject_averages = data[subjects].mean().reset_index()
        subject_averages.columns = ['Subject', 'Average Marks']
        bar_fig = px.bar(subject_averages, x='Subject', y='Average Marks',
                         color='Subject', text='Average Marks', height=400)
        st.plotly_chart(bar_fig, use_container_width=True)
        
    with col2:
        st.markdown("### 🧁 Grade Distribution")
        grade_counts = data['Grade'].value_counts().reset_index()
        grade_counts.columns = ['Grade', 'Count']
        pie_fig = px.pie(grade_counts, names='Grade', values='Count',
                         color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(pie_fig, use_container_width=True)
    
    # -----------------------
    # 🏆 Topper Highlight
    # -----------------------
    
    st.markdown("### 🏆 Topper Highlight")
    topper_info = highlight_topper(data)
    st.success(f"Topper: **{topper_info}**")
    
    # -----------------------
    # 🔎 Filter by Grade
    # -----------------------
    st.markdown("### 🔍 Filter Students by Grade")
    selected_grades = st.multiselect("Select Grade(s) to View", options=sorted(data['Grade'].unique()))
    
    if selected_grades:
        filtered_data = data[data['Grade'].isin(selected_grades)]
        st.dataframe(filtered_data.reset_index(drop=True), use_container_width=True)
    else:
        st.info("Select grade(s) above to filter students.")

else:
    st.warning("👆 Please upload a CSV file to get started.")

# ----------------------------
# 📝 Footer
# ----------------------------
st.markdown("---")
st.caption("Developed by Sakshi Kumari • Student Performance Visualizer using Streamlit")
