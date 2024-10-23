# EVTX to CSV Converter

## Açıklama
EVTX to CSV Converter, Windows olay günlüklerini (EVTX) CSV formatına dönüştürmek için kullanılan bir Python sınıfıdır. Bu sınıf, bir JSON dosyası içindeki olay günlüklerini okur ve her birini CSV dosyalarına dönüştürmek için gerekli komutları oluşturur.

## Özellikler
- EVTX dosyalarını CSV formatına dönüştürür.
- JSON dosyasından olay günlükü dosyası isimlerini yükler.
- Geçersiz dosya isimlerini günlüğe kaydeder.
- Dönüştürme işlemini otomatik olarak yapar.

## Gereksinimler
- Python 3.x
- Windows işletim sistemi
- `powershell`

## Kurulum
1. Bu projeyi bilgisayarınıza klonlayın veya indirin.
2. Gerekli Python kütüphaneleri standart kütüphanelerdir, bu nedenle ek bir yükleme işlemi gerektirmemektedir. Projeyi çalıştırmak için sadece Python 3.x kurulu olmalıdır.

## Kullanım
1. `evtx_path.json` adında bir JSON dosyası oluşturun. Aşağıda örnek bir JSON formatı verilmiştir:

    ```json
    {
        "event_logs": [
            {
                "file_name": "Application.evtx",
                "description": "Contains event logs related to the application."
            },
            {
                "file_name": "HardwareEvents.evtx",
                "description": "Contains event logs related to hardware."
            }
        ]
    }
    ```

2. Python dosyasını çalıştırın:

    ```bash
    python EVTX2CSV.py
    ```

## Dosya Yapısı
- `evtx_path.json`: Olay günlüklerinin isimlerini ve açıklamalarını içeren JSON dosyası.
- `log_error.csv`: Dönüştürme işlemi sırasında oluşabilecek hataların kaydedileceği dosya.
- `evtx_csv/`: Dönüştürülmüş CSV dosyalarının kaydedileceği klasör.

## Hata Ayıklama
Herhangi bir hata ile karşılaşırsanız, `log_error.csv` dosyasını kontrol edin. Hatalar burada zaman damgası, hata türü ve hata mesajı ile birlikte kaydedilecektir.

## Katkıda Bulunma

Herhangi bir öneri veya katkıda bulunmak isterseniz, lütfen aşağıdan iletişime geçin.

- E-posta: [akbasselcuk32@gmail.com](mailto:akbasselcuk32@gmail.com)
- LinkedIn: [Mustafa Selçuk Akbaş](https://linkedin.com/in/mustafa-selcuk-akbas)