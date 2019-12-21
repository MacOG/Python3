#!/usr/bin/env python3

## Variables ##

user={ 'admin': True, 'active': False, 'name': 'Shawn' }

if user['admin'] and user['active']:
    print(f"ACTIVE - ADMIN: {user['name']}")
elif user['admin'] or user['active']:
        if user['admin']:
            print(f"ADMIN: {user['name']}")
        elif user['active']:
            print(f"ACTIVE: {user['name']}")
elif not user['admin'] and not user['active']:
    print(user['name'])
