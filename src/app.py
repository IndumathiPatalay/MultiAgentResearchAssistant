import streamlit as st
from pipeline import research_pipeline

# Streamlit App
st.set_page_config(page_title="Research Assistant", layout="wide")

st.title("🔎 Research Assistant Pipeline")
st.write("Enter a topic and let the pipeline search, read, and generate a structured research report.")

# Input field
topic = st.text_input("Enter your research topic here:")

# Run pipeline button
if st.button("Run Research Pipeline"):
    if topic.strip():
        with st.spinner("Running research pipeline..."):
            try:
                report = research_pipeline(topic)
                st.success("Pipeline executed successfully!")
                
                # Display the report
                st.subheader("📄 Generated Research Report")
                st.text_area("Report Output", report, height=400)
            except Exception as e:
                st.error(f"Error running pipeline: {e}")
    else:
        st.warning("Please enter a topic before running the pipeline.")