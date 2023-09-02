# Project-Viparva
A vulnerable application by design


Working:

We currently have three main pages within the system:

1. Login Page
2. Home Page
3. Product Page

Before launching the Flask server, a few essential steps need to be taken:

- First, you'll need to enter the username and password credentials for the SQL database in the "app.py" file.
- Following this, execute the SQL commands provided within the "app.py" file. These commands are crucial for establishing the required tables and columns within the SQL database.

Now, let's delve into the details of each page:




1. **Login Page:**
   This page serves as the initial entry point for users. It's important to note that there exists a significant vulnerability in the form of a potential SQL injection attack. Exploiting this vulnerability involves using SQL payloads, such as the classic example `' OR 'x'='x`, which can be employed to manipulate the login process. Successful exploitation of this vulnerability can allow unauthorized access, circumventing the intended login mechanism. Upon successful compromise, users are redirected to the home page.




![Screenshot (413)](https://github.com/DarkRelay-Security-Labs/Project-Viparva/assets/88880988/de0dad93-1be2-4a5d-a551-d3da2fef0a73)








2. **Home Page:**
   The home page provides various features, but it also harbors a vulnerability related to reflected DOM-based Cross-Site Scripting (XSS) attacks. This means that malicious scripts can be injected into the page's content, which could potentially impact users who interact with the content. Furthermore, the search bar functionality might also be a potential point of exploitation. Users can utilize it to search for products available on the platform. Each product listed on this page has a "Shop Now" button that directs users to the third page.





![Screenshot (414)](https://github.com/DarkRelay-Security-Labs/Project-Viparva/assets/88880988/c457d4ef-97d2-4b10-a102-b4b3e24f0294)









3.** Product Page:**
   On the product page, users can view detailed information about a specific product along with comments and reviews. There's a vulnerability within the review section that leaves it susceptible to stored XSS attacks. When users post comments, these comments are stored in the database. If another user visits the same page, the malicious code within the stored comment might be executed within their browser, potentially leading to unintended consequences.

    It's important to note that the system also offers a reset button, which performs the function of removing all reviews and comments from the database. This can be useful for cleaning up the content and eliminating any potential security risks associated with stored malicious scripts.



![Screenshot (415)](https://github.com/DarkRelay-Security-Labs/Project-Viparva/assets/88880988/a0c997dc-017f-43cf-891d-227fa0778ed7)



