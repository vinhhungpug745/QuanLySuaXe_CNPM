import requests, hmac, hashlib, json, time,uuid
PARTNER_CODE = "MOMO"
ACCESS_KEY = "F8BBA842ECF85"
SECRET_KEY = "K951B6PE1waDMi640xX08PD3vg6EkVlz"
MOMO_ENDPOINT = "https://test-payment.momo.vn/v2/gateway/api/create"

# payWithATM
# captureWallet

def create_momo_payment(amount, order_info, redirect_url, ipn_url):
    try:
        order_id = str(uuid.uuid4())
        request_id = str(uuid.uuid4())

        # Create signature
        raw_signature = (
            f"accessKey={ACCESS_KEY}&amount={amount}&extraData=&"
            f"ipnUrl={ipn_url}&orderId={order_id}&orderInfo={order_info}&"
            f"partnerCode={PARTNER_CODE}&redirectUrl={redirect_url}&"
            f"requestId={request_id}&requestType=payWithATM"
        )

        signature = hmac.new(
            SECRET_KEY.encode('utf-8'),
            raw_signature.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()

        payload = {
            "partnerCode": PARTNER_CODE,
            "accessKey": ACCESS_KEY,
            "requestId": request_id,
            "amount": str(amount),
            "orderId": order_id,
            "orderInfo": order_info,
            "redirectUrl": redirect_url,
            "ipnUrl": ipn_url,
            "extraData": "",
            "requestType": "payWithATM",
            "signature": signature,
            "lang": "vi"
        }

        print(f"Sending to MoMo:")
        print(f"Endpoint: {MOMO_ENDPOINT}")
        print(f"Order ID: {order_id}")
        print(f"Amount: {amount:,} VNĐ")
        print(f"Payload: {payload}")

        response = requests.post(
            MOMO_ENDPOINT,
            json=payload,
            timeout=10,
            headers={'Content-Type': 'application/json'}
        )

        if response.status_code != 200:
            print(f"Thành công: {response.status_code}")
            return {
                "resultCode": -1,
                "message": f"MoMo API: HTTP {response.status_code}"
            }, None

        response_data = response.json()
        return response_data, order_id
    except Exception as e:
        print(f"Unexpected error in create_momo_payment: {e}")
        return {"resultCode": -1, "message": "Lỗi không xác định"}, None
