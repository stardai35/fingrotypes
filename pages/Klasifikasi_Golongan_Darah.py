import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

# Set judul
st.set_page_config(page_title="Prediksi",page_icon="🩸", layout="wide")

st.title("🔬 Analisis Citra - Identifikasi Golongan Darah dan Pola Sidik Jari")
with st.expander("🧭 Panduan Mandiri: Upload atau Ambil Gambar Sidik Jari", expanded=False):
    st.markdown("""
    Untuk mendapatkan hasil identifikasi golongan darah dan pola sidik jari yang akurat, ikuti panduan berikut ini secara mandiri.

    ### ✅ **Syarat Gambar Sidik Jari**
    - Gambar **grayscale** dan **jelas, fokus**, dan **tidak buram**.
    - Hindari **pantulan cahaya langsung** atau **bayangan gelap**.
    - Gunakan **latar belakang netral**, seperti **kertas putih**
    - Format file: `.jpg`, `.jpeg`, `.png`, atau `.bmp`.
                
    ### 📷 **Langkah Pengambilan Sidik Jari dengan Alat**
    1. Cuci dan keringkan jari jempol Anda.
    2. Buka software pengambil gambar bawaan dari perangkat anda
    3. Ambil gambar jari dan Upload ke Aplikasi ini

    ### 📷 **Langkah Pengambilan Sidik Jari Manual**
    1. Cuci dan keringkan jari jempol Anda.
    2. Ambil Penanda sidik jari seperti tinta cap ke kertas putih/background putih
    3. Ambil foto dari **atas jari** menggunakan kamera HP/laptop, usahakan **tegak lurus**.
    4. Pastikan **seluruh sidik jari** tampak jelas pada foto.
    5. Upload gambar ke aplikasi ini atau gunakan kamera langsung.

    > 📌 **Tips**: semakin kontras sidik jari terlihat semakin cepat prosesnya
    """)
# Load model
# Pastikan path ke model Anda benar
try:
    fingerprint_model = load_model('fingerprint_detection_model.h5')  # Model dengan kelas 'y'/'n'
    model = load_model('best_vgg16_model.h5')
    class_names = ['A', 'AB', 'B', 'O']
except Exception as e:
    st.error(f"Gagal memuat model: {e}. Pastikan file 'best_vgg16_model.h5' ada dan tidak rusak.")
    st.stop() # Hentikan eksekusi jika model tidak dapat dimuat
# Fungsi untuk deteksi apakah gambar adalah sidik jari (y/n)
def check_fingerprint(img):
    img_resized = img.resize((224, 224)).convert("RGB")
    img_array = image.img_to_array(img_resized)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    prediction = fingerprint_model.predict(img_array, verbose=0)
    
    # Jika model output binary (sigmoid)
    if prediction.shape[1] == 1:  # Output tunggal (0-1)
        is_fingerprint = prediction[0][0] > 0.5
        confidence = prediction[0][0] if is_fingerprint else 1 - prediction[0][0]
        return 'y' if is_fingerprint else 'n', confidence * 100
    
    # Jika model output multiclass (softmax)
    else:  # Output dua kelas ['n', 'y']
        class_idx = np.argmax(prediction)
        confidence = np.max(prediction) * 100
        return ('y', confidence) if class_idx == 1 else ('n', confidence)
    
# Fungsi prediksi golongan darah
def predict_blood_type(img):
    img_resized = img.resize((224, 224)).convert("RGB")
    img_array = image.img_to_array(img_resized)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    preds = model.predict(img_array, verbose=0) # verbose=0 untuk menghilangkan output prediksi ke konsol
    label = class_names[np.argmax(preds)]
    confidence = np.max(preds) * 100
    return preds[0], label, confidence

