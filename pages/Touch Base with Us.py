import streamlit as st
from PIL import Image

# Konfigurasi halaman
st.set_page_config(
    page_title="Kontak",
    page_icon="🩸",
    layout="centered"
)
st.markdown("""
<div style="text-align: center; margin-bottom: 70px;">
    <img src="https://www.ukmpp.org/wp-content/uploads/2023/11/22-1.png" style="border-radius: 50%; width: 150px;">
    <h3>Tri Kusuma Faradila</h3>
</div>
""", unsafe_allow_html=True)


# Kontak
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <p><span class="contact-icon">📧</span> Email: 
        <a href="mailto:faradilatrikusuma@gmail.com">faradilatrikusuma@gmail.com</a></p>
        
        <p><span class="contact-icon">📱</span> LinkedIn: 
        <a href="https://www.linkedin.com/in/tri-kusuma-faradila-0123b8200/">linkedin.com/in/tri-kusuma-faradila-0123b8200/</a></p>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <p><span class="contact-icon">🔗</span> GitHub: 
        <a href="https://github.com/stardai35">github.com/stardai35</a></p>
        
        <p><span class="contact-icon">📞</span> Telepon: +62 831-5561-6880</p>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
