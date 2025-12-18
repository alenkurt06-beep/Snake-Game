# 🐍 Snake Game with Hand Tracking

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?style=for-the-badge&logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Latest-orange?style=for-the-badge&logo=google)

Bu proje, bilgisayar kamerasını kullanarak **el hareketleriyle (Hand Tracking)** kontrol edilen modern bir Snake Game (Yılan Oyunu) uygulamasıdır. Klasik yılan oyunu deneyimini, görüntü işleme teknolojileriyle birleştirerek etkileşimli bir hale getirir.

---

## 🎮 Oynanış

* **Kontrol:** Yılan, işaret parmağınızın ucunu (`Index Finger Tip`) takip eder.
* **Yem Toplama:** Ekranda beliren nesneleri (Donut vb.) yiyerek puan kazanın.
* **Büyüme:** Her yem yediğinizde yılanın gövdesi uzar.
* **Oyun Sonu:** Yılan kendi gövdesine çarptığında oyun biter.
* **Kısayollar:**
    * `R`: Oyunu yeniden başlatır.
    * `Q`: Oyundan çıkar.

---

## 🚀 Özellikler

- ✅ **Gerçek Zamanlı El Takibi:** MediaPipe tabanlı hassas parmak takibi.
- ✅ **Dinamik Skor Sistemi:** Toplanan yemlere göre anlık skor hesaplama.
- ✅ **Görsel Efektler:** Yılanın boğumlu yapısı ve yem görselleri.
- ✅ **Yeniden Başlatma Modu:** Oyun bittiğinde tek tuşla sıfırlama.

---

## 🛠 Kurulum

1. **Depoyu klonlayın:**

   ```bash
   git clone [https://github.com/alenkurt06-beep/Snake-Game.git](https://github.com/alenkurt06-beep/Snake-Game.git)
   cd Snake-Game
   
2. **Gerekli kütüphaneleri yükleyin:**

pip install -r requirements.txt

Oyunu başlatın:

python snake_game.py

📦 Gereksinimler

Projenin çalışması için aşağıdaki kütüphanelerin yüklü olması gerekir:

opencv-python

cvzone

numpy

mediapipe

📁 Proje Yapısı
Plaintext

Snake-Game/

├── snake_game.py      # Ana oyun döngüsü ve mantığı

├── Donut.png          # Yem olarak kullanılan görsel

├── requirements.txt   # Gerekli Python paketleri

└── README.md          # Proje dökümantasyonu

⚠️ Notlar

Kameranızın başka bir uygulama (Zoom, Teams vb.) tarafından kullanılmadığından emin olun.

En iyi performans için iyi aydınlatılmış bir ortamda oynamanız önerilir.

Arka planın sade olması el takibi hassasiyetini artıracaktır.

👤 Geliştirici
Alen Kurt 🔗(https://github.com/alenkurt06-beep)

📧 E-posta: alenkurt06@gmail.com

⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!
