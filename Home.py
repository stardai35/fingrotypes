import streamlit as st
import os
from PIL import Image
# Set page config

st.set_page_config(
    page_title="Bloodgroup Prediction",
    page_icon="🩸",  # Emoji atau path ke gambar
    layout="centered"
)

# Section Overview
st.markdown('<h2 id="overview">Overview</h2>', unsafe_allow_html=True)
st.write("""
Aplikasi ini memanfaatkan teknologi Deep Learning berbasis Convolutional Neural Network (CNN) untuk memprediksi golongan darah seseorang dengan menggunakan gambar sidik jarinya. 
Teknologi ini diharapkan dapat membantu dalam proses identifikasi golongan darah dengan cara yang cepat, mudah, dan tanpa perlu alat tes darah konvensional.
""")

st.link_button("Prediksi saya sekarang! ꩜☝️", "https://fingrotype.streamlit.app/Klasifikasi_Golongan_Darah")
st.markdown(
    """
    <div style="text-align: left;">
        <iframe width="640" height="360" src="https://youtu.be/6jSorLHovjE?si=wfIAcgJm2t3An9wp" 
        frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen></iframe>
    </div>
    """,
    unsafe_allow_html=True
)

# Dataset Section
# Fungsi untuk menampilkan gambar dari folder golongan darah
def show_blood_group_images(blood_group, num_samples=5):
    folder_path = f"sidik_jari/{blood_group}"
    try:
        image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png', '.jpeg'))]
        st.subheader(f"Golongan Darah {blood_group}")
        
        cols = st.columns(min(num_samples, len(image_files)))  # Membuat kolom sesuai jumlah gambar
        
        for idx, col in enumerate(cols):
            if idx < len(image_files):
                img_path = os.path.join(folder_path, image_files[idx])
                try:
                    
                    image = Image.open(img_path)
                    image = image.resize((200, 200))
                
                    with col:
                        st.image(image, caption=f"Sidik Jari {blood_group}", width=150)
                except Exception as e:
                    st.error(f"Error loading image {img_path}: {e}")
            else:
                break
                
    except FileNotFoundError:
        st.warning(f"Folder untuk golongan darah {blood_group} tidak ditemukan")

blood_groups = ["A", "B", "AB", "O"]

# Atau tampilkan per golongan darah dengan tab
st.title("Galeri Dataset Sidik Jari")
tabs = st.tabs(blood_groups)

for i, tab in enumerate(tabs):
    with tab:
        show_blood_group_images(blood_groups[i], num_samples=10)  
# Korelasi Antara Golongan Darah dan Sidik Jari
st.header("Hubungan Pola Sidik Jari dan Golongan darah")
st.write("""
Bersumber penelitian Study of Fingerprint Patterns in Relation
to Gender and ABO Blood Groups. Indian Journal of Forensic Medicine and Toxicology 2023;17(4) ditunjukkan adanya korelasi antara pola sidik jari—seperti loops, whorls, dan arches—
dengan golongan darah seseorang. Misalnya, pola loop lebih sering ditemukan pada individu bergolongan darah B dan O,
sedangkan whorl cenderung lebih umum pada golongan darah O dan A.

Meskipun temuan ini belum menjadi acuan medis, studi ini memberikan wawasan tentang kemungkinan hubungan antara
karakteristik biologis dan genetika manusia.
""")
# Gambar lokal
local_image = Image.open("korelasi.png")
st.image(local_image, caption="""
Tabel Korelasi Antara Sidik Jari dan Golongan Darah
""",
    width=400 )
# Section Features
st.header("Fitur Utama")
st.write("""
- **Prediksi Otomatis:** Unggah gambar sidik jari dan aplikasi akan secara otomatis memprediksi golongan darah.
- **Antarmuka Sederhana:** Desain user-friendly sehingga mudah digunakan oleh siapa saja.
- **Hasil Prediksi Lengkap:** Menampilkan golongan darah beserta tingkat kepercayaan hasil prediksi.
- **Open Source:** Mudah untuk dikembangkan dan dimodifikasi sesuai kebutuhan.
""")

# Footer
st.markdown("---")
st.markdown("""
<style>
.footer {
    font-size: small;
    text-align: center;
    padding: 10px;
}
</style>
<div class="footer">
    © 2025 Tri Kusuma Faradila - Blood Group Detection System | All Rights Reserved
</div>
""", unsafe_allow_html=True)
