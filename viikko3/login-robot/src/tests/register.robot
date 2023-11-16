*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  maija  maija123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  salasana123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  a  password123
    Output Should Contain   Username length should be at least 3 characters

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  äääää  password123
    Output Should Contain  Username should consist of letters ^[a-z]+$

Register With Valid Username And Too Short Password
    Input Credentials  heikki  k
    Output Should Contain  Password should be at least 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  lotta  kahdeksan
    Output Should Contain  Password must include numbers

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command

