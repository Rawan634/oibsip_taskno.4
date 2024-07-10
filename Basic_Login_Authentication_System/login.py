import tkinter as tk
import bcrypt

users = {}

def show_reg():
    main_frame.pack_forget()
    reg_frame.pack()

def show_login():
    main_frame.pack_forget()
    login_frame.pack()

def reg():
    username = reg_username_entry.get().strip()
    password = reg_password_entry.get().strip()

    if username == "" or password == "":
        reg_result_label.config(text="Please enter both username and password.", fg="red")
        return

    if username in users:
        reg_result_label.config(text="Username already taken. Please choose another one.", fg="red")
    else:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        users[username] = hashed_password
        reg_result_label.config(text="Registration successful!", fg="green")
        update_user_count()

def log():
    username = login_username_entry.get().strip()
    password = login_password_entry.get().strip()

    if username == "" or password == "":
        login_result_label.config(text="Please enter both username and password.", fg="red")
        return

    if username in users and bcrypt.checkpw(password.encode('utf-8'), users[username]):
        login_result_label.config(text=f"Welcome back, {username}!", fg="green")
        secured()
    else:
        login_result_label.config(text="Invalid username or password.", fg="red")

def secured():
    login_frame.pack_forget()
    reg_frame.pack_forget()
    secured_label.config(text="Welcome to the secured page.")
    secured_label.pack(pady=10)
    logout_button.pack(pady=10)

def show_options():
    login_frame.pack_forget()
    reg_frame.pack_forget()
    secured_label.pack_forget()
    logout_button.pack_forget()
    main_frame.pack()

def update_user_count():
    user_count_label.config(text=f"Registered Users: {len(users)}")

window = tk.Tk()
window.title("Login App")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_width = 400
window_height = 350
x_pos = int((screen_width - window_width) / 2)
y_pos = int((screen_height - window_height) / 2)

window.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

main_frame = tk.Frame(window)

tk.Label(main_frame, text="Options", font=("Arial", 16)).pack(pady=10)

reg_button = tk.Button(main_frame, text="Register", command=show_reg, width=20)
reg_button.pack(pady=5)

login_button = tk.Button(main_frame, text="Login", command=show_login, width=20)
login_button.pack(pady=5)

user_count_label = tk.Label(main_frame, text="Registered Users: 0", font=("Arial", 12))
user_count_label.pack(pady=5)

main_frame.pack()

reg_frame = tk.Frame(window)

tk.Label(reg_frame, text="Registration", font=("Arial", 14)).pack(pady=10)

tk.Label(reg_frame, text="Username:").pack()
reg_username_entry = tk.Entry(reg_frame)
reg_username_entry.pack(pady=5)

tk.Label(reg_frame, text="Password:").pack()
reg_password_entry = tk.Entry(reg_frame, show="*")
reg_password_entry.pack(pady=5)

register_button = tk.Button(reg_frame, text="Register", command=reg)
register_button.pack(pady=5)

reg_result_label = tk.Label(reg_frame, text="", fg="black")
reg_result_label.pack(pady=5)

back_button = tk.Button(reg_frame, text="Back to Options", command=show_options)
back_button.pack(pady=5)

login_frame = tk.Frame(window)

tk.Label(login_frame, text="Login", font=("Arial", 14)).pack(pady=10)

tk.Label(login_frame, text="Username:").pack()
login_username_entry = tk.Entry(login_frame)
login_username_entry.pack(pady=5)

tk.Label(login_frame, text="Password:").pack()
login_password_entry = tk.Entry(login_frame, show="*")
login_password_entry.pack(pady=5)

login_button = tk.Button(login_frame, text="Login", command=log)
login_button.pack(pady=5)

login_result_label = tk.Label(login_frame, text="", fg="black")
login_result_label.pack(pady=5)

back_button = tk.Button(login_frame, text="Back to Options", command=show_options)
back_button.pack(pady=5)

secured_label = tk.Label(window, text="", fg="blue")
logout_button = tk.Button(window, text="Logout", command=show_options)

window.mainloop()
