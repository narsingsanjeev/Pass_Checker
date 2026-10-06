import re
import hashlib
import requests
flag=0
while flag==0:
    print("__________--------CREATE STRONG PASSWORD--------____________")
    print("Your Password must needs to include:")
    print("1.UpperCase Character")
    print("2.LowerCase Character")
    print("3.Length Greater than 8")
    print("4.Special Character[!@#$%^&*]")
    print("5.Number[0-9]")
    s=input("Enter Password:")
    if((re.search(r'[A-Z]',s))and(re.search(r'[a-z]',s))and(re.search(r'[!@#$%^&*]',s))and(len(s)>=8)and(re.search(r'\d',s))):
        flag=1
def check_pwned_password(password):
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]
    
    
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return f"Error connecting to API (Status: {response.status_code})"
    

    breaches = response.text.splitlines()
    
    for line in breaches:
        breached_suffix, count = line.split(":")
        if breached_suffix == suffix:
            return f"Compromised! This password has appeared in {count} data breaches."
            
    return "Clean! This password was not found in known data breaches."

print(f"Testing your password .If your was appeared in real world data breaches:")
print(check_pwned_password(s))
print("-" * 40)
