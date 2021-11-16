from coincurve import PrivateKey

sk = PrivateKey()
pk = sk.public_key

sk_hex = sk.to_hex()
pk_hex = sk.public_key.format().hex()
print(f'Your public key (sharable, wallet address):\n{pk_hex}')
print(f'Your secret key (private - keep this secret!, to sign transactions):\n{sk_hex}')
