# import json

# class Note:
#     def __init__(self, note_id, topic, category, content):
#         self.note_id = note_id
#         self.topic = topic
#         self.category = category
#         self.content = content
    
#     def to_dict(self):
#         return {
#             "note_id": self.note_id,
#             "topic": self.topic,
#             "category": self.category,
#             "content": self.content
#         }
    
#     @classmethod
#     def from_dict(cls,data):
#         return cls(
#             data["note_id"],
#             data["topic"],
#             data["category"],
#             data["content"]
#         )

# class NoteManager():
#     def __init__(self):
#         self.notes = []
#         self.load_notes()
    
#     def add_note(self, note):

#         # Check for duplicate Note ID
#         for existing_note in self.notes:
#             if existing_note.note_id == note.note_id:
#                 print("Note ID already exists!")
#                 return
        
#         # Add note if ID is unique
#         self.notes.append(note)
#         self.save_notes()
#         print("Note saved successfully!")
    
#     def view_note(self):
#         if not self.notes:
#             print("No notes avaiable.")
#             return

#         print("========== ALL NOTES ==========")
#         for note in self.notes:
#             print(f"Note Id: {note.note_id}")
#             print(f"Topic: {note.topic}")
#             print(f"Category: {note.category}")
#             print(f"Content: {note.content}")
#             print("-----------------------------------")
    
#         print("Total Notes:" , len(self.notes))

#     def search_notes(self, topic):
#         count = 0
#         found = False
        
#         print("========== SEARCH RESULTS ==========")
        
#         for note in self.notes:
#             if topic.lower() in note.topic.lower():
#                 found = True
#                 count += 1
          
#                 print(f"Note Id: {note.note_id}")
#                 print(f"Topic: {note.topic}")
#                 print(f"Category: {note.category}")
#                 print(f"Content: {note.content}")
        
#         if not found:
#             print("No matching notes found!")
#         else:
#             print(count, "matching notes found.")
    
#     def delete_note(self, note_id):
#         found = False
        
#         print("========== DELETE NOTE ==========")
        
#         for note in self.notes:
#             if note_id == note.note_id:
#                 found = True
                
#                 delete_ques = input("Are you sure? (yes/no): ").strip().lower()
                
#                 if delete_ques.lower() == "yes":
#                     self.notes.remove(note)
#                     self.save_notes()
#                     print("Note deleted successfully!")
#                 else:
#                     print("Note deletion cancelled!")
#                 break

#         if not found:
#             print("Note ID not found!")
    
#     def view_categories(self):
#         categories = set()
        
#         print("========== AVAILABLE CATEGORIES ==========")
#         if not self.notes:
#             print("No categories available.")
#             return
        
#         for note in self.notes:
#             categories.add(note.category)
        
#         for index, category in enumerate(sorted(categories), start=1):
#             print(f"{index}.{category}")
        
#         print("Total Categories: ", len(categories)) 

#     def load_notes(self):
#         try:
#             with open("notes.json", "r") as file:
#                 data = json.load(file)
#                 self.notes = [
#                     Note.from_dict(note_data) for note_data in data
#                 ]

#         except FileNotFoundError:
#             self.notes = []
        
#         except json.JSONDecodeError:
#             print("Error: notes.json contains invalid JSON.")
#             self.notes = []
    
#     def save_notes(self):
#         data = [note.to_dict() for note in self.notes]

#         with open("notes.json","w") as file:
#             json.dump(data, file, indent=4)
    
#     def exit_application():
#         print("Thank you for using AI Study Assistant!")
#         print("Keep Learning. Keep Building.")
#         print("Application closed successfully.")
#         return True


# my_notes = NoteManager()

import json

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

def load_notes():
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
            return notes
    except FileNotFoundError:
        return []

def save_notes():
    with open("notes.json","w") as file:
        json.dump(notes,file,indent = 4)

notes = load_notes()


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
    save_notes()
    print("Note saved successfully!")

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
                save_notes()
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

    





    