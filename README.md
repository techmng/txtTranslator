# Text Translator
This app is developed to translate text of one language to selected language text
1. # create python virtual environment
   python -m venv venv
2. # activate virtual environment
   i) # unrestrict terminal for activitating virtual environment. If getting restriction error
        Set-ExecutionPolicy Unrestricted -Scope Process
   ii) # use below command to activate virtual environemnt
        ./venv/Scripts/activate  
3. # Install dependencies
   pip install -r requirement.txt
4. # set flask developement mode
   set FLASK_ENV=development
5. # run flask using below command
   flask run
6. # Open below url in browser
   http://127.0.0.1:5000