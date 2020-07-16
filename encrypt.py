>>> stored_password = hash_password('ThisIsAPassWord')
>>> print(stored_password)
cdd5492b89b64f030e8ac2b96b680c650468aad4b24e485f587d7f3e031ce8b63cc7139b18
aba02e1f98edbb531e8a0c8ecf971a61560b17071db5eaa8064a87bcb2304d89812e1d07fe
bfea7c73bda8fbc2204e0407766197bc2be85eada6a5
>>> verify_password(stored_password, 'ThisIsAPassWord')
True
>>> verify_password(stored_password, 'WrongPassword')
False
1
2
3
4
5
6
7
8
9
>>> stored_password = hash_password('ThisIsAPassWord')
>>> print(stored_password)
cdd5492b89b64f030e8ac2b96b680c650468aad4b24e485f587d7f3e031ce8b63cc7139b18
aba02e1f98edbb531e8a0c8ecf971a61560b17071db5eaa8064a87bcb2304d89812e1d07fe
bfea7c73bda8fbc2204e0407766197bc2be85eada6a5
>>> verify_password(stored_password, 'ThisIsAPassWord')
True
>>> verify_password(stored_password, 'WrongPassword')
False