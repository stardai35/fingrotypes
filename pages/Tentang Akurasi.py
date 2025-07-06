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
- **Accuracy:** 76%
""")

# Methodology Section
st.header("Analisis Project dan Hasil")

col1, col2 = st.columns(2)

with col1:
    st.write("Accuracy Plot")
    st.image("https://www.researchgate.net/publication/332582518/figure/fig2/AS:922521150959616@1596957590148/A-plot-of-accuracy-on-the-training-train-and-validation-valid-datasets-over-training.ppm", caption="Accuracy Plot", use_container_width=True)
    
    st.write("Precision Recall")
    st.image("https://www.researchgate.net/publication/345162864/figure/fig3/AS:955267659350017@1604764966904/The-classification-report-with-precision-recall-f1-score-and-support-for-RFI-pixel.png", caption="Precision Recall Curve", use_container_width=True)

with col2:
    st.write("Training and Testing Loss Ratio")
    st.image("https://www.researchgate.net/publication/323796573/figure/fig2/AS:715724972621828@1547653539362/Training-Loss-and-Validation-Accuracy-visualization-for-different-saliency-ratios-Left.png", caption="Training vs Testing Loss", use_container_width=True)
    
    st.write("Overall Architecture of the Project")
    st.image("https://blog.pintu.co.id/wp-content/uploads/2023/04/arsitektur-convolutional-neural-networks.webp", caption="Project Architecture",use_container_width=True)
