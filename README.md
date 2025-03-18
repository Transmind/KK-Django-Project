
# KK Django Project
A Django webapp based on the code framework setout with chapter 18~20 by the book of <Python Crash Cource 3rd Edition>. In addtion, KK DJango Project added a few items outlined below.
 
 * Integrated TinyMCE rich-text edit, to allow users to enter rich contents into entry, such as pastings pictures 
    (Note, I am using a 14 days free trial key that expires on March 29, 2025. After this day, please apply your free key from Tiny to test the function out. You only need to edit new_entry.html and edit_entry.html by refreshing the key string. Please see the comment in these two files)
 * Allow user to share public topics for all viewers of the site.
 * Modified kk_project/settings.py to avoid using hard-coded secret key. 



## Setup Instructions
1. Clone the repository:

   git clone https://github.com/yourusername/my-django-project.git
   cd my-django-project

2. Create and activate a virtual environment:

   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:

   pip install -r requirements.txt


4. Apply migrations and load initial data. Run below command in the folder containing "manage.py".

   python manage.py makemigrations
   python manage.py migrate


6. Run the development server:

   python manage.py runserver

7. Explore "http://localhost:8000/" in your broswer to test the app locally.

8. Push the app to Platform.sh 
   
   Please to refer chapter 20 of the book for detailed instructions of pushing project onto platform. 
