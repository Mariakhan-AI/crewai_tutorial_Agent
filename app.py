import streamlit as st
from crew import crew  # Import the crew object from crew.py
import datetime

st.set_page_config(
    page_title="AI News Researcher",
    page_icon="📰",
    layout="centered"
)

st.title("📰 AI News Researcher & Writer")
st.markdown("Enter a topic and let the AI research & write a professional article for you.")

# Topic input
topic = st.text_input("Enter your topic:", "AI in healthcare")

# Generate button
if st.button("Generate Article"):
    with st.spinner("Researching and writing... Please wait."):
        try:
            # Run the crew pipeline
            result = crew.kickoff(inputs={'topic': topic})
            
            # Show the result
            st.subheader("Generated Article")
            st.markdown(result)

            # Prepare Markdown download
            file_name = f"{topic.replace(' ', '_')}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
            st.download_button(
                label="📥 Download as Markdown",
                data=result.encode('utf-8'),
                file_name=file_name,
                mime="text/markdown"
            )
        except Exception as e:
            st.error(f"❌ An error occurred: {e}")