def extract_and_classify_pattern(img_pil):
    img_cv = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
    h, w = img_cv.shape[:2]

    # Konversi ke grayscale untuk pemrosesan
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)

    # Pra-pemrosesan: Gaussian blur untuk mengurangi noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Deteksi tepi menggunakan Canny
    # Coba tuning parameter Canny jika masih banyak noise
    # Misalnya, (70, 200) atau (30, 90)
    edges = cv2.Canny(blur, 50, 150) # Parameter Canny awal, bisa disesuaikan

    # Cari kontur untuk mendapatkan area bounding box yang mencakup semua fitur
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    x1_core, y1_core, x2_core, y2_core = 0, 0, w, h # Inisialisasi dengan seluruh gambar

    if contours:
        # Gabungkan semua kontur untuk mendapatkan area bounding box yang mencakup semua fitur
        x_coords = []
        y_coords = []
        for contour in contours:
            for point in contour:
                x_coords.append(point[0][0])
                y_coords.append(point[0][1])

        if x_coords and y_coords:
            min_x, max_x = min(x_coords), max(x_coords)
            min_y, max_y = min(y_coords), max(y_coords)

            # Tambahkan sedikit padding ke bounding box
            padding = 20
            x1_core = max(0, min_x - padding)
            y1_core = max(0, min_y - padding)
            x2_core = min(w, max_x + padding)
            y2_core = min(h, max_y + padding)
        else: # Jika tidak ada kontur yang ditemukan dari x_coords/y_coords (kasus jarang)
            x1_core, y1_core = w // 4, h // 4
            x2_core, y2_core = x1_core + w // 2, y1_core + h // 2
    else: # Jika tidak ada kontur sama sekali, gunakan bagian tengah default
        x1_core, y1_core = w // 4, h // 4
        x2_core, y2_core = x1_core + w // 2, y1_core + h // 2

    # Pastikan ROI tidak kosong
    if x1_core >= x2_core or y1_core >= y2_core:
        x1_core, y1_core = w // 4, h // 4
        x2_core, y2_core = x1_core + w // 2, y1_core + h // 2

    roi = img_cv[y1_core:y2_core, x1_core:x2_core]
    
    # Jika ROI kosong karena koordinat invalid, gunakan seluruh gambar sebagai fallback
    if roi.size == 0:
        roi = img_cv
        roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    else:
        roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # Pra-pemrosesan ROI
    blur_roi = cv2.GaussianBlur(roi_gray, (5, 5), 0)
    
    # Coba tuning parameter Canny untuk ROI juga
    edges_roi = cv2.Canny(blur_roi, 30, 100) # Parameter Canny awal untuk ROI

    # Menghitung kontur dalam ROI untuk klasifikasi pola
    contours_roi, _ = cv2.findContours(edges_roi, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # --- FILTRASI KONTUR PENTING ---
    # Filter kontur berdasarkan luas area untuk menghilangkan noise kecil
    min_contour_area = 10 # Ambang batas luas area minimum kontur. Sesuaikan!
    filtered_contours_roi = [c for c in contours_roi if cv2.contourArea(c) > min_contour_area]
    
    count_roi = len(filtered_contours_roi) # Gunakan jumlah kontur yang sudah difilter

    # Untuk debugging: Tampilkan jumlah kontur yang terdeteksi
    # print(f"Jumlah kontur yang difilter: {count_roi}")

    # Klasifikasi pola (batas perlu disesuaikan dengan dataset Anda)
    # Ini adalah bagian yang PALING PENTING untuk disesuaikan
    # Berdasarkan eksperimen Anda, ganti nilai 50 dan 150 ini.
    if count_roi < 30: # Contoh: Arch cenderung memiliki kontur paling sedikit
        pattern = "Arch (Lengkung)"
    elif count_roi < 90: # Contoh: Loop memiliki kontur lebih banyak dari Arch, tapi lebih sedikit dari Whorl
        pattern = "Loop (Gelung)"
    else: # Contoh: Whorl cenderung memiliki kontur paling banyak karena pola melingkar kompleks
        pattern = "Whorl (Pusaran)"

    # --- Visualisasi Pola Sebelum Pengotakan ---
    img_pattern_highlighted = img_cv.copy()

    # Highlight pola di dalam ROI dengan warna merah (menggunakan kontur yang sudah difilter)
    for contour in filtered_contours_roi: # Menggunakan filtered_contours_roi
        shifted_contour = contour + np.array([x1_core, y1_core])
        cv2.drawContours(img_pattern_highlighted, [shifted_contour], -1, (0, 0, 255), 1)

    # --- Tambahkan kotak merah pada gambar yang sudah di-highlight pola ---
    cv2.rectangle(img_pattern_highlighted, (x1_core, y1_core), (x2_core, y2_core), (0, 0, 255), 3)

    img_pil_boxed_and_pattern = Image.fromarray(cv2.cvtColor(img_pattern_highlighted, cv2.COLOR_BGR2RGB))
    return img_pil_boxed_and_pattern, pattern


# Upload gambar
uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png", "bmp"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    
    # Tampilkan gambar asli
    col_img_original, col_img_processed = st.columns(2)
    with col_img_original:
        st.subheader("📥 Gambar Asli")
        st.image(img, use_container_width=False, width=200)
    
    # Tombol prediksi
    if st.button("🔍 Prediksi Sekarang !"):
        # Pertama, cek apakah gambar adalah sidik jari (y/n)
        result, confidence = check_fingerprint(img)
        
        if result == 'n':
            st.error(f"⚠️ Gambar bukan sidik jari. Tidak dapat melanjutkan prediksi.")
            st.warning("Silakan upload gambar sidik jari yang valid untuk analisis lebih lanjut.")
            
            # Tampilkan visualisasi (opsional)
            with col_img_processed:
                st.subheader("❌ Hasil Deteksi")
                st.image(img, use_container_width=False, width=200, 
                        caption="Gambar tidak terdeteksi sebagai sidik jari")
        else:
            st.success(f"✅ Gambar terdeteksi sebagai sidik jari (Confidence: {confidence:.2f}%). Melanjutkan analisis...")
            
            # Lanjutkan dengan prediksi golongan darah dan pola
            img_boxed_pattern, pattern = extract_and_classify_pattern(img)
            scores, label, blood_confidence = predict_blood_type(img)
            
            with col_img_processed:
                st.subheader("📋 Ekstraksi Pola dan Hasil Prediksi")
                st.image(img_boxed_pattern, use_container_width=False, width=200)
            
            st.markdown("---")
            
            # Kolom untuk Ringkasan dan Grafik Confidence Score
            col_summary, col_chart = st.columns([1, 2])
            
            with col_summary:
                st.subheader("📋 INFORMASI GOLONGAN DARAH")
                df = pd.DataFrame({
                    'Kategori': ['Golongan Darah', 'Pola Sidik Jari'],
                    'Hasil': [label, pattern],
                    'Confidence': [ f"{blood_confidence:.2f}%", "-"]
                })
                st.table(df)
                st.markdown(
    """
    <a href="https://fingrotype.streamlit.app/Tentang_Golongan_Darah" target="_self">
        <button style="
            background-color:#008CBA;
            border:none;
            color:white;
            padding:10px 20px;
            text-align:center;
            text-decoration:none;
            display:inline-block;
            font-size:16px;
            margin:4px 2px;
            cursor:pointer;">
            👉 Lihat Penjelasan Lengkap Golongan Darah
        </button>
    </a>
    """,
    unsafe_allow_html=True
)
            
            with col_chart:
                st.subheader("📊 Confidence Score Golongan Darah")
                fig, ax = plt.subplots(figsize=(8, 5))
                bar_colors = ['#4caf50', '#2196f3', '#ff9800', '#f44336']
                bars = ax.bar(class_names, scores * 100, color=bar_colors)
                ax.set_ylim([0, 100])
                ax.set_ylabel("Confidence (%)")
                ax.set_xlabel("Golongan Darah")
                ax.set_title("Distribusi Confidence Score")
                
                for bar in bars:
                    yval = bar.get_height()
                    ax.text(bar.get_x() + bar.get_width()/2, yval + 1, round(yval, 2), 
                            ha='center', va='bottom')
                
                st.pyplot(fig)
else:
    st.info("Silakan upload gambar sidik jari terlebih dahulu untuk memulai.")
