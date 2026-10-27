from port_checker.checker import check_port

result = check_port("google.com", 443)
print(result["status"])

result = check_port("127.0.0.1", 1)
print(result["status"])

result = check_port("this-domain-definitely-does-not-exist.invalid", 443)
print(result["status"])

result = check_port("", 443)
print(result["status"])