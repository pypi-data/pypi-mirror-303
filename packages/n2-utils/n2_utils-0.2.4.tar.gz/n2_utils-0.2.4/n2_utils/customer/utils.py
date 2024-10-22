import requests
import json
from django.core.signing import Signer
import os

from .models import EBillIntegration


def decode_password(password):
    """
    Verilen şifreyi çözer.

    Parameters
    ----------
    password : str
        Şifreli olarak gelen parola.

    Returns
    -------
    decoded_password : str
        Çözülmüş (decoded) parola.
    """
    secret_key = os.getenv('INTEGRATION_HASH_SECRET', 'IvN90w1iPdzA5fohxplmfALOxF9dviH1')
    signer = Signer(key=secret_key)
    decoded_password = signer.unsign_object(password).get('password')
    return decoded_password


def get_active_ebill_integration(company_id=None):
    """
    Verilen şirket için aktif EBillIntegration nesnesini getirir.

    Parameters
    ----------
    company_id : UUID
        Müşterinin şirket ID'si.

    Returns
    -------
    EBillIntegration
        Aktif EBillIntegration nesnesi veya bulunamazsa None.
    """
    if not company_id:
        return False

    integrators = EBillIntegration.objects.filter(company_id=company_id, is_active=True, sync=True)
    if integrators.exists():
        return integrators.first()
    return False


def check_and_send_request(method, company_id, url, payload={}, params={}, integration=None):
    """
    Verilen URL'ye belirtilen yöntem, parametreler ve yük ile bir istek gönderir.

    Parameters
    ----------
    method : str
        HTTP yöntemi (örn: 'GET', 'POST', 'PUT', 'DELETE').
    company_id : UUID
        Müşterinin şirket ID'si.
    url : str
        İsteğin gönderileceği URL.
    payload : dict, optional
        İstekle birlikte gönderilecek yük (JSON), varsayılan olarak {}.
    params : dict, optional
        İstekle birlikte gönderilecek parametreler, varsayılan olarak {}.
    integration : EBillIntegration, optional
        EBillIntegration nesnesi, varsayılan olarak None.

    Returns
    -------
    response : requests.Response
        İstekten dönen yanıt (response) nesnesi.
    """
    if not integration:
        integration = get_active_ebill_integration(company_id)

    if integration:
        headers = {
            'username': integration.username,
            'password': integration.password,
            'Content-Type': 'application/json'
        }
        rest_url = "{0}{1}".format(integration.url, url)
        return requests.request(method, rest_url, params=params, headers=headers, data=payload)
    else:
        print('E-FATURA ENTEGRASYONU BULUNAMADI')
        return False


def get_customer_from_turmob(identity_no, company_id):
    """
    Verilen kimlik numarası ve şirket ID'sine göre Turmob servisinden bir müşteri alır.

    Parameters
    ----------
    identity_no : str
        Müşterinin kimlik numarası.
    company_id : int
        Müşterinin şirket ID'si.

    Returns
    -------
    customer : tuple
        Müşteri bilgisi. Başarılı olup olmadığını belirten bir bool, bir mesaj ve müşteri bilgisi içerir.
    """
    integration = get_active_ebill_integration(company_id)
    url = "MukellefBilgisiSorgulama"

    payload = json.dumps({
        "vknTckn": identity_no,
        "meslekMensubuKey": integration.smmm_turmob_key
    })

    response = check_and_send_request(method='POST', company_id=company_id, url=url, payload=payload, integration=integration)

    if response:
        resp = response.json()
        return resp['IsSucceeded'], resp['Message'], resp["mukellef"]
    return False, "Entegrasyon Hatası", False
