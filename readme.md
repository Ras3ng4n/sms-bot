# ⚠️ Ras3ng4n — SMS Load Tester (Etik / İzinli Kullanım)

> **Önemli:** Bu proje *SMS bomber* değildir. Bu repo, SMS altyapılarını **izinli ve yasal** biçimde test etmek, dayanıklılık analizi yapmak ve teslimat/hat yönetimi senaryolarını simüle etmek için hazırlanmış bir *yük test* / *simülatör* aracıdır. İzinsiz mesajlaşma, spam veya başkalarını rahatsız etmek kesinlikle yasaktır. Bu tür kullanımlar için yardım verilmeyecektir.

---

## 🎯 Amaç
- Operasyonel SMS altyapısının sınırlarını ölçmek (izinli testler).  
- Teslimat gecikmesi, hata oranları ve yeniden deneme (retry) davranışlarını değerlendirmek.  
- Sağlayıcı (ör. Twilio) entegrasyonunu test etmek için güvenli, kontrollü bir ortam sağlamak.  
- Detaylı loglama ve raporlama ile sistem davranışını görünür kılmak.

---

## ✨ Yeniden Yorumlanmış Özellikler (Ras3ng4n ilhamlı ama güvenli)
> Aşağıdaki özellikler "yük/ölçek testi" bağlamında kullanılmak üzere tasarlanmıştır.

- **Konfigüre edilebilir concurrency** — aynı anda kaç sanal istemci çalışsın (örnek: 1..50).  
- **Rate limiter & politikalı gönderim** — saniye/dk başına limit; sağlayıcı politikalarına uyum.  
- **Kabul/İzin mekanizması (consent-check)** — test başlamadan önce onay gerektirir (manuel veya otomatik doğrulama).  
- **Sandbox / Test-Provider modu** — gerçek gönderim yerine provider test modunda simülasyon.  
- **Gelişmiş log & rapor** — başarı/oran, hata kodları, latency dağılımları (CSV/JSON).  
- **Retry + exponential backoff** — kısa süreli hatalarda yeniden deneme, agresif retry yok.  
- **Proxy desteği (sadece ağ testi amaçlı)** — SOCKS/HTTP proxy ile ağ davranışı testi (yasal kullanım).  
- **Dry-run modu** — hiçbir gerçek mesaj atılmaz; tüm hatalar/akışlar simüle edilir.  
- **Rate-limit & quota uyarıları** — sağlayıcı limitine yaklaşınca otomatik duraklatma.  
- **CLI + Basit GUI (opsiyonel)** — terminal üzerinden veya basit web arayüzü ile yönetim.  
- **Test senaryoları** — kısa burst, uzun süreli düşük hacim, artan ramp-up gibi kontrollü senaryolar.  
- **İzleme entegrasyonları** — Prometheus/CSV/Slack uyarıları (opsiyonel).

---

## 🛑 Zorunlu Etik & Hukuki Kurallar
1. **Her test için açık yazılı izin alın.** (numara sahibi, müşteri, sistem sahibi vb.)  
2. Testleri yalnızca kendi altyapınızda veya izin verilen test ortamlarında çalıştırın.  
3. Sağlayıcı hizmet şartlarını ihlal etmeyin.  
4. Yasal sonuçlardan proje sahibi sorumlu değildir — hukuki sorumluluğunuz var.  
5. Bu repo kitlesel istenmeyen mesajlaşma araçlarına dönüşmemelidir.

---

## 🧰 Önkoşullar
- Python 3.9+ (örnek).  
- `pip install -r requirements.txt` (örn. requests, click, python-dotenv).  
- Test için sağlayıcı hesabı (sandbox/test modunu tercih edin).  
- `.env` dosyasında API anahtarları — **asla** anahtarları halka açık repo'ya koymayın.

---

## Kurulum (Hızlı)
```bash
git clone https://github.com/Ras3ng4n/sms-bot.git
cd sms-bot
python -m venv venv
source venv/bin/activate  # Linux / macOS
pip3 install -r requirements.txt
python rasengan.py
``` 
