# n2_utils

## Proje Hakkında

`n2_utils`, bir **Django** uygulaması içinde kullanılan yardımcı modüller ve entegrasyonları içeren bir Python paketi olarak tasarlanmıştır. Farklı bileşenler (`base`, `bill`, `customer`) içinde çeşitli işlevsellikler sağlar. Bu modül, e-fatura ve diğer işlevler için çeşitli yardımcı sınıflar ve fonksiyonlar içerir.

### Ana Bileşenler:

- **base**: Temel sınıflar ve modeller içerir.
- **bill**: Fatura yönetimi ve entegrasyonları ile ilgili işlemler içerir.
- **customer**: Müşteri yönetimi için gerekli olan modeller ve işlevler içerir.

---

## Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki araç ve kütüphanelerin kurulu olması gerekir:

- Python 3.7+
- Django 3.2+
- `requests` kütüphanesi (API talepleri için)

## Kurulum

Projeyi kurmak için aşağıdaki adımları izleyin:

1. Proje dizinini klonlayın:

   ```bash
   git clone <repository-url>
   ```

2. Sanal bir ortam oluşturun ve aktif hale getirin:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate  # Windows
   ```

3. Gereken bağımlılıkları yükleyin:

   ```bash
   pip install -r requirements.txt
   ```

4. `n2_utils` modülünü yüklemek için:
   ```bash
   pip install .
   ```

## Kullanım

1. Projeyi çalıştırmak için Django uygulaması ile entegre edin. Aşağıdaki adımları izleyin:

   a. Django ayar dosyanızda (`settings.py`) `INSTALLED_APPS` kısmına `n2_utils` uygulamasını ekleyin:

   ```python
   INSTALLED_APPS = [
       ...,
       'n2_utils',
   ]
   ```

2. Faturalar ve müşteri bilgileri gibi işlevleri kullanmak için `bill` ve `customer` modüllerine başvurabilirsiniz.

## API Entegrasyonları

`n2_utils` API'ler ile entegrasyon yapar ve örnek bir `GET` ve `POST` isteği kullanımı aşağıdaki gibidir:

```python
from n2_utils.bill import get_customer_from_turmob

response = get_customer_from_turmob(identity_no="12345678901", company_id=1)
```
