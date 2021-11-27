from typing import ClassVar

from coincurve import PrivateKey


class KeyGenerator:
    keys: ClassVar[list[dict[str, str]]] = []

    @staticmethod
    def generate_new_key_pair(save: bool = False) -> dict[str, str]:
        sk = PrivateKey()
        sk_hex = sk.to_hex()
        pk_hex = sk.public_key.format().hex()
        pair = {'public_key': pk_hex, 'secret_key': sk_hex}
        if save:
            keys.append(pair)
        return pair
