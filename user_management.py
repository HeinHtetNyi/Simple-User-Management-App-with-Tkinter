import tkinter as tk
from tkinter import messagebox, simpledialog
import pandas as pd

USERS = [
    {
        "id": 1,
        "name": "Mg Mg",
        "email": "mgmg@gmail.com",
        "phone": "09-123123"
    },
    {
        "id": 2,
        "name": "Thaw Thaw",
        "email": "thawthaw@gmail.com",
        "phone": "09-123123"
    },
    {
        "id": 3,
        "name": "Su Su",
        "email": "susu@gmail.com",
        "phone": "09-123123"
    }
]

class UserManagementSystem:
    def __init__(self) -> None:
        self.users = USERS
        self.window = tk.Tk()
        # self.window.title = "User Management System"
        self.window.geometry("800x800")

        self.button_frame = tk.Frame(master=self.window, height=200)
        self.button_frame.pack(fill=tk.X)

        self.user_frame = tk.Frame(master=self.window, height=600)
        self.user_frame.pack(fill=tk.X)
        
        self.add_btn = tk.Button(self.button_frame, text="Add", width=6, height=2, bg="green", font=("Arial", 13), command=self.add_user)
        self.add_btn.pack(pady=10, padx=10, side=tk.LEFT)
        
        self.update_btn = tk.Button(self.button_frame, text="Update", width=6, height=2, bg="blue", font=("Arial", 13), command=self.update_user)
        self.update_btn.pack(pady=10, padx=10, side=tk.LEFT)
        
        self.delete_btn = tk.Button(self.button_frame, text="Delete", width=6, height=2, bg="red", font=("Arial", 13), command=self.delete_user)
        self.delete_btn.pack(pady=10, padx=10, side=tk.LEFT)
        
        self.export_btn = tk.Button(self.button_frame, text="Export", width=6, height=2, bg="yellow", font=("Arial", 13), command=self.export_excel)
        self.export_btn.pack(pady=10, padx=10, side=tk.LEFT)
        
        self.show_users()
        
        self.window.mainloop()
        
    
    def add_user(self):
        new_name = simpledialog.askstring("Update User", "Enter new name:")
        new_email = simpledialog.askstring("Update User", "Enter new email:")
        new_phone = simpledialog.askstring("Update User", "Enter new phone number:")

        if self.check_already_exist("email", new_email):
            messagebox.showwarning("Email Duplicate", "Email already exist!")
        else:
            new_user = {
                "id": len(self.users) + 1,
                "name": new_name,
                "email": new_email,
                "phone": new_phone
            }
            self.users.append(new_user)
            messagebox.showinfo("Add Success", "User added successfully!")
            self.clear_frame(self.user_frame)
            self.show_users()
            
        
    def update_user(self):
        id = simpledialog.askstring("Update user", "Enter user id")
        index = self.find_user(id)
        if index != -1:
            new_name = simpledialog.askstring("Update User", "Enter new name:")
            new_email = simpledialog.askstring("Update User", "Enter new email:")
            new_phone = simpledialog.askstring("Update User", "Enter new phone number:")

            if self.check_already_exist("email", new_email):
                messagebox.showwarning("Email Duplicate", "Email already exist!")
            else:
                user = self.users[index]
                if new_name is not None and len(new_name) > 0:
                    user["name"] = new_name
                if new_email is not None and len(new_email) > 0:
                    user["email"] = new_email
                if new_phone is not None and len(new_phone) > 0:
                    user["phone"] = new_phone
                
                messagebox.showinfo("Update Success", "User updated successfully!")
                self.clear_frame(self.user_frame)
                self.show_users()
        else:
            messagebox.showwarning("User Not Found", "Username not found!")
            
    
    def delete_user(self):
        id = simpledialog.askstring("Delete user", "Enter user id")
        index = self.find_user(id)
        if index != -1:
            self.users.pop(index)
            self.clear_frame(self.user_frame)
            self.show_users()
            messagebox.showinfo("Update Success", "User deleted successfully!")
        else:
            messagebox.showwarning("User Not Found", "Username not found!")
            
            
    def export_excel(self):
        if self.users:
            df = pd.DataFrame(self.users)
            df.to_excel("users.xlsx", index=False)
            messagebox.showinfo("Export Success", "Users data exported to users_data.xlsx successfully!")
        else:
            messagebox.showwarning("No Users", "No Users to export")
        
        
    def show_users(self):
        for user in self.users:
            label_text = f"Id: {user['id']} | Name: {user['name']} | Email: {user['email']} | Phone: {user['phone']}"
            self.label = tk.Label(self.user_frame, text=label_text, font=("Arial", 15))
            self.label.pack(pady=5, fill=tk.X)
            
            
    def find_user(self, id):
        print("Id", id)
        for i in range(len(self.users)):
            user = self.users[i]
            if user["id"] == int(id):
                return i
        return -1
    
    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()
            
            
    def check_already_exist(self, key, value):
        for user in self.users:
            return user[key] == value
                
    
    
system = UserManagementSystem()

    

