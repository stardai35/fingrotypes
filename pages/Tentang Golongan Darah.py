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
    st.markdown("""
<h3 style="display: flex; align-items: center;">
    <img src="https://i.pinimg.com/736x/a8/a9/00/a8a900e1c9fe76cc138c24f0f6785bc3.jpg" width="70" style="margin-right:10px; border-radius:15px;">
    Golongan A (The Agrarian – Si Petani)
</h3>
""", unsafe_allow_html=True)
    st.write("""
    #### 🔹 Kepribadian:
    - Kind (baik hati)
    - Careful (hati-hati)
    - Perfectionist (perfeksionis)

    #### 🔹 Ciri Umum:
    - Bertanggung jawab, pekerja keras, suka keteraturan
    - Sensitif, pemalu, serius
    - Cocok sebagai pemimpin yang sabar dan teliti

    #### 📝 Tips Harian:
    - Hindari makan larut malam
    - Minum teh hijau
    - Konsumsi makanan organik bila memungkinkan
             
    #### Kekuatan:
    - Sistem pencernaan adaptif terhadap makanan nabati
    - Tangguh terhadap pola hidup teratur

    #### Kelemahan:
    - Sistem imun sensitif terhadap stres dan makanan olahan
    - Rentan terhadap penyakit jantung dan kanker

    #### Diet Ideal:
    - **Disarankan**: Sayuran hijau (brokoli, bayam), buah (apel, nanas), tahu, tempe, beras merah, oat, ikan (salmon, sarden)
    - **Dihindari**: Daging merah, produk susu, tomat, terong, makanan olahan, gandum berlebihan

    #### Aktivitas Fisik:
    - Yoga, tai chi, pilates, jalan santai, berenang pelan
    - Fokus pada aktivitas yang menurunkan kortisol

    #### Manajemen Stres:
    - Teknik pernapasan dalam, meditasi, rutinitas tidur yang teratur
    - Hindari tekanan atau lingkungan kompetitif
    """)

with tab2:
    st.markdown("""
<h3 style="display: flex; align-items: center;">
    <img src="https://i.pinimg.com/736x/d6/dc/a5/d6dca51d493a9fbfe50b5cc15bb05abd.jpg" width="70" style="margin-right:10px; border-radius:15px;">
    Golongan B (The Nomad – Si Pengembara)
</h3>
""", unsafe_allow_html=True)
    st.write("""
    #### 🔹 Kepribadian:
    - Brightly (ceria)
    - Attractive (menarik)
    - Frank (jujur)

    #### 🔹 Ciri Umum:
    - Kreatif, independen, tidak suka dibatasi
    - Sering dianggap nyentrik dan bebas
    - Cocok di bidang seni, musik, atau pekerjaan yang fleksibel

    #### 📝 Tips Harian:
    - Seimbangkan antara aktivitas dan waktu tenang
    - Jelajahi hobi baru
    - Hindari pola makan sembarangan
           
    #### Kekuatan:
    - Sistem imun relatif kuat dan fleksibel terhadap berbagai jenis makanan
    - Daya tahan tubuh baik terhadap aktivitas berat

    #### Kelemahan:
    - Makanan tertentu seperti ayam/jagung bisa menurunkan metabolisme dan kekebalan
  
    #### Diet Ideal:
    - **Disarankan**: Daging kambing/domba, ikan, telur, yogurt, kefir, sayuran hijau, oatmeal
    - **Dihindari**: Ayam, jagung, kacang tanah, lentil, gandum

    #### Aktivitas Fisik:
    - Tenis, hiking, bersepeda, mendaki, berenang
    - Butuh variasi agar tidak cepat bosan

    #### Manajemen Stres:
    - Liburan singkat, seni/kreativitas, journaling, aktivitas sosial
    """)

