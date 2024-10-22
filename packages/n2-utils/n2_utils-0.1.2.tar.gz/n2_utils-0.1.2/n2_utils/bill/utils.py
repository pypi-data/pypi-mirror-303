from django.core.exceptions import ObjectDoesNotExist
import requests

from .models import Application
from .constants import BILL_TYPES
from uuid import UUID


def create_bill(data, company_id, user_id, customer_id):
    """
    Şirket için fatura oluşturur ve ERP sistemine HTTP POST isteği gönderir.

    Bu fonksiyon, verilen verilerle bir fatura oluşturur ve belirtilen şirket için 
    ERP sistemine fatura detaylarını bir HTTP POST isteği ile gönderir.

    Args:
        data (dict): Fatura bilgilerini içeren obje. Aşağıdaki keyler bulunmalıdır:
            - created_user_id (UUID): Faturayı oluşturan kullanıcının UUID'si.
            - company_id (UUID): Faturanın ait olduğu şirketin UUID'si.
            - customer_id (UUID): Faturanın ait olduğu müşterinin UUID'si.
            - ebill_type (int): Fatura tipi. Seçenekler aşağıdaki gibidir:
                - 1: E-Arşiv
                - 2: E-Fatura
                - 3: E-İrsaliye
                - 4: E-SMM
                - 5: E-Arşiv İnternet Satışı
                - 6: E-Müstahsil
                - 7: E-İrsaliye Yaniti
                - 8: E-Gider Pusulası
                - 9: E-Döviz Alım
                - 10: E-Döviz Satış
                - 11: E-Adisyon
                - 12: E-Kıymetli Maden Alım
                - 13: E-Kıymetli Maden Satış
            - bill_type (int): Alış/Satış (örn: 1).
            - subtype (int): Fatura alt tipi.
            - type (int): Fatura türü.
            - category (int): Fatura kategorisi.
            - due_date (datetime): Fatura son ödeme tarihi.
            - issue_date (datetime): Fatura düzenlenme tarihi.
            - exchange_choice_id (int): Döviz seçeneği kimliği.
            - prefix_id (int): Fatura ön eki kimliği.
            - total (float): Faturanın toplam tutarı.

        company_id (UUID): Faturanın ait olduğu şirketin UUID'si.

    Returns:
        dict: ERP sisteminden dönen yanıt. Yanıt başarılıysa JSON formatında döner. 
              Eğer hata oluşursa bir hata mesajı içeren sözlük döner.

    Raises:
        ObjectDoesNotExist: Belirtilen şirket için ERP uygulaması bulunamadığında.
        requests.exceptions.RequestException: HTTP isteği başarısız olduğunda.
    """

    try:
        application = Application.objects.filter(key='ERP', company_id=company_id).first()

        if not application:
            raise ObjectDoesNotExist("ERP uygulaması bulunamadı")

        res = requests.post(
            f'http://{application.url}/api/bookkeep/bill_integration/',
            json=data,
            headers={
                'Authorization': 'Token 45b1b648778ed49cfba088778c99500f0b19a784',
                'Content-Type': 'application/json'
            },
            params={
                'customer_id': customer_id,
                'user_id': user_id,
                'company_id': company_id}
        )

        return res.json()

    except ObjectDoesNotExist as e:

        return str(e)


def get_bill(bill_id: UUID, company_id: UUID, type='export'):
    """
    Fatura bilgilerini getirir.

    Args:
        bill_id (UUID): Fatura UUID'si.
        company_id (UUID): Faturanın ait şirketin UUID'si.
        type (str, optional): Fatura türü. Defaults to 'export'.

    Returns:
        content: Eğer type = 'export' ise, fatura dosyası olarak döner.
        json: Eğer type export dışında bir şey ise, fatura JSON formatında döner.

    Raises:
        ObjectDoesNotExist: Belirtilen şirket için ERP uygulaması bulunamadığında.
        requests.exceptions.RequestException: HTTP isteği başarısız doğunda.
    """

    try:
        application = Application.objects.filter(key='ERP', company_id=company_id).first()

        if not application:
            raise ObjectDoesNotExist("ERP uygulaması bulunamadı")

        res = requests.get(
            f'http://{application.url}/api/bookkeep/bill_integration/',
            headers={
                'Authorization': 'Token 45b1b648778ed49cfba088778c99500f0b19a784',
                'Content-Type': 'application/json'
            },
            params={
                'bill': bill_id,
                'type': type
            }
        )
        if type == 'export':
            return res.content
        else:
            return res.json()

    except ObjectDoesNotExist as e:

        return str(e)


def bill_paid(bill_id: UUID, company_id: UUID):
    """
    Faturanın ödenip ödenmediğini kontrol eder.

    Args:
        bill_id (UUID): Fatura UUID'si.
        company_id (UUID): Faturanın ait şirketin UUID'si.

    Returns:
        dict: ERP sisteminden dönen yanıt. Yanıt başarılıysa JSON formatında döner. 
              Eğer hata oluşursa bir hata mesajı içeren şıklık döner.

    Raises:
        ObjectDoesNotExist: Belirtilen şirket için ERP uygulaması bulunamadığında.
        requests.exceptions.RequestException: HTTP isteği başarısız doğunda.
    """

    try:
        application = Application.objects.filter(key='ERP', company_id=company_id).first()

        if not application:
            raise ObjectDoesNotExist("ERP uygulaması bulunamadı")

        res = requests.get(
            f'http://{application.url}/api/bookkeep/bill_integration/',
            headers={
                'Authorization': 'Token 45b1b648778ed49cfba088778c99500f0b19a784',
                'Content-Type': 'application/json'
            },
            params={
                'bill': bill_id,
                'type': 'bill_paid'
            }
        )

        is_paid = res.json()
        return is_paid
    except ObjectDoesNotExist as e:

        return str(e)
