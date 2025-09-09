Connect → Login → Upload → Download → Verify → List Directory → Quit

------------------------------
4. DNS (Domain Name System)
------------------------------

What is DNS?
- DNS is like the phonebook of the internet.
- Converts human-readable domain names (like google.com) into IP addresses (142.250.190.14) that computers understand.
- Helps you find websites, email servers, and other services.

How it Works:
1. You provide a domain name.
2. DNS servers return the IP address or other records (A, MX, CNAME).
3. Your computer connects to the server using that IP.

Workflow:
Input Domain → Query A/MX/CNAME → Log Results → Done

------------------------------
Summary Table of Workflows
------------------------------

| Protocol | Workflow |
|----------|---------|
| HTTP     | Connect → Send GET/POST → Receive Response → Log → Done |
| SMTP     | Connect → Start TLS → Login → Send Email → Quit |
| FTP      | Connect → Login → Upload → Download → Verify → List Directory → Quit |
| DNS      | Input Domain → Query A/MX/CNAME → Log Results → Done |
