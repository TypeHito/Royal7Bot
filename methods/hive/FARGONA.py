import create_json
from urllib3.exceptions import InsecureRequestWarning

import requests

USERNAME = 'hoji2'
PASSWORD = 'ddsak34964364'
API_HOST = "https://royaltaxi-fargona.hivelogin.ru"

HEADERS = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "ru,en;q=0.9",
    "content-type": "application/json;charset=UTF-8",
    "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"111\", \"Yandex\";v=\"23\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-api-request": "true",
    # "x-csrf-token": "",
    # "x-xsrf-token": "",
    # "cookie": "",
}

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
SESSION = requests.Session()
SERVICES = {}
OFFICES = {}
FLEETS = {}
CURRENT_SERVICE = 0
CURRENT_OFFICE = 0
CURRENT_FLEET = 0
WAIT_SEC = 0.5


def get(path, include_headers=True, custom_headers={}):
    global SESSION, HEADERS

    h = {}
    if include_headers:
        h = HEADERS.copy()
        h.update(custom_headers)
    response = SESSION.get("{}{}".format(API_HOST, path), headers=h, verify=False)
    return response


def post(path, payload, include_headers=True, form_data=False):
    global SESSION, HEADERS

    h = {}
    if include_headers:
        h = HEADERS.copy()

    if form_data:
        data = payload
    else:
        data = json.dumps(payload).encode("utf-8")

    response = SESSION.post("{}{}".format(API_HOST, path), data=data, headers=h, verify=False)
    return response


def get_param_value(text, pattern):
    idx = text.find(pattern)
    text = text[idx + len(pattern):]
    return text[:text.find("\"")]


def get_oid_token():
    try:
        response = get("/management/")
        token = get_param_value(response.text, "/oidc/auth/")
        return token
    except Exception as e:
        print(e)

    return False


def auth(username, password, phone):
    try:
        oid_token = get_oid_token()
        if oid_token:
            payload = {"username": username, "password": password}
            response = post("/oidc/auth/{}".format(oid_token), payload, False, True)
            text = response.text
            if response.status_code != 200:
                print(text)
                return False

            return get_orders(phone)
    except Exception as e:
        print(e)

    return False


def check_auth():
    try:
        response = post("/management/archive/get-fares-for-selected", {}, True)
        if response.status_code != 200:
            return False

        data = response.json()
        if "response" in data and not data["response"]:
            return False
        return True
    except Exception as e:
        print(e)

    return False


def get_orders(phone):
    payload = {
        "officeIds": None,
        "serviceIds":  [
            199000106778749,
            199000017886863,
            199000000009223,
            199000000009228,
            199000000009229,
            199000000009230,
            199000000009231,
            199000070628531,
            199000000009232,
            199000117471914,
            199000117472621,
            199000000009239,
            199000033796872,
            199000153109515,
            199000055188623,
            199000055189042,
            199000166934783,
            199000087168179,
            199000000009240,
            199000087180571,
            199000046681682,
            199000000009241,
            199000123753807,
            199000000009242,
            199000182071721,
            199000087167939,
            199000000009251,
            199000000009252,
            199000000009253,
            199000000009254,
            199000000009255,
            199000000009256,
            199000000009257,
            199000000009258,
            199000000009259,
            199000000009260,
            199000000009262,
            199000000009261,
            199000000009268,
            199000000009269,
            199000000009270,
            199000000009271,
            199000000009272,
            199000000009273,
            199000000009274,
            199000000009275
        ],
        "tariffIds": [],
        "sources": [
            "dispatch",
            "mobile",
            "widget",
            "integration"
        ],
        "paymentMethods": [],
        "periodStart": "2023-09-07T00:00",
        "periodEnd": "2023-11-08T00:00",
        "driver": "",
        "deferred": [
            True,
            False
        ],
        "status": [
            "completed"
        ],
        "clientPhone": phone,
        "submissionAddress": "",
        "destinationAddress": "",
        "orderId": None,
        "offset": 0,
        "limit": 1000,
        "driverId": None,
        "vehicleId": None,
        "driverChangedRoute": [],
        "driverPaidForOrder": [
            True,
            False
        ]
    }

    try:
        if not check_auth():
            if not auth(USERNAME, PASSWORD, phone):
                return False

        response = post("/management/archive/get-orders", payload, True)
        if response.status_code != 200:
            return False

        data = response.json()
        print('HTTP Method:', data['state']['total'])
        return data['state']['total']
    except Exception as e:
        print("Ferghana auth:", e)

    return False


def get_count(phone):
    if not check_auth():
        return auth(USERNAME, PASSWORD, phone=phone)
    else:
        return get_orders(phone=phone)