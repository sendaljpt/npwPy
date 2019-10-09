import json
import requests

DIRJEN_PAJAK = 'https://sse3.pajak.go.id/cekWsDataWp'

def check(npwp_number):
    body = {
        "npwp": npwp_number
    }

    npwp_header = {
        "Content-Type": "application/json"
    }

    body_fix = json.dumps(body)

    result = requests.post(url=DIRJEN_PAJAK, data=body_fix, headers=npwp_header)

    res_code = result.status_code

    response = {
        'status': 200,
        'data': [],
        'message': 'success'
    }

    if res_code != 200:
        response["message"] = 'something error in dirjen pajak'

    else:
        res_json = result.json()
        res_data = res_json.get('data')

        if len(res_data) < 1:
            response["message"] = 'npwp number not found'

        else:
            res_data_final = res_data[0]
            response["data"] = res_data_final

    return response

