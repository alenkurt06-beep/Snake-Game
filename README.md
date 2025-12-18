# 🐍 Snake Game (Hand Tracking)

Bu proje, **Python**, **OpenCV** ve **cvzone** kullanılarak geliştirilmiş,
**el hareketleriyle kontrol edilen** bir Snake Game uygulamasıdır.

Kamera üzerinden elinizi algılar ve **işaret parmağınızla yılanı kontrol edersiniz**.

---

## 🎮 Oynanış

- Yılan, **işaret parmağının hareketlerini** takip eder
- Yemleri topladıkça:
  - Yılan uzar
  - Skor artar
- Yılan kendi gövdesine çarparsa **GAME OVER**
- `R` tuşu → Oyunu yeniden başlat
- `Q` tuşu → Oyundan çık

---

## 🛠 Kullanılan Teknolojiler

- Python 3
- OpenCV
- cvzone
- NumPy
- Bilgisayar Kamerası (Webcam)
- El Takibi (Hand Tracking)

---

## 📦 Gereksinimler

Aşağıdaki kütüphanelerin yüklü olması gerekir:

⚠️ cvzone kütüphanesi MediaPipe bağımlılığı ile çalışır.

▶️ Çalıştırma

Projeyi klonla:

git clone https://github.com/alenkurt06-beep/Snake-Game.git


Proje klasörüne gir:

cd Snake-Game


Oyunu başlat:

python snake_game.py


📸 Kamera otomatik açılacaktır.

📁 Proje Yapısı

Snake-Game/
│

├── snake_game.py     # Ana oyun dosyası

├── Donut.png         # Yiyecek görseli

└── README.md         # Proje açıklaması

⚠️ Notlar

Kamera çalışmıyorsa başka bir uygulama kullanmıyor olduğundan emin ol

Oyun iyi aydınlatılmış ortamda daha stabil çalışır

El çok hızlı hareket ederse algılama sınırlanır (bilinçli olarak)

🚀 Geliştirme Fikirleri

Seviye sistemi

Ses efektleri

Mobil kamera desteği

Farklı yiyecek türleri

Skor kaydetme

👤 Geliştirici

Alen Kurt

GitHub:
👉 https://github.com/alenkurt06-beep

🎉 İyi eğlenceler! 🐍🎮


---

## ✅ Son Adım: GitHub’a Yükleme

```bash
git add README.md
git commit -m "Add README file"
git push

```bash
pip install opencv-python cvzone numpy
