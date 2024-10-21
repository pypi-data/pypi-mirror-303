import base64

# Base64 encoded cookie value with corrected padding
cookie_value = "BQFmAAEBEFd21DfEba9E7VVGFMyXC3NAZKGsQnOXI126cK_1MFdp0RhswzR7B8IW1JQedBG5B5sPOTMuKirJkW8CBSjfsek1iBrky3SSoa0sPaLX8SvWoA=="

# Correct the padding
while len(cookie_value) % 4 != 0:
    cookie_value += '='

# Decode the cookie value
try:
    decoded_value = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    print(decoded_value)
except Exception as e:
    print(f"Error decoding cookie: {e}")