with tab3:
    st.markdown("""
<h3 style="display: flex; align-items: center;">
    <img src="https://i.pinimg.com/736x/b7/b2/75/b7b275b17d0ae5a726f5205cc62cbef6.jpg" width="70" style="margin-right:10px; border-radius:15px;">
    Golongan AB (The Enigma – Si Misterius)
</h3>
""", unsafe_allow_html=True)
    st.write("""
    #### 🔹 Kepribadian:
    - Talented (berbakat)
    - Calm (tenang)
    - Rational (rasional)

    #### 🔹 Ciri Umum:
    - Gabungan sifat A dan B
    - Rasional dan logis namun bisa berubah-ubah
    - Dikenal sebagai pribadi unik dan sulit ditebak
             
    #### 📝 Tips Harian:
    - Pola makan kecil namun sering
    - Hindari stimulasi larut malam
    - Ekspresikan emosi lewat aktivitas kreatif
    
    #### Kekuatan:
    - Adaptasi pencernaan dari A & B
    - Fleksibel dalam pilihan diet moderat

    #### Kelemahan:
    - Mudah lelah, imun fluktuatif
    - Tidak tahan tekanan jangka panjang
                      
    #### Diet Ideal:
    - **Disarankan**: Ikan laut (tuna, sarden), produk susu rendah lemak, tahu, sayuran hijau, buah beri, anggur, semangka
    - **Dihindari**: Daging merah, makanan berpengawet, kafein, alkohol, makanan pedas
    #### Aktivitas Fisik:
    - Kombinasi yoga dan jalan cepat, berenang santai, latihan kekuatan ringan

    #### Manajemen Stres:
    - Meditasi terfokus, aromaterapi, membaca, berkebun, musik instrumental
    """)

with tab4:
    st.markdown("""
<h3 style="display: flex; align-items: center;">
    <img src="https://i.pinimg.com/736x/a3/0a/a0/a30aa022a2c071b6b410ff7b63e9a27f.jpg" width="70" style="margin-right:10px; border-radius:15px;">
    Golongan O (The Hunter – Si Pemburu)
</h3>
""", unsafe_allow_html=True)
    st.write("""
    #### 🔹 Kepribadian:
    - Social (sosial)
    - Active (aktif)
    - Glib (pandai bicara)
    - Curious (penasaran)

    #### 🔹 Ciri Umum:
    - Ramah, energik, percaya diri
    - Terkadang terlalu bersemangat atau keras kepala
    - Pemimpin alami, kompetitif, dan optimis

    #### 📝 Tips Harian:
    - Sarapan tinggi protein (telur, daging)
    - Hindari konsumsi kopi berlebih
    - Jadwalkan olahraga intens secara rutin
             
    #### Kekuatan:
    - Pencernaan kuat terhadap protein hewani
    - Metabolisme tinggi saat mengikuti diet dan latihan yang sesuai

    #### Kelemahan:
    - Rentan terhadap stres berlebihan → naiknya kortisol
    - Masalah lambung (asam tinggi)    
                
    #### Diet Ideal:
    - **Disarankan**: Daging tanpa lemak (sapi, ayam kalkun), ikan (tuna, cod), sayuran hijau, buah (pisang, apel), minyak zaitun
    - **Dihindari**: Produk susu, gluten (roti gandum), jagung, kentang, kacang merah, kafein, alkohol

    #### Aktivitas Fisik:
    - Lari, HIIT, angkat beban, bela diri, kardio berat

    #### Manajemen Stres:
    - Aktivitas fisik terjadwal
    - Tantangan dengan target olahraga dan kompetisi sehat
    """)

st.caption("""
Catatan: Rekomendasi gaya hidup berdasarkan golongan darah ini berasal dari teori kontroversial 'Eat Right for Your Type'. Untuk keputusan yang lebih akurat dan aman, konsultasikan dengan dokter atau ahli gizi.
""")
st.markdown("[Buka Jurnal Korelasi Golongan darah dan Karakter - 2015](https://2024.sci-hub.se/6942/ec15ab76f8acedec4a463122976660ba/10.1371@journal.pone.0126983.pdf?download=true)")

