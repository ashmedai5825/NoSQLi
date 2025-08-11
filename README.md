This repository hosts a Python script designed to automate the process of discovering passwords within a website vulnerable to NoSQL Injection.

First, you should test whether the site is using JSON for querying data, and verify if its parameters can be modified through a proxy such as Burp Suite. You should also check whether it is susceptible to JSON operators or if the use of regex is allowed. If it is confirmed that the site accepts these inputs, you can check for the existence of a user account (for example, “admin”) and then add this user to the script to carry out the attack.

Once this is verified, you will need to modify the script by opening it and following the provided comments. You must change the target URL and the user to test, both in the character length discovery function and in the password discovery function.

The script contains detailed comments on what needs to be modified in order to customize it for the specific website you are attempting to test. It is important to note that this script is intended for educational purposes only, and I do not encourage or promote intrusion into systems that you do not own.
