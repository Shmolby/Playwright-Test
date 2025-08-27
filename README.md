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
