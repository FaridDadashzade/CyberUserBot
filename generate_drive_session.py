from pydrive.auth import GoogleAuth


def main():
    gauth = GoogleAuth()
    # Qeyd
    gauth.LoadCredentialsFile("secret.json")
    if gauth.credentials is None:
        # Doğrulama
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Restart
        gauth.Refresh()
    else:
        # Kaydedilen kimlik bilgilerini başlat
        gauth.Authorize()
    # Geçerli kimlik bilgilerini bir dosyaya kaydet
    gauth.SaveCredentialsFile("secret.json")


if __name__ == '__main__':
    main()
