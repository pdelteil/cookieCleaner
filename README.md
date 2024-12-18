# cookieCleaner
The Cookie Cleaner Burp Suite extension enhances web application testing by identifying and removing non-essential cookies from HTTP requests.

1. From the proxy tab you can select a requests.
2. In the extension tab  you can select what cookies to manually remove (known not essential).
3. You can ask the extension to test which cookies are essential. This is done by removing cookies one by one until an error is obtained (404, 400, 500 or other), when that happens that cookie is defined as essential.
4. Other cookies are test for the same behavoir until all cookies are analyzed. 
