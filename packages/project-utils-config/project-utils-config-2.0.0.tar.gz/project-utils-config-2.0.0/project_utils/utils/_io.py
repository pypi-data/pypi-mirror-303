import json
import base64
import hashlib


def json_encode(data: dict):
    return json.dumps(data, ensure_ascii=False)


def base64_encode(data: str, encoding: str = "utf-8"):
    bytes_code: bytes = data.encode(encoding=encoding)
    return base64.b64encode(bytes_code)


def md5_encode(data: str, encoding: str = "utf-8"):
    md5: any = hashlib.md5()
    md5.update(data.encode(encoding=encoding))
    return md5.hexdigest()


def sha256_encode(data: str, encoding: str = "utf-8"):
    sha256: any = hashlib.sha256()
    sha256.update(data.encode(encoding=encoding))
    return sha256.hexdigest()


if __name__ == '__main__':
    print(md5_encode("111"))
