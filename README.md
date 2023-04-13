## Description
This is a command-line application that uses a programming approach called Test-Driven Development (TDD). The tests cover different types of testing, such as acceptance testing, unit testing, and regression testing. 

The app saves data in the memory, so it is not lost even if you close the app. Additionally, I have created my own instance of a database using a JSON file. This helps to store data in a structured way, making it easy to retrieve and manage later.

App is using thread to run an instance of the TODOApp class. This test requires threading because it needs to simulate user input and verify output while testing the persistence of data in the app's database. Running the TODOApp class in a separate thread allows the test to send input to the app and verify its output while also checking whether data is correctly persisted in the database.


## Navigate to src folder and run app
```
python -m todo
```

## Add things to your todos
```
add buy milk
```
## Close app
```
quit
```
## Run all tests
```
python -m unittest discover -v   
```

## Run unit tests

```
python -m unittest discover -k unit -v
```

## Run acceptance tests
```
python -m unittest discover -k acceptance
```