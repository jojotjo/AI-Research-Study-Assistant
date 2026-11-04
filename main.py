def check_choice(choice):
        match choice:
            case 1:
                add_note()
            case 2:
                view_note()
            case 3:
                search_note()
            case 4:
                delete_note()
            case 5:
                view_categories()
            case 6:
                return exit_application()
            case _:
                print("Invalid choice!")
                print("Please enter a number between 1 and 6")

        return False


def add_note():
    note_id_input = int(input("Enter note id: "))

    for note in notes:
        if note["id"] == note_id_input:
            print("Note ID already exists!")
            return
        
    topic_input = input("Enter topic: ")
    category_input = input("Enter category: ")
    notes_input = input("Enter notes: ")
    note = {
        "id" : note_id_input,
        "topic" : topic_input,
        "category" : category_input,
        "content" : notes_input
    }
    notes.append(note)
    print("Note saved successfully!")


notes = []


def view_note():
    if not notes:
        print("No notes available.")
    else:
        print("========== ALL NOTES ==========")
        for note  in notes:
            print("Note ID:", note["id"])
            print("Topic:", note["topic"])
            print("Category:", note["category"])
            print("Content:", note["content"])
            print("-----------------------------------------------")
        print(len(notes))


def search_note():
    search_input = input("Enter topic to search: ")
    found = False
    count = 0
    print("========== SEARCH RESULTS ==========")
    for note in notes:
        if search_input.lower() in note["topic"].lower():
            found = True
            count += 1
            print("Note ID:", note["id"])
            print("Topic:", note["topic"])
            print("Category:", note["category"])
            print("Content:", note["content"])
            print("-----------------------------------------------")

    if not found:
            print("No matching notes found!")
    else:
        print(count, "matching notes found.")


def delete_note():
    delete_note_id_input = int(input("Enter Note ID to delete: "))
    found = False
    print("========== DELETE NOTE ==========")
    for note in notes:
        if delete_note_id_input == note["id"]:
            found = True
            delete_ques = input("Are you sure you want to delete this note? (yes/no): ")
            if delete_ques.lower() == "yes":
                notes.remove(note)
                print("Note deleted successfully!")
            else:
                print("Note deletion cancelled!")
            break

    if not found:
        print("Note ID not found!")


def view_categories():
    categories = set()

    print("========== AVAILABLE CATEGORIES ==========")
    if not notes:
        print("No categories available.")
        return
    
    for note in notes:
        categories.add(note["category"])
    
    for index, category in enumerate(categories, start=1):
        print(f"{index}.{category}")
    
    print("Total Categories : ", len(categories))  


def exit_application():
    print("Thank you for using AI Study Assistant!")
    print("Keep Learning. Keep Building.")
    print("Application closed successfully.")
    return True



while (True):
    print("===========================================================")
    print("                     AI STUDY ASSISTANT                    ")
    print("===========================================================")
    print("1. Add a note")
    print("2. View all notes")
    print("3. Search notes")
    print("4. Delete a note")
    print("5. View categories")
    print("6. Exit")

    choice = int(input("Enter your choice: "))
    
    if check_choice(choice):
        break

    





    