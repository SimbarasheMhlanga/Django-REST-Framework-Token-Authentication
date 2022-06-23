'''importing python's getpass,pprint and requests library in order for our interactive app to run'''
# import database
# from models import User
from getpass import getpass
import pprint
import requests


ENDPOINT_USER_PARENT = "http://localhost:8000/user/parent/"
ENDPOINT_LOGIN = "http://localhost:8000/account/login/"
ENDPOINT_REGISTRATION = "http://localhost:8000/account/register/"
ENDPOINT_LOGOUT = "http://localhost:8000/account/logout/"
ENDPOINT_USER_CHILD_CREATE = "http://localhost:8000/user/parent/pk/child/"
ENDPOINT_USER_CHILD = "http://localhost:8000/user/child/"


DISPLAY_MESSAGE = """\n----Welcome to the Data Store App !----
\nWARNING: ONLY FILL UP REQUIRED FIELDS AND LEAVE OTHER FIELDS EMPTY FOR PARTIAL UPDATE
WARNING: PLEASE DO NOT USE SPACE IN USERNAME WHILE OPTING FOR REGISTRATION
\n
1]  Login
2]  Sign Up
3]  Add Parent
4]  Update Parent
5]  Partial Update Parent
6]  Delete Parent
7]  Add Child
8]  Update Child
9]  Partial Update Child
10] Delete Child
11] View all user data
12] View Child data
13] Logout
14] Exit

Selection: """


def add_signup_data():
    signup_details = {
        'username': input("enter user name: "),
        'email': input("enter email: "),
        'password': input("enter pass: "),
        'password2': input("enter pass again: "),
    }
    return signup_details


def user_parent_data():
    '''Takes input details from user and sends them to database'''
    user_data = {
        'fathersname': input("enter father's name: "),
        'mothersname': input("enter mother's name: "),
        'street': input("enter street name: "),
        'city': input("enter city name: "),
        'zipcode': input("enter state name: ")
    }

    return user_data


def user_child_data():
    '''helps add child data in interactive mode'''
    user_data = {
        'childname': input("enter name: "),
        'schoolname': input("enter school name: ")
    }
    return user_data


def put_data(endpoint, body, headers):
    return requests.put(endpoint, json=body, headers=headers)


def patch_data(endpoint, body, headers):
    return requests.patch(endpoint, json=body, headers=headers)


def delete_data(endpoint, headers):
    return requests.delete(endpoint, headers=headers)


def account_user_data():
    credentials_data = {
        'username': input("enter username: \n"),
        'password': getpass("What is your password?\n")
    }
    return credentials_data


def post_data(endpoint, body, headers=None):
    if headers is not None:
        return requests.post(endpoint, json=body, headers=headers)
    return requests.post(endpoint, json=body)


def view_data(response):
    pprint.pprint(response.json())


def response_modify(response):
    if response.status_code == 200 or response.status_code == 201:

        if response.json()['token'] is not None:
            token = response.json()['token']
            headers = {
                "Authorization": f"Token {token}"
            }

            return headers


def get_data(endpoint, headers):
    return requests.get(endpoint, headers=headers)


def func_mod(endpoint, _id=None):
    if _id is None:
        _id = input(
            "please input parent id so that we can assign child to that parent : ")
        return endpoint.split('pk')[0] + _id + endpoint.split('pk')[1]
    else:
        return endpoint + _id + "/"


# the following operator: walrus operator , was introduced in python 3.8
# and works in later versions

while(user_input := input(DISPLAY_MESSAGE)) != '14':

    if user_input == '1':
        if 'headers_body' not in locals():
            headers_body = ''
            credentials = account_user_data()
            response = post_data(ENDPOINT_LOGIN, credentials)
            if response.status_code != 400:
                headers_body = response_modify(response)
            else:
                print("LOGIN FAILED")
                del headers_body

    elif user_input == '2':
        if 'headers_body' not in locals():
            headers_body = ''
            signup_details = add_signup_data()
            response = post_data(ENDPOINT_REGISTRATION, signup_details)
            if response.status_code != 400:
                headers_body = response_modify(response)
            else:
                print("REGISTRATION FAILED")
                del headers_body

    elif user_input == '3':
        if 'headers_body' in locals():
            user_data = user_parent_data()
            response = post_data(ENDPOINT_USER_PARENT, user_data, headers_body)
            view_data(response)

        else:
            print('PLEASE SIGNUP OR LOGIN')

    elif user_input == '4':
        if 'headers_body' in locals():
            user_data = user_parent_data()
            parent_id = input('enter parent id: ')
            endpoint = func_mod(ENDPOINT_USER_PARENT, parent_id)
            print(endpoint)
            response = put_data(endpoint, user_data, headers_body)
            view_data(response)
        else:
            print('PLEASE SIGNUP OR LOGIN')

    elif user_input == '5':
        if 'headers_body' in locals():
            user_data = {
                key: value for key,
                value in user_parent_data().items() if value}
            parent_id = input('enter parent id: ')
            endpoint = func_mod(ENDPOINT_USER_PARENT, parent_id)
            response = patch_data(endpoint, user_data, headers_body)
            view_data(response)
        else:
            print('PLEASE SIGNUP OR LOGIN')

    elif user_input == '6':
        if 'headers_body' in locals():
            parent_id = input('enter parent id: ')
            endpoint = func_mod(ENDPOINT_USER_PARENT, parent_id)
            response = delete_data(endpoint, headers_body)
            print('Deleted')
        else:
            print('PLEASE SIGNUP OR LOGIN')

    elif user_input == '7':
        if 'headers_body' in locals():
            user_data = user_child_data()
            endpoint = func_mod(ENDPOINT_USER_CHILD)
            response = post_data(endpoint, user_data, headers_body)
            view_data(response)
        else:
            print('PLEASE SIGNUP OR LOGIN')

    elif user_input == '8':
        if 'headers_body' in locals():
            user_data = user_child_data()
            child_id = input('enter child id: ')
            endpoint = func_mod(ENDPOINT_USER_CHILD, child_id)
            print(endpoint)
            response = put_data(endpoint, user_data, headers_body)
            view_data(response)
        else:
            print('PLEASE SIGNUP OR LOGIN')

    elif user_input == '9':
        if 'headers_body' in locals():
            user_data = {
                key: value for key,
                value in user_child_data().items() if value}
            child_id = input('enter child id: ')
            endpoint = func_mod(ENDPOINT_USER_CHILD, child_id)
            response = patch_data(endpoint, user_data, headers_body)
            view_data(response)
        else:
            print('PLEASE SIGNUP OR LOGIN')

    elif user_input == '10':
        if 'headers_body' in locals():
            child_id = input('enter child id: ')
            endpoint = func_mod(ENDPOINT_USER_CHILD, child_id)
            response = delete_data(endpoint, headers_body)
            print('Deleted')
        else:
            print('PLEASE SIGNUP OR LOGIN')

    elif user_input == '11':
        if 'headers_body' in locals():
            print("loading ... ")
            response = get_data(ENDPOINT_USER_PARENT, headers_body)
            view_data(response)

        else:
            print('PLEASE SIGNUP OR LOGIN')

    elif user_input == '12':
        if 'headers_body' in locals():
            print("loading ... ")
            response = get_data(ENDPOINT_USER_CHILD, headers_body)
            view_data(response)
        else:
            print('PLEASE SIGNUP OR LOGIN')

    elif user_input == '13':
        if 'headers_body' in locals():
            resposne = get_data(ENDPOINT_LOGOUT, headers_body)
            print("logged out successfully")
            del headers_body
        else:
            print('YOU HAVE NOT LOGGED IN')
