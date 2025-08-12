import streamlit as st
from crew import crew  # importing your crew object from crew.py

st.set_page_config(
    page_title="AI Research & Writing Agent",
    page_icon="📰",
    layout="centered"
)

st.title("📰 AI Research & Writing Agent")
st.write("Enter a topic below and let the AI research & write an article for you.")

# User input
topic = st.text_input("Enter topic", "AI in healthcare")

if st.button("Generate Article"):
    with st.spinner("Researching and writing your article... ⏳"):
        try:
            # Run your CrewAI process
            result = crew.kickoff(inputs={'topic': topic})
            
            if isinstance(result, dict) and "output" in result:
                article_text = result["output"]
            else:
                article_text = str(result)

            # Show article
            st.subheader("📄 Generated Article")
            st.markdown(article_text)

            # Markdown download
            st.download_button(
                label="⬇️ Download as Markdown",
                data=article_text,
                file_name=f"{topic.replace(' ', '_')}.md",
                mime="text/markdown"
            )

        except Exception as e:
            st.error(f"Error: {e}")


