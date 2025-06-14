import requests
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def main():
    data = requests.get("http://localhost:8080/analytics").json()

    st.title("🧠 Stroke Analytics Dashboard")

    st.subheader("📊 Key Statistics")
    st.metric("Total Records", data["records"])
    st.metric("Average Age", f'{data["averageAge"]:.2f} years')

    st.subheader("👥 Gender Distribution")
    gender_df = pd.DataFrame.from_dict(data["genderDistribution"], orient="index", columns=["Count"])
    st.bar_chart(gender_df)

    # Stroke Distribution
    st.subheader("❤️ Stroke Distribution")
    stroke_df = pd.DataFrame({
        "Stroke": ["No", "Yes"],
        "Count": [data["strokeDistribution"]["false"], data["strokeDistribution"]["true"]]
    })
    fig, ax = plt.subplots()
    ax.pie(stroke_df["Count"], labels=stroke_df["Stroke"], autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)


if __name__ == '__main__':
    main()