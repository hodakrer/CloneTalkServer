import bcrypt
from repositories.member_repository import save_user, find_user_by_phone
from utils.jwt_util import create_token  # jwt_util의 create_token 사용

class UserExistsError(Exception):
    pass

def register(phone_number, password):
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    try:
        save_user(phone_number, password_hash)
    except Exception as e:
        # sqlite3.IntegrityError 등 DB 에러를 포장해서 던질 수 있음
        raise UserExistsError from e

def login(phone_number, password):
    row = find_user_by_phone(phone_number)
    if row is None:
        return None

    stored_hash = row[0]
    # stored_hash가 str로 들어오는 경우도 대비 (하지만 repository에서 BLOB이므로 bytes여야 함)
    if isinstance(stored_hash, str):
        stored_hash = stored_hash.encode('utf-8')
    if not bcrypt.checkpw(password.encode('utf-8'), stored_hash):
        return None

    # JWT 발급은 jwt_util이 담당
    return create_token(phone_number)