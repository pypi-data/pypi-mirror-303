import requests
import json

from .models import EBillIntegration


def get_active_ebill_integration(company_id=None):
    """
    Get the active EBillIntegration object for the given company.

    Parameters
    ----------
    company_id : UUID
        Company id of the customer.

    Returns
    -------
    EBillIntegration
        EBillIntegration object or None if no active integrator found.
    """

    if not company_id:
        return False

    integrators = EBillIntegration.objects.filter(company_id=company_id, is_active=True, sync=True)
    if integrators.exists():
        return integrators.first()
    return False


def check_and_send_request(method, company_id, url, payload={}, params={}, integration=None):
    """
    Send a request to the given URL with given payload and params.

    Parameters
    ----------
    method : str
        HTTP method (e.g. 'GET', 'POST', 'PUT', 'DELETE').
    company_id : UUID
        Company id of the customer.
    url : str
        URL to send the request to.
    payload : dict, optional
        Payload to send with the request, by default {}
    params : dict, optional
        Parameters to send with the request, by default {}
    integration : EBillIntegration, optional
        EBillIntegration object, by default None

    Returns
    -------
    response : requests.Response
        Response object from the request.
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
    Get a customer from Turmob service with given identity number and company id.

    Parameters
    ----------
    identity_no : str
        Identity number of the customer.
    company_id : int
        Company id of the customer.

    Returns
    -------
    customer : Customer
        Customer object if found, None if not found.
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
