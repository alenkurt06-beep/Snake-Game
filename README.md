🐍 Snake Game with Hand Tracking

Bu proje, bilgisayar kamerası aracılığıyla el hareketleriyle kontrol edilen modern bir Snake (Yılan) Oyunudur. Klasik yılan oyununu, görüntü işleme ve el takibi teknolojileriyle birleştirerek etkileşimli bir deneyim sunar.

🎮 Oynanış

Kontrol: Yılan, işaret parmağınızın ucunu (Index Finger Tip) takip eder.

Yem Toplama: Ekranda beliren yemleri yiyerek skor kazanın.

Büyüme: Her yem yendiğinde yılan uzar.

Oyun Sonu: Yılan kendi gövdesine çarptığında oyun biter.

⌨️ Kısayollar

R → Oyunu yeniden başlat

Q → Oyundan çık

🚀 Özellikler

✅ Gerçek Zamanlı El Takibi

✅ Kamera ile Temassız Kontrol

✅ Dinamik Skor Sistemi

✅ Görsel Yem ve Yılan Efektleri

✅ Oyun Sonu & Yeniden Başlatma Mekaniği

🛠 Kurulum

1️⃣ Depoyu Klonlayın

git clone https://github.com/alenkurt06-beep/Snake-Game.git
cd Snake-Game

2️⃣ Gerekli Kütüphaneleri Yükleyin

pip install -r requirements.txt

3️⃣ Oyunu Çalıştırın

python snake_game.py

📦 Gereksinimler

Python 3.8+

opencv-python

mediapipe

cvzone

numpy

📁 Proje Yapısı

Snake-Game/

├── snake_game.py      # Oyun mantığı ve ana döngü

├── Donut.png          # Yem görseli

├── requirements.txt   # Gerekli Python paketleri

└── README.md          # Proje dokümantasyonu

⚠️ Önemli Notlar

Kameranın başka bir uygulama tarafından kullanılmadığından emin olun.

En iyi sonuç için iyi aydınlatılmış bir ortam önerilir.

Sade arka plan, el takibi doğruluğunu artırır.

👤 Geliştirici

Alen Kurt

🔗 GitHub: https://github.com/alenkurt06-beep

📧 E-posta: alenkurt06@gmail.com

⭐ Projeyi beğendiyseniz GitHub’da yıldız vermeyi unutmayın!
