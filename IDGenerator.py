import random

seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


# 生成唯一的字符串id
def get_dream_id():
    sa = []

    for i in range(10):
        sa.append(random.choice(seed))

    salt = ''.join(sa)
    print("生成的唯一ID" + salt)
    return salt
