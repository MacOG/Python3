#!/usr/bin/env python3

## Variables

user_list = [ {'admin': True, 'active': True, 'name': 'Shawn'}, {'admin': True, 'active': False, 'name': 'David'}, {'admin': False, 'active': True, 'name': 'Mike'}, {'admin': False, 'active': False, 'name': 'Chris'} ]

count = 1
for user in user_list:
    if user['admin'] and user['active']:
        print(f"Line: {count} | ACTIVE - ADMIN: {user['name']}")
        count += 1
    elif user['admin'] or user['active']:
        if user['admin']:
            print(f"Line: {count} | ADMIN: {user['name']}")
            count += 1
        elif user['active']:
            print(f"Line: {count} | ACTIVE: {user['name']}")
            count += 1
    elif not user['admin'] and not user['active']:
        print(f"Line: {count} | {user['name']}")
        count += 1
