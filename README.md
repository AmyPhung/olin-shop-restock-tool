# Restock App
This repository contains code for a flask app that makes it easier to restock the stock market at Olin College.


## Usage
#### Standard Usage
Visit the app at [olin-stock-market.herokuapp.com](olin-stock-market.herokuapp.com) and use the instructions listed there

#### Development
+ Clone this repository
+ Copy the keys folder from the google drive into the base directory of this project
+ To test locally, first navigate to this repository, then use the following commands:
  + For Linux and Mac:
```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
  + For Windows cmd, use set instead of export:
```
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```
  + For Windows PowerShell, use $env: instead of export:
```
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"
flask run
```
+ Once you are ready to update the app, first login to heroku using `heroku login` (credentials are listed in the gdrive)
+ To push code, run the command `git push heroku master` (If you are using a different branch, you can push using the command `git push heroku branch_name:master`) **Note: You will need to push the keys folder to heroku for the app to work, but make sure you don't push this folder to GitHub!**

## Current Status
#### Built Features:
+ Dual-listbox part selection with search functionality
+ Google Sheets integration
+ QR Code generation
+ Label generation
+ Automatic PDF generator from labels

#### Future Directions:
+ Filters with checkboxes (filter by drawer number, size, finish, length, bolt type, etc.)
+ Do something with the QR codes
+ Add favicon
