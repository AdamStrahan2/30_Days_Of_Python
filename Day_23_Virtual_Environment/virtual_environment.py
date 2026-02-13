# ------ Virtual Environment ------

# ------ Setting Up Virtual Environments ------

# To start with this project, it would be better to have a virtual environment.
# Virtual environments can help us to create an isolated or separate environment.
# This will help us to avoid conflicts in dependencies across projects.
# If you write pip freeze on your terminal you will see all the installed packages on your computer:

# >>>pip freeze
# beautifulsoup4==4.14.2
# certifi==2025.10.5
# charset-normalizer==3.4.4
# idna==3.11
# numpy==2.3.4
# pandas==2.3.3
# python-dateutil==2.9.0.post0
# pytz==2025.2
# requests==2.32.5
# six==1.17.0
# soupsieve==2.8
# typing_extensions==4.15.0
# tzdata==2025.2
# urllib3==2.5.0

# If we use virtualenv, we will access only packages which are specific for that project.
# Open your terminal and install virtualenv:

# >>>pip install virtualenv

# Inside the 30DaysOfPython folder create a flask_project folder.
# After installing the virtualenv package go to your project folder and create a virtual env by writing:
# For Mac/Linux: >>>virtualenv venv
# For Windows: >>>python -m venv venv

# Let us check if the the venv was created by using ls (or dir for windows command prompt) command:
# >>> dir venv
#     Directory: C:\Users\adams\PycharmProjects\30DaysOfPython\flask_project\venv
#
# Mode                 LastWriteTime         Length Name
# ----                 -------------         ------ ----
# d-----        05/12/2025     16:42                Include
# d-----        05/12/2025     16:42                Lib
# d-----        05/12/2025     16:42                Scripts
# -a----        05/12/2025     16:42             71 .gitignore
# -a----        05/12/2025     16:42            223 pyvenv.cfg

# Activation of the virtual environment in Windows may vary on Windows Power shell and git bash.
# For Windows Power Shell: >>>venv\Scripts\activate
# For Windows Git bash:    >>>venv\Scripts\. activate

# After you write the activation command, your project directory will start with venv:
# (venv) PS C:\Users\adams\PycharmProjects\30DaysOfPython\flask_project>

# Let's check the available packages in this project by writing pip freeze. You will not see any packages.
# We are going to do a small flask project so let us install flask package to this project:
# (venv) PS C:\Users\adams\PycharmProjects\30DaysOfPython\flask_project> pip install Flask

# Now, let us write pip freeze to see a list of installed packages in the project:
#>>>pip freeze
#blinker==1.9.0
#click==8.3.1
#colorama==0.4.6
#Flask==3.1.2
#itsdangerous==2.2.0
#Jinja2==3.1.6
#MarkupSafe==3.0.3
#Werkzeug==3.1.4

# When you finish you should deactivate active project using deactivate.
# (venv) PS C:\Users\adams\PycharmProjects\30DaysOfPython\flask_project> deactivate
# PS C:\Users\adams\PycharmProjects\30DaysOfPython\flask_project>

# The necessary modules to work with flask are installed.
# Now, your project directory is ready for a flask project.
# You should include the venv to your .gitignore file not to push it to github.