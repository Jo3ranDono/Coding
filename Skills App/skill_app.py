#!/usr/bin/env Python3

import sqlite3

db = sqlite3.connect("app.db")

cr = db.cursor()

cr.execute("CREATE TABLE if not exists users (user_id integer, name txt)")
cr.execute("CREATE TABLE if not exists skills (name TEXT, progress integer, user_id integer)")

cr.execute("INSERT INTO users(user_id, name) values(1, 'Ahmad')")
cr.execute("INSERT INTO users(user_id, name) values(2, 'Sayed')")
cr.execute("INSERT INTO users(user_id, name) values(3, 'Osama')")

def commit_and_close():
    """Commit Changes and Close Connection To Database"""
    db.commit()
    db.close()
    print("Connection To Database Is Closed")

uid = input("Enter The User ID: ").strip()

input_message = """
What Do You Want To Do ?
"s" => Show All Skills
"a" => Add New Skill
"d" => Delete A Skill
"u" => Update Skill Progress
"q" => Quit The App
Choose Option: 
"""
user_input = input(input_message).strip().lower()

commands_list = ["s", "a", "d", "u", "q"]

def show_skills():
    """Showing Skills"""
    cr.execute(f"select * from skills where user_id = '{uid}'")
    results = cr.fetchall()
    print(f"You Have {len(results)} Skills.")
    if len(results) > 0:
        print("Showing Skills With Progress")
    else:
        print("The User Don't Have Any Skills")
    for row in results:
        print(f"Skill => {row[0]}",end=" ")
        print(f"Skill => {row[1]}%")
    commit_and_close()

def add_skills():
    """Adding New Skill To the skills"""
    skill_name = input("Write Skill Name: ").strip().capitalize()
    cr.execute(f"select name from skills where name = '{skill_name}' and user_id = '{uid}'")
    results = cr.fetchone()
    print(f"{results}")
    if results == None:
        progress = input("Write Skill Progress: ").strip()
        cr.execute(f"insert into skills(name, progress, user_id) values('{skill_name}', '{progress}', '{uid}')")
    else:
        option = input("The Skill Is Exist. Do You Want To Update it? Y/N ").strip().capitalize()
        if option == "Y":
            progress = input("Write The New Skill Progress: ").strip()
            cr.execute(f"update skills set progress = '{progress}' where user_id = '{uid}'")
        else:
            print("Not Added")
    commit_and_close()

def delete_skills():
    """Deleting Skill"""
    skill_name = input("Write Skill Name: ").strip().capitalize()
    cr.execute(f"delete from skills where name = '{skill_name}' and user_id = '{uid}' ")
    commit_and_close()

def update_skills():
    """Updating Skill"""
    skill_name = input("Write Skill Name: ").strip().capitalize()
    progress = input("Write The New Skill Progress: ").strip()
    cr.execute(f"update skills set progress = '{progress}' where user_id = '{uid}' and where name = '{skill_name}'")
    commit_and_close()

if user_input in commands_list:
    if user_input == "s":
        show_skills()
    elif user_input == "a":
        add_skills()
    elif user_input == "d":
        delete_skills()
    elif user_input == "u":
        update_skills()
    else:
        print("App is Clossed")
        commit_and_close()
else:
    print(f"This Command \"{user_input}\" Is Not Found")