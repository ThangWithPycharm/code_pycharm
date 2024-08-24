""" Tạo OTP bảo mật ngẫu nhiên gồm 6 chữ số """
import secrets

secretsGenerator = secrets.SystemRandom()
random_number = secretsGenerator.randrange(100000, 999999)
print(random_number)
