# Webscraping Wikipedia

This python console app searches for articles on wikipedia and narrates them using Google Text 2 Speech API.

## How to setup?

To run the app, make sure you are using Python 3 and have pipenv installed. To install `pipenv`, run -

```
$ pip3 install pipenv
```

After that, clone this repo and change to the directory -

```
$ git clone https://github.com/aneeshsharma/Webscraping-Wikipedia
$ cd Webscraping-Wikipedia
```

Then use `pipenv` to install all dependencies -

```
$ pipenv install
```

## Launching the interface

First make sure you have your GCloud application credentails inside `secrets/text2speech_token.json` (in the application directory)

Then, starting the interface is simple.

```
$ pipenv run start
```

> Note : Tested and built using Python 3.8
