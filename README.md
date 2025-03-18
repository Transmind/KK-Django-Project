
# KK Django Project
A web-based blogging application that enables users to embed images seamlessly for your logs.

This Django web application is built upon the foundational framework presented in Chapters 18 through 20 of <Python Crash Course, 3rd Edition>. This app incorporates the TinyMCE rich-text editor to provide users with an intuitive interface for embedding images within their content. 

Below are the items added upon the basic framework outlined by the book.  
* Integrated the TinyMCE rich-text editor to enable users to input rich content, including the ability to embed images.
    (Note: This implementation currently utilizes a 14-day free trial key from TinyMCE, valid until March 29, 2025. After this date, please replace it with your own free key from TinyMCE to continue testing this feature. To update the key, modify the new_entry.html and edit_entry.html templates by refreshing the key string as indicated in the comments within these files.)
* Enabled users to share public topics accessible to all site visitors.  
* Updated kk_project/settings.py to eliminate the use of a hard-coded secret key,  enhancing security.





## Setup Instructions
1. Clone the repository:

   git clone https://github.com/Transmind/KK-Django-Project.git
   cd my-django-project

2. Create and activate a virtual environment:

   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:

   pip install -r requirements.txt


4. Apply migrations and load initial data. Run below command in the folder containing "manage.py".

   python manage.py migrate


6. Run the development server:

   python manage.py runserver

7. Explore "http://localhost:8000/" in your broswer to test the app locally.

8. Push the app to Platform.sh, and having fun with friends! 
   
   Please to refer chapter 20 of the book for detailed instructions of pushing project onto platform.sh platform. 
