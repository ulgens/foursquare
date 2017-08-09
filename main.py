from settings import fs_client

print("Auth URL: {}".format(fs_client.oauth.auth_url()))

code = input("Enter the code from URL: ")
access_token = fs_client.oauth.get_token(code)
fs_client.set_access_token(access_token)
