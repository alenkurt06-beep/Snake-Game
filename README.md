🐍 Snake Game with Hand Tracking



Bu proje, bilgisayar kamerasını kullanarak el hareketleriyle (Hand Tracking) kontrol edilen modern bir Snake Game (Yılan Oyunu) uygulamasıdır. Klasik yılan oyunu deneyimini, görüntü işleme teknolojileriyle birleştirerek daha etkileşimli ve eğlenceli bir hale getirir.

🎮 Oynanış


Kontrol: Yılan, işaret parmağınızın ucunu (Index Finger Tip) takip eder.


Yem Toplama: Ekranda beliren yemleri (ör. donut) yiyerek puan kazanın.


Büyüme: Her yem yediğinizde yılanın gövdesi uzar.


Oyun Sonu: Yılan kendi gövdesine çarptığında oyun biter.


Kısayollar:


R → Oyunu yeniden başlat


Q → Oyundan çık





🚀 Özellikler


✅ Gerçek Zamanlı El Takibi: Hassas ve düşük gecikmeli parmak takibi


✅ Dinamik Skor Sistemi: Toplanan yemlere göre anlık skor


✅ Görsel Efektler: Boğumlu yılan yapısı ve özel yem görselleri


✅ Tek Tuşla Yeniden Başlatma: Oyun sonrasında hızlı sıfırlama



🛠 Kurulum


Depoyu klonlayın
git clone https://github.com/alenkurt06-beep/Snake-Game.git
cd Snake-Game



Gerekli kütüphaneleri yükleyin
pip install -r requirements.txt



Oyunu başlatın
python snake_game.py




📦 Gereksinimler


opencv-python


cvzone


numpy


mediapipe



Python 3.8+ önerilir.


📁 Proje Yapısı
Snake-Game/
├── snake_game.py      # Ana oyun döngüsü ve mantığı
├── Donut.png          # Yem olarak kullanılan görsel
├── requirements.txt   # Gerekli Python paketleri
└── README.md          # Proje dokümantasyonu


⚠️ Notlar


Kameranızın başka bir uygulama (Zoom, Teams vb.) tarafından kullanılmadığından emin olun.


En iyi performans için iyi aydınlatılmış bir ortamda oynayın.


Sade bir arka plan, el takibi hassasiyetini artırır.



👤 Geliştirici
Alen Kurt
🔗 GitHub: https://github.com/alenkurt06-beep
📧 E-posta: alenkurt06@gmail.com

⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!
