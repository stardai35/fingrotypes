import streamlit as st

# Set judul
st.set_page_config(page_title="Tentang Golongan Darah",page_icon="🩸", layout="wide")


st.subheader("Sistem Penggolongan Darah")
st.write("""
Golongan darah diklasifikasikan berdasarkan keberadaan antigen tertentu pada permukaan sel darah merah.
Dua sistem penggolongan darah yang paling penting adalah:
1. **Sistem ABO** - Dibagi menjadi A, B, AB, dan O
2. **Sistem Rhesus (Rh)** - Dibagi menjadi Rh+ dan Rh-
""")
st.subheader("Kompatibilitas Donor Darah")
st.write("""
| Golongan Darah | Bisa Mendonor ke | Bisa Menerima dari |
|----------------|------------------|--------------------|
| A+            | A+, AB+          | A+, A-, O+, O-     |
| A-            | A+, A-, AB+, AB- | A-, O-             |
| B+            | B+, AB+          | B+, B-, O+, O-     |
| B-            | B+, B-, AB+, AB- | B-, O-             |
| AB+           | AB+              | Semua golongan     |
| AB-           | AB+, AB-         | AB-, A-, B-, O-    |
| O+            | O+, A+, B+, AB+  | O+, O-             |
| O-            | Semua golongan   | O-                 |
""")

st.subheader("Golongan Darah ABO")
st.write("""
- **Golongan A**: Memiliki antigen A pada sel darah merah dan antibodi anti-B dalam plasma
- **Golongan B**: Memiliki antigen B pada sel darah merah dan antibodi anti-A dalam plasma
- **Golongan AB**: Memiliki antigen A dan B pada sel darah merah, tidak memiliki antibodi anti-A atau anti-B dalam plasma
- **Golongan O**: Tidak memiliki antigen A atau B pada sel darah merah, memiliki antibodi anti-A dan anti-B dalam plasma
""")

st.subheader("Faktor Rhesus (Rh)")
st.write("""
- **Rh+**: Memiliki antigen D pada permukaan sel darah merah
- **Rh-**: Tidak memiliki antigen D pada permukaan sel darah merah
""")

st.subheader("Rekomendasi Gaya Hidup Berdasarkan Golongan Darah")

tab1, tab2, tab3, tab4 = st.tabs(["Golongan A", "Golongan B", "Golongan AB", "Golongan O"])

with tab1:
    st.write("""
    **Golongan A (The Agrarian)**
    
    - **Diet**: Vegetarian atau tinggi sayuran, biji-bijian, tofu, seafood (ikan), kacang-kacangan
    - **Hindari**: Daging merah, susu, kacang merah, gandum berlebihan
    - **Olahraga**: Yoga, tai chi, olahraga ringan
    - **Manajemen stres**: Meditasi, pernapasan dalam
    - **Kekuatan**: Sistem pencernaan efisien, adaptasi baik dengan diet stabil
    - **Kelemahan**: Sistem imun sensitif, risiko penyakit jantung dan kanker lebih tinggi
    """)

with tab2:
    st.write("""
    **Golongan B (The Nomad)**
    
    - **Diet**: Seimbang - daging (kambing, domba), susu, biji-bijian, sayuran hijau
    - **Hindari**: Ayam, jagung, kacang tanah, lentil, gandum
    - **Olahraga**: Aktivitas moderat seperti hiking, tenis, berenang
    - **Manajemen stres**: Kreativitas, aktivitas sosial
    - **Kekuatan**: Sistem imun kuat, sistem pencernaan fleksibel
    - **Kelemahan**: Risiko gangguan autoimun, sensitif terhadap makanan tertentu
    """)

with tab3:
    st.write("""
    **Golongan AB (The Enigma)**
    
    - **Diet**: Campuran A dan B - tahu, seafood, susu, sayuran hijau, rumput laut
    - **Hindari**: Daging asap, alkohol berlebihan, kafein
    - **Olahraga**: Kombinasi relaksasi dan aktivitas intensitas sedang
    - **Manajemen stres**: Teknik relaksasi, aktivitas spiritual
    - **Kekuatan**: Adaptasi modern, sistem imun kompleks
    - **Kelemahan**: Risiko penyakit jantung, kanker, anemia
    """)

with tab4:
    st.write("""
    **Golongan O (The Hunter)**
    
    - **Diet**: Tinggi protein - daging merah, ikan, sayuran, buah-buahan
    - **Hindari**: Gluten (gandum), susu, kacang-kacangan tertentu
    - **Olahraga**: Intens seperti lari, angkat beban, high-intensity interval training
    - **Manajemen stres**: Aktivitas fisik intens
    - **Kekuatan**: Sistem pencernaan kuat, sistem imun protektif
    - **Kelemahan**: Risiko gangguan tiroid, radang sendi, alergi
    """)

st.caption("""
Catatan: Rekomendasi gaya hidup berdasarkan golongan darah ini berasal dari teori kontroversial 'Eat Right for Your Type' \. Untuk rekomendasi lebih lanjut, konsultasikan dengan dokter atau ahli gizi sebelum \
membuat perubahan signifikan pada diet atau gaya hidup Anda.
""")