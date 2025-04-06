
# KK Django Project
A web-based blogging application that enables users to embed images seamlessly for your logs.

This Django web application is built upon the foundational framework presented in Chapters #18 through #20 of <Python Crash Course, 3rd Edition>. This app incorporates the CKEditor rich-text editor to provide users with an intuitive interface for embedding images within their content. 

Below are new features added upon the basic framework outlined by the book.  
* Integrated the CKEditor rich-text editor to allow users to create and format rich content, including support for image embedding and resizing. Note, to apply image resizing effectively, make sure to select the “Inline” style from the image toolbar after resizing.
* Enabled users to share public topics accessible to all site visitors.  
* Updated kk_project/settings.py to eliminate the use of a hard-coded secret key,  enhancing security.

Note: This implementation currently uses CKEditor under the GPL (General Public License). If your project does not comply with GPL licensing requirements, please replace 'GPL' with your own valid license key in main.js, located in the staticfiles/ckeditor/ directory, then run "python manage.py collectstatic".

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
   python manage.py collectstatic

6. Run the development server:

   python manage.py runserver

7. Explore "http://localhost:8000/" in your broswer to test the app locally.

8. Push the app to Platform.sh to make it live on internet, have fun with friends! 
   
   Please refer to chapter #20 of the book for detailed instructions of pushing project onto platform.sh platform. 

9. To manage or clean up users, topics, or entries, use the python manage.py createsuperuser command to create an administrator account. Once the account is created, you can access the Django admin interface locally at http://localhost:8000/admin or at http://your_web_addr/admin if the application has already been deployed to Platform.sh.
