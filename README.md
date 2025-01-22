# Cisco Webex Bot Project

A Cisco Webex bot is an automated user within the Webex platform that can be interacted with, enhancing the user experience within an organisation.

# Task 1 - Set up and run hello bot

This first task will get you all set up to run a very simple hello bot that replies with a basic message.

### Create a Webex account

Go to [Cisco Webex for Developers](https://developer.webex.com/) and click **Sign up** on the top right corner. Fill in your details and follow the instructions to create an account.

### Create a Webex Bot

Go back to [Cisco Webex for Developers](https://developer.webex.com/) and log in with your account details.

Click **Documentation** on the top bar and select the **Bots** section on the left. On this [Bots Documentation](https://developer.webex.com/docs/bots) webpage you will find an extended explanation on what Bots are and how to create them.

To proceed, click on the **Create a Bot** button and fill up all the required information to describe your new Bot. Finally, scroll down and click on the **Add Bot** button.

Now that your Bot has been created, save the **Access Token** since you will need it later.

### Install Git

"Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency." [Link to install git](https://git-scm.com/download/).

### Install Python

"Python is an interpreted, high-level, general-purpose programming language" [Link to install the latest python version](https://www.python.org/downloads/).

For Mac and Linux make sure to use Python 3 and that when using the ```python``` command in the terminal that it points to Python 3. You can check this by using the ```python --version``` command. If for whatever reason it points to python 2 (which is now end of life) substitue the python commands with ```python3``` and pip commands with ```pip3```.

### Download Ngrok

"Ngrok exposes local servers behind NATs and firewalls to the public internet over secure tunnels." [Link to download ngrok](https://ngrok.com/download).

## Setup Bot

### 1. Open Terminal and Define Working Directory

Open a terminal and you can start working on your home directory (`/Users/<username>` for macOS, `<root>\Users\<username>` for Windows or `/home/<username>` for Linux). Otherwise, you can navigate to another directory using `cd <other-directory>`.

### 2. Clone git Repository and Install Dependencies

Clone the git repository to your local machine by running the following command on your terminal.

```sh
git clone git@github.com:tomtvr/webex-python-bot-project.git
```

To go to the directory you have just cloned simply run `cd webex-python-bot-project`. Try running `ls` and check that you can see all the files you will need to get your Bot up and running.


We recomend using a python virtual environment to install your dependencies too. You can find help on this [here](https://docs.python.org/3/library/venv.html).

After installing Python, open terminal and run the following command to create a virtual environment:

```sh
python -m venv myvenv
```

This will create a python virtual environment in the code directory for you to use. To use this in the terminal you have to run the following command

### Mac/Linux
```sh
source ./myvenv/bin/activate
```

### Windows
```sh
.\myvenv\Scripts\activate
```

The required dependencies can then be installed using the following pip command:

```sh
pip install -r requirements.txt
```

Remember each time you create a new terminal, you need to activate your virtual environment. Visual Studio Code can help with automatically picking this up, information can be found [here](https://code.visualstudio.com/docs/python/environments#_creating-environments) on how to do this.

When running the virtual environment activation script on Windows, there could be some "Execution Policy" changes needed to do this.

You need to run the following command from the terminal:

```sh
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

More information for this can be found [here](https://docs.python.org/3/library/venv.html) and [here](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.4).

## Run Bot

### 1. Run Ngrok

Unzip the ngrok file that you downloaded above and copy the executable file to the `webex-python-bot-project` folder. On a terminal window, go to this directory and run the following command to expose a web server on port 12000 of your local machine to the internet.

Before you can use ngrok you need to sign up for an account to provide an authorisation key.

Go to https://dashboard.ngrok.com/signup

and follow the steps on: https://dashboard.ngrok.com/get-started/your-authtoken

On the terminal window, you can run this to add your user token:

**Mac and Linux**
```sh
ngrok config add-authtoken <your auth token>
```

**Windows**
```sh
.\ngrok.exe config add-authtoken <your auth token>
```

Then to run ngrok use one of the following commands:

**Mac and Linux**
```sh
ngrok http 12000
```

**Windows**
```sh
.\ngrok.exe http 12000
```

### 2. Configure Access Token

Create a new file named `.env` in the root directory of this project. This is the same folder where `task1.py` is located. Use your favourite text editor to open the `.env` file. If you still do not have one yet, take a quick look at [Visual Studio Code](https://code.visualstudio.com/), [Atom](https://atom.io/) or (in case you are a very brave developer) [Vim](https://www.vim.org).

In the `.env` file, add the following line:

```
WEBEX_TEAMS_ACCESS_TOKEN='<my-bot-access-token>'
```

Replace <my-bot-access-token> with the Access Token you saved during the **Create a Bot** step. Make sure the token is enclosed in quotes, otherwise, it won't be recognised correctly.

Next, open `task1.py`. This file contains the main code for your bot. If this is your first time seeing Python code, here are a few things to note:

- **Indentation Matters**: Python uses indentation to define blocks of code, such as those inside functions or loops. Consistent indentation is crucial for the code to run correctly, so make sure to use the same number of spaces or tabs throughout.
- **Comments for Clarity**: Comments in Python start with a `#` symbol and are used to add explanations or notes about the code. They are not executed by the program and are a great way to make your code more understandable for yourself and others.
- **Defining Functions**: Functions are reusable blocks of code that perform a specific task. They are defined using the `def` keyword, followed by the function name and parentheses.
- **Handling Strings**: Strings are sequences of characters enclosed in quotes, either single (') or double ("). Both types of quotes are used to define string literals in Python.

Additionally, take advantage of syntax highlighting in your text editor. It visually distinguishes different parts of the code, like keywords, strings, and comments, making it easier to read and debug.

### 3. Run Bot

On the terminal window, run the following to get your bot working.

```sh
python task1.py
```

### 4. Interact with your Bot
Login to your [Webex](https://web.webex.com/sign-in) account and **Create a Space** by clicking the **+** button. Then, enter your Bot Username (something like **XXXX@webex.bot**).

To start interacting with the bot, type `@<bot_name>` along with your message. For example, if the bot was called "HelloBot" you would type `@HelloBot hello`

# Task 2 - Getting started with Poll Bot.
The goal of this task is for you to get the poll bot up and running and make a few test polls with the rest of your team.

## Create new poll bot in your bots
Follow the steps of the previous task to create a new bot called "Poll Bot".

## Run the bot
To run the bot, execute in a terminal the command:

```sh
python task2.py
```

Make sure that ngrok is also running like in the previous task in a separate terminal.

## 3. - Create some polls
Login to your [Webex](https://web.webex.com/sign-in) account and **Create a Space** by clicking the **+** button. Then, enter your Bot Username (something like **XXXX@webex.bot**) along with all the people you want to take part in the poll. The bot has four commands: `create poll`, `add option`, `start poll` and `end poll`. To invoke one of those commands, type `@<bot_name>`, a space, and then the command. For example `@PollBot create poll`.

### How to use the bot
1. Start by using the `create poll` command to create an initial poll. The bot will message you 1 to 1 with a card to get started.
2. Everyone in the space can then add options for the poll using the command `add option`. An adaptive card will be messaged 1 to 1 to add the option to the poll.
3. Once all the options have been added use the command `start poll`. An adaptive card should now appear in the space for people to start voting.
4. Once everyone has voted run `end poll` to get the results in the space.

# Task 3 - Make improvements to Poll Bot

 For this section, the aim will be to extend the functionality of the poll bot. As you will have seen from experimenting with it in the previous section, it is quite limited in terms of what it can do. You will be adding new features of your own and addressing some issues with the current implementation.

## Add some new commands
### 1. Add a `help` command

The first new feature that we will add is a `help` command that gives the user a list of the available commands along with a brief description of what each command does. After all, the bot is pretty useless if people don't know how to interact with it!

 - <b>Exercise:</b> Using the code in `task3.py`, add a new command `help` that posts a help message either directly to the user or in the space. This can be just in plain text.
    <details>

    <summary><b>Hint</b></summary>

    You may find it helpful to use the functions `send_direct_message` or `send_message_in_room` which have already been defined for you.

    </details>

### 2. Add a command that gives the current status of a poll

It would also be nice to be able to check the status of an ongoing poll, so that the author can preview the results before closing the poll.

 - <b>Exercise:</b> Define a new command `status poll` that shows the title and description of the poll, whether the poll has started, and if available, the preliminary results.

    This should also include number of votes for each option, as well as the total number of votes submitted.

## Improve error handling

As a developer, you need to be thinking about what can go wrong in your program! In this section, we will identify and address potential sources of errors.

### 1. Identify sources of error

Discuss in your group what would happen if:

+ You enter a command that isn't recognised.
+ When creating a poll, you don't enter a title and/or description before clicking submit.
+ You don't create a poll before trying to start one.
+ You create a poll but don't add any options before trying to start it.
+ You try to add an option after a poll has already started.
+ No votes are recorded before the poll is closed.
+ You try to create a second poll

* <b>Exercise:</b> Try these out to detemine what the current behaviour is and have a think about what the desired behaviour would be.

### 2. Send helpful error messages

In many of the cases in the previous exercise, the program just fails silently :( When things go wrong we should be letting the user know!

+ **Exercise**: Upon receiving an unknown command, send an error message in the space and suggest trying `help` to view list of available commands.

When writing error messages, it is best practice to be clear, precise, and contructive. Note how in the message above, a solution is provided.

+ **Exercise:** If the user tries to start a poll without creating one first, send an error message in the space and suggest trying `create poll`.

## Send a confirmation message upon receiving a vote

In general, users should receive feedback when they invoke a command or submit a reponse to confirm the success of the action. In this task, when a user submits a vote we would like to send them a confirmation message.

 + **Exercise:** Upon submitting a vote, send the user a direct message to confirm that their vote was recorded successfully. This should include the user's choice.

## Allow user to create a second poll

Currently, once invoking the `create poll` command and submitting the description for a poll, any subsequent attempts to use `create poll` are ignored. This is something we need to change!

+ **Exercise:** After a poll has ended, allow the user to create a new one. Make sure that the options and votes recorded are reset.

+ **Exercise:** If a user tries to create a new poll while there is a poll in progress, send a message to tell the current poll needs to be closed before you can create a new one.

## Multiple votes per person :O

As things are, we've got an issue! People can vote multiple times, can you think of a good way to prevent this?

* **Exercise**: Only allow one vote per person. Either send a direct message to the user that they cannot vote more than once, or let the user change their vote and send a new confirmation message.

## Challenge task!

For this challenge, we will be adding a new commmand `ping poll` that sends a direct message to every member of the space that hasn't submitted their vote yet.

* **Exercise**: Implement `ping poll` that fulfills the description above.

When all the members of the space have submitted their votes, it would be nice to have the poll end automatically instead of waiting for the author to end it manually.

* **Exercise**: When everyone has already voted, automatically end the poll and display results.

## Stuck? Tips for Debugging

### Command Line Debugging
Debugging code is a necessary part of programming. Sometimes stepping though the code seeing how values change can help you track down tricky bugs!

Insert the following at the location you want to break into the debugger:
```python
import pdb; pdb.set_trace()
```

When the line above is executed, you will be dropped into the interactive debugger. For an introduction to the various debugger commands you can use, have a look at the link provided in the resources section.

### Debugging in VSCode
VSCode has a package for running and debugging python executables. Make sure to install the VSCode python extension: https://marketplace.visualstudio.com/items?itemName=ms-python.python

To run the task files in VSCode click on the "Run and Debug" section and hit the play button. Breakpoints can be added to the necessary lines and you can interatively step through the debugger.

More information can be found here: https://code.visualstudio.com/docs/python/debugging

# Task 4 - Create a new bot of your own
Now it's time to take everything you have learnt from the previous few tasks and create a bot of your own. 🥳

Here are a few ideas to get you started:
* A bot to help remind you of important events coming up
* A bot to help make notes while in class or a meeting

These are just a few ideas, to help with inspiration check out the bot page here: https://apphub.webex.com/bots

## Extra Resources

* [Cisco Webex for Developers](https://developer.webex.com/docs/platform-introduction): Platform documentation
* [Webex Teams APIs](https://webexteamssdk.readthedocs.io/): Webex Teams SDK documentation
* [Webex Cards Guide](https://developer.webex.com/docs/api/guides/cards): Webex Teams SDK documentation for sending Adaptive Cards
* [Adaptive Cards Spec](https://adaptivecards.io/explorer/): Schema Explorer for Adaptive Cards and interactive online demo
* [Cisco Webex Teams App Hub](https://apphub.webex.com/categories): Get some inspiration to develop your own bot from this list of Cisco Webex Teams Bot examples
* [RapidAPI](https://rapidapi.com/): The world's largest API directory
* [Python Debugger](https://docs.python.org/3/library/pdb.html): An interactive source code debugger for Python programs
