import streamlit as st

# Set judul
st.set_page_config(page_title="Tentang Akurasi",page_icon="🩸", layout="wide")


# Methodology Section
st.header("Metodologi")
st.markdown("""
- **Dataset:** 1,200 fingerprint images
- **Training Model:** CNN pre-trained model VGG-16
- **Testing Model:** CNN pre-trained model VGG-16  
- **Optimizer:** Adam Optimizer  
- **Deployment:** Streamlit with Python  
- **Accuracy:** 80%
""")

# Methodology Section
st.header("Analisis Project dan Hasil")

col1, col2 = st.columns(2)

with col1:
    st.write("Confusion Matrix")
    st.image("https://pbs.twimg.com/media/Gv4CZlWW0AIMfU8?format=png&name=small", caption="Confusion Matrix", use_container_width=True)
    
    st.write("Precision Recall")
    st.image("https://pbs.twimg.com/media/Gv4CZcTa4AAWtI0?format=png&name=small", caption="Report Precision Recall", use_container_width=True)

with col2:
    st.write("Training and Testing Loss Ratio")
    st.image("https://pbs.twimg.com/media/Gv4CZjXWcAA9_8h?format=jpg&name=medium", caption="Training vs Testing Loss", use_container_width=True)
    
    st.write("Overall Architecture of the Project")
    st.image("https://pbs.twimg.com/media/Gv4CZiNa0AA34kS?format=jpg&name=large", caption="Project Architecture",use_container_width=True)
