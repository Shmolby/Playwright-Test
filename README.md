# Getting started (IDE)
Make sure that the IDE has python installed.
If you're using an IDE, you can use "Get from VCS" to clone the repository

Go to the green "<> Code" button on the middle top right of the "<> code" tab on github and click it
Copy the HTTPS code into the URL bar of your IDE and choose a directory for the project

An IDE can automatically start creating a Virtual Environment for you
If it doesn't, run the following code in the IDE terminal:

```
python -m venv venv
```

And activate the Virtual Enviroment with:

```
venv\Scripts\activate.bat
```

Once you've done this you can install the required modules through:
```
pip install -r requirements.txt
```

After running this, playwright will be installed.
However, playwright still needs to install the browsers it uses through the following command:
```
playwright install
```

After the installation is done, tests can be run through the IDE itself, or through the command line with the following command:
```
pytest
```
Running a command with only Pytest will not show what's happening, in order to see that the following two arguments can be added:
--headed
  shows the browser as it's running
--slowmo
  Slows down the actions by milliseconds equal to the given number. For example, "--slowmo 500" slows down every action by 500ms/0.5s
For example:
```
pytest --headed --slowmo 500
```


# Getting started (just python and powershell)
Make sure the computer has python installed

Open up PowerShell
Go to a directory where you want the project to be, for example:
```
cd C:\Users\<username>\Pythonprojects
```

Create a directory (e.g. Playwright-test) for the project to be in:

```
mkdir Playwright-test
```

Go to the green "<> Code" button on the middle top right of the "<> code" tab on github and click it
If you have git you can copy the web URL under HTTPS and run:
```
git clone https://github.com/Shmolby/Playwright-Test.git
```
If you don't you can choose "Download ZIP" and unpack the zip in the project folder

After doing this you need to create a virtual environment to run the tests in:
```
python -m venv venv
```

And activate the Virtual Enviroment with:

```
venv\Scripts\activate.bat
```

Once the environment is active you can change directory to the project itself (Playwright-Test-main by default)
```
cd Playwright-Test-main
```
Once you've done this you can install the required modules through:
```
pip install -r requirements.txt
```

After running this, playwright will be installed.
However, playwright still needs to install the browsers it uses through the following command:
```
playwright install
```

After the installation is done, tests can be run through the IDE itself, or through the command line with the following command:
```
pytest
```
Running a command with only Pytest will not show what's happening, in order to see that the following two arguments can be added:
--headed
  shows the browser as it's running
--slowmo
  Slows down the actions by milliseconds equal to the given number. For example, "--slowmo 500" slows down every action by 500ms/0.5s
For example:
```
pytest --headed --slowmo 500
```
