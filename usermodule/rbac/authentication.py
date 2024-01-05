# -*- coding:utf-8 -*-
"""
安全的密码保存与认证思路：

1.密码保存

加密算法：
对称加密：
AES算法：美国国家标准与技术研究院

非对称加密：
sha256

hash算法
sha-256



JWT认证：
《JSON Web Token 入门教程》https://www.ruanyifeng.com/blog/2018/07/json_web_token-tutorial.html


OAuth2认证：
https://learnku.com/articles/20031

passlib:https://passlib.readthedocs.io/en/stable/narr/quickstart.html


什么是跨域？

"""
from typing import Optional
from datetime import datetime, timedelta
import jwt  # pyjwt
from jwt.exceptions import *
import secrets


class JWT:

    # 初始化一个JWT(公用一个key，还是每个用户独立的key？)
    def __init__(
            self,
            private_key: str,
            public_key: str,
            algorithm: str = "HS256",
            access_expiration: int = 60,
            refresh_expiration: int = 60 * 60 * 24 * 15,
    ) -> None:

        self._private_key = private_key
        self._public_key = public_key
        self.algorithm = algorithm
        self.access_expiration = access_expiration
        self.refresh_expiration = refresh_expiration

    def create_token(
            self, payload: dict,
            token_type: str,
            expiration_delta: Optional[int] = None
    ) -> str:
        iat = datetime.utcnow()
        if expiration_delta:
            exp = datetime.utcnow() + timedelta(seconds=expiration_delta)
        else:
            exp = datetime.utcnow() + timedelta(seconds=60)

        # payload |= {"iat": iat, "exp": exp, "type": token_type}
        payload.update({"iat": iat, "exp": exp, "type": token_type})
        token = jwt.encode(payload, self._private_key, algorithm=self.algorithm)
        return token.decode("utf-8") if isinstance(token, bytes) else token

    def create_access_token(self, payload: dict) -> str:
        return self.create_token(payload, "access", self.access_expiration)

    def create_refresh_token(self, payload: dict) -> str:
        return self.create_token(payload, "refresh", self.refresh_expiration)

    def create_token_pair(self, payload: dict) -> tuple:
        access_token = self.create_access_token(payload)
        refresh_token = self.create_refresh_token(payload)
        return access_token, refresh_token

    def decode_token(self, token: str, leeway: int = 0) -> Optional[dict]:
        try:
            payload = jwt.decode(
                token,
                self._public_key,
                leeway=leeway,
                algorithms=self.algorithm,
            )
            return payload
        except ExpiredSignatureError:
            print("JWT签名已过期")
            return None
        except ImmatureSignatureError:
            print("JWT签名尚未生效")
            return None
        except InvalidSignatureError:
            print("JWT签名验证失败")
            return None
        except Exception as e:
            print(e)
            return None

    def update_tokens_with_refresh_token(self, refresh_token: str) -> Optional[tuple]:
        payload = self.decode_token(refresh_token)
        if payload:
            return self.create_token_pair(payload)
        print("update failed")
        return None

class Auth:
    pass

if __name__ == '__main__':


    #测试过期能否被发现
    print("[测试access签名过期]"+"-"*10)
    key = secrets.token_urlsafe()
    j = JWT(private_key=key,public_key=key,access_expiration=1,refresh_expiration=60*1)
    info = {
        "usermodule": "zwp"
    }
    access_token1, refresh_token1 = j.create_token_pair(info)
    import time
    time.sleep(1)
    print("[过期解码结果]" + "-" * 10)
    dainfo = j.decode_token(access_token1)
    print("dainfo",dainfo)
    print("[没过期解码结果]" + "-" * 10)
    dfinfo = j.decode_token(refresh_token1)
    print("dfinfo",dfinfo)

    print("[没过期update结果]" + "-" * 10)
    res = j.update_tokens_with_refresh_token(refresh_token1)
    print(res)
    time.sleep(60)
    print("[过期update结果]" + "-" * 10)
    res = j.update_tokens_with_refresh_token(refresh_token1)
    print(res)
    print("-"*10)

    print("[检查篡改]" + "-" * 10)
    key2 = secrets.token_urlsafe()
    j2 = JWT(private_key=key2, public_key=key2, access_expiration=1, refresh_expiration=60 * 60)
    #测试篡改能否被发现
    j2.decode_token(refresh_token1)
    j2.decode_token(access_token1)
