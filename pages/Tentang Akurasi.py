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
    st.write("Confusion Matrix")
    st.image("https://scontent.fsrg6-1.fna.fbcdn.net/v/t39.30808-6/514331731_1927955168035840_760855731047475214_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=127cfc&_nc_ohc=QLfEsG3nOtkQ7kNvwEFD47_&_nc_oc=AdltlbZoi9vTplx2WUUAizgyqbTw-G3mPs_cTm8fIje8QWe4iEsWcie-JMUYpQFIUJrhP5X5-fz9LzIIQ5XUAXkt&_nc_zt=23&_nc_ht=scontent.fsrg6-1.fna&_nc_gid=oBOSEyAMyxFt40Hivlb0CQ&oh=00_AfTCfDfv8htEBJp2z0nCnudbPeJx7Z8DJfLSOHkFWMdyog&oe=6870E744", caption="Confusion Matrix", use_container_width=True)
    
    st.write("Precision Recall")
    st.image("https://scontent.fsrg6-1.fna.fbcdn.net/v/t39.30808-6/514415683_1927955171369173_2387643765714314076_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=127cfc&_nc_ohc=hPNhIHO0A58Q7kNvwEPfmyD&_nc_oc=AdnbI_ilsN9_3q7_fHLrVqez7MWu_p4QeQssrvpkMfLqKVWR767pAYX4GqQYuVk5HT1Hq9WVuuR14DMsN3okO4WQ&_nc_zt=23&_nc_ht=scontent.fsrg6-1.fna&_nc_gid=l6rCEeAXRJcgpVeYkOdg5w&oh=00_AfQRxQv2gsVyw_SuYep4rKiz7GF4FRoifin3D4nXNder0A&oe=6870BC93", caption="Report Precision Recall", use_container_width=True)

with col2:
    st.write("Training and Testing Loss Ratio")
    st.image("https://scontent.fsrg6-1.fna.fbcdn.net/v/t39.30808-6/515669042_1927955174702506_6030725602347938722_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=127cfc&_nc_ohc=AW8OzaRZRpUQ7kNvwEVlR1D&_nc_oc=AdnZGZbXqpIeLoTfTJe5C5_AtjsjCwHbtvKbmTILxfk0Jcn5BcUNAHZwJwzFMMlT0xqUZE3S0u-75DISWMddWunv&_nc_zt=23&_nc_ht=scontent.fsrg6-1.fna&_nc_gid=7pzoMeNpsdi1Dfc00SCUEg&oh=00_AfQ7KPZwVV5GWK4i3pvFjap1A9T2wcWvUnk9s52X0gyKKA&oe=6870DDC3", caption="Training vs Testing Loss", use_container_width=True)
    
    st.write("Overall Architecture of the Project")
    st.image("https://scontent.fsrg6-1.fna.fbcdn.net/v/t39.30808-6/516034673_1927955361369154_2556558314671695475_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=127cfc&_nc_ohc=IZvFJaqGwNsQ7kNvwEssKTI&_nc_oc=AdkGGRfIg4dt8molkf9zK2e-ypX2qCWm_pglE1WSWnVSOZW72ynR1Ew3c4MPCDBnmr5P1EBBPaTfbeLe2xfhiJT1&_nc_zt=23&_nc_ht=scontent.fsrg6-1.fna&_nc_gid=2iy1wsaxq8kTh-FPBfT82w&oh=00_AfSYBeh1jfbZo3CAiAeXeMEh3Lgo2r5IwWT4HwBTKYY3vQ&oe=6870C66B", caption="Project Architecture",use_container_width=True)
