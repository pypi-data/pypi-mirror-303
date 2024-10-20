# vuln_scanner

مكتبة بايثون لاكتشاف الثغرات الشائعة مثل XSS، SQL Injection، LFI، و RFI.

## الاستخدام

```python
from vuln_scanner import scan_xss, scan_sql_injection, scan_lfi, scan_rfi

url = "http://example.com"
external_url = "http://malicious.com/shell.txt"

scan_xss(url)
scan_sql_injection(url)
scan_lfi(url)
scan_rfi(url, external_url)