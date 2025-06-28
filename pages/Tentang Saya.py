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
    <img src="https://scontent.fsrg6-1.fna.fbcdn.net/v/t1.6435-9/118701093_2853818641503341_8318291082169027335_n.jpg?stp=c0.169.1536.1536a_dst-jpg_s565x565_tt6&_nc_cat=110&ccb=1-7&_nc_sid=a5f93a&_nc_ohc=fFMAR4Zic4AQ7kNvwGTWWxe&_nc_oc=AdlDoH0zPZ8J1N7VPWJlpJH_01G5zjIyPbL8yu36r3QgM4a9CQbmwsZ1YHxDOBC22uc2SOdxjKlrvo1W2N4YXNGC&_nc_zt=23&_nc_ht=scontent.fsrg6-1.fna&_nc_gid=-irsu7f3W03kYiLbeznyNQ&oh=00_AfPwx8G_Pi2PNfiHW7VoVl0l5tnn1r1UhZCacJsEaFmWKA&oe=68797ECC" style="border-radius: 50%; width: 150px;">
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
