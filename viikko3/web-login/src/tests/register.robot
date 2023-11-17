*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Set Username  maija
    Set Password  maija123
    Set Password Confirmation  maija123
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Registration
    Registration Should Fail With Message  Username lenghth should be at least 3 characters

Register With Valid Username And Too Short Password
    Set Username  hanna
    Set Password  oho123
    Set Password Confirmation  oho123
    Submit Registration
    Registration Should Fail With Message  Password should be at least 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Set Username  kaisa
    Set Password  salasana
    Set Password Confirmation  salasana
    Submit Registration
    Registration Should Fail With Message  Password must include numbers

Register With Nonmatching Password And Password Confirmation
    Set Username  henna
    Set Password  salasana678
    Set Password Confirmation  salasana876
    Submit Registration
    Registration Should Fail With Message  Passwords do not match

*** Keywords ***
Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Registration
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Input New Command And Create User
    Create User  heikki  heikki123
    Go To Registration Page
    Register Page Should Be Open
