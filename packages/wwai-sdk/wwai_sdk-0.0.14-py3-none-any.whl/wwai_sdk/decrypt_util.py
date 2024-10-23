import base64

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

private_key_base64 = "MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDfbMdpMFSc8cwTa+Q6QFKWsc4hTJmuBCUSQNgvdNal9Q77BlvAHzzWle44ImrjVFs/djMnaWVWPHgmB8TTNqV9Qyvml/SobTtsbqQtTRfjGaTtqr8PJiBoXQxFdvHyO6ZeyhapIal2Jz2USV0l2lA/tPKxzwSQOiHD9D09eq6D/ddgChK3h5pGVl0nCtN3IPmn5WCeJh5HVglfR50dLygdmI76H/HiE02umUuVaTjFKAgJrCHrEp2s34rKDRrnZLTD7+XiKDoFSX6yaiEU/mKxuYofrmCAM1kZ1yVocDENdWxhH1IGLDFykEfoY++LVBumRnlBZnvjXL1pPq//gh2fAgMBAAECggEABKqizvLNpEo1RHyUPkE6AwrAru0I0rEkeGlL+qXFQUnJNSYGBDvCy1/t+KnYs1nU3rz1xuTKfeQdGvzo4q55WLtD7043iSMK7YdcEil847yVN3TsW6vPW86sYxu1Dvr+98DfJfYy3L8SErGmP+mmPnEQQUrSd2liFikuSZqb4DGC8LH3RDUtPg+pyxXLqvkGC/vWT+J1YkgMv7FI0Dwe8k2ZZbuazI7ucS7fbwnANpeNktySYWItlO3ALmnj7yQ/TtMcpQewQwJI99N8nu8dOci7zunCrxIdOfS9upnNH6+pQRLqxUz1c4XLeBhkXYNKJ0eG5oziAkljLBdQ/9r/8QKBgQDuiE2tXdRz0b06Lnqov6wZH3QVHVDqI03FcwacMEpHbpll2bvoew3tgNGjrZaJ78lP8L/mlJ42TFVrQR6BX3FFB/99jlEkAXHKkfepGxCs7697Zy/u4ZJyDf+qkCJ1hhp9/qcUY6F13s9BsDuwG0vxiVaXl6aOmbtfESwMH/Pm8QKBgQDvyUJnQB6qSqkvbHfWidGiuKc56btgM5k7VkHYFsSNMW9d3decBvlYDZ2l3XCjHJswdgglZv6+QmXx/u25aX62weBcVOZl9eabc05CSPaQR4Rp/Y3S3uhp2qFVgGX417iD1RzJHI+kQ/GWvpaw2isTOKUKI3pwC67/X25bVuftjwKBgBFnpLNXu17QGQybw5t4kOgsYV4BC5xqAwy7Peo7o8/ehBbockueXv/LfICC9A8QjhHlMTtz8K9plnoDAGTUQAGXec8BiW4lJNZxHC8cqHTV8GoCt36ouvTTjKo3ZixJIrm60RotwuRE476ZS2GoPDxdlxHsoNya3w8qw5oG4tchAoGABh/z7EM9BUiG7cktfnNiwW9KBjasLJbk0Rkw8V4Tgy/CEnm6Kigbcl5Wqofvepsec6xwJNRuqVl01SuX0uaY7/4fxvv8LpqLW2kklJjcg27wOOzbFInREfMdr9tpv2NzORrWc2ShXqbFov4XR0krVIBb5thlJjuGKsu7O+YKYo0CgYAW6Fc3vVtAhZFFY0HLr90Cb20YMzGHLC0bKURJTXzjksv0aeVy3xLM+ts+o7TSMIroib3KlBMSDc2BDTChOIPhpZMc+Eu25my9Rjw4VgbSfPA05BaqLR7sLhYqi3WODalAcnSY1zOtrQb970x8BVY644PX5giSkLuMenr82SSN/A=="

def decrypt_rsa(encrypt_data: str, private_key=None):
    """
    RSA 解密
    填充模式：Pkcs7
    返回解密后的字符串
    :param private_key:
    :param encrypt_data:
    :return:
    """
    private_key = private_key or private_key_base64
    private_key = base64.b64decode(private_key)
    private_key = serialization.load_der_private_key(private_key, password=None, backend=default_backend())
    decrypt_data = private_key.decrypt(
        base64.b64decode(encrypt_data),
        padding.PKCS1v15()
    )
    return decrypt_data.decode('utf-8')

def decrypt_aes(encrypt_data: str, key: str):
    """
    解密AES
    加密模式：ECB
    :param encrypt_data:
    :param key:
    :return:
    """
    cipher = AES.new(base64.b64decode(key), AES.MODE_ECB)
    text = cipher.decrypt(base64.b64decode(encrypt_data))
    text = unpad(text, AES.block_size)
    return text.decode('utf-8')
