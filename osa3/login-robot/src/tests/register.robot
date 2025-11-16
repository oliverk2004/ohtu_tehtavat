*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  kalle  salasana123
    Input Credentials  kalle  kalle123
    Run Application
    Output Should Contain  User already exists

Register With Too Short Username And Valid Password
    Input Credentials  k  kalle123
    Run Application
    Output Should Contain  Invalid username

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kalle!_  kalle123
    Run Application
    Output Should Contain  Invalid username 

Register With Valid Username And Too Short Password
    Input Credentials  kalle  kalle12
    Output Should Contain  Invalid password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kallekalle
    Run Application
    Output Should Contain  Invalid password

*** Keywords ***
Input New Command
    Input  new
