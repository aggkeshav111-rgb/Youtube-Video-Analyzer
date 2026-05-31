import streamlit as st
from youtube_analyzer import build_yt_agent

st.set_page_config(
    page_title="YT Video Analyzer",
    layout="centered"
)

st.title("YOUTUBE Video Analyzer")

@st.cache_resource
def get_agent():
    return build_yt_agent()

agent=get_agent()
video_url=st.text_input("Paste the yt video link below:")
button=st.button("Analyze the Video")

if video_url and button:
    with st.spinner("Analyzing..."):
        response=agent.run(
            f"analyze the video:{video_url}"
        )
        
    st.markdown("Analysis report of above youtube video")
    st.markdown(response.content)