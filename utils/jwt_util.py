import jwt
import datetime

SECRET_KEY = "my_secret_key"  # 환경변수로 빼는 게 안전
ALGORITHM = "HS256"

def create_token(phone_number, expires_hours=1):
    payload = {
        "phoneNumber": phone_number,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=expires_hours)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    if isinstance(token, bytes):
        token = token.decode('utf-8')
    return token

def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload  # 유효하면 payload 반환
    except jwt.ExpiredSignatureError:
        return None  # 토큰 만료
    except jwt.InvalidTokenError:
        return None  # 잘못된 토큰