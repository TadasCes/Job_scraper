import tkinter as tk
from tkinter import *
from script import get_all_viable_jobs


root = tk.Tk()
root.title("Jobs scraper")
root.geometry("700x700")

# TODO: add scrollbar

canvas = tk.Canvas(root, height=700, width=700, bg="#ccc")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=1, relheight=0.8, rely=0.2)

input_label = Label(root, text="Type in search term")
input_label.place(x=285, y=30)
job_name_input = Entry(root, bd=5)
job_name_input.place(x=260, y=60)


def print_jobs(jobs):
    import webbrowser

    for widget in frame.winfo_children():
        widget.destroy()

    def open_in_broswer(link):
        print(id)
        webbrowser.open_new(link)

    for idx, job in enumerate(jobs):
        def onclick(link=job.link): return open_in_broswer(link)
        label_company = tk.Label(
            frame, text="Company: " + job.company, bg="white")
        label_position = tk.Label(
            frame, text="Position: " + job.position, bg="white")
        label_salary = tk.Label(
            frame, text="Salary: " + job.salary, bg="white")
        open_link = tk.Button(frame, text="Open ad", padx=10, pady=5, fg="white",
                              bg="#13224F", command=onclick)

        Label(frame, text="", bg="white").pack()

        label_company.pack()
        label_position.pack()
        label_salary.pack()
        open_link.pack()


def get_jobs():
    value = job_name_input.get()
    if value != None:
        jobs = get_all_viable_jobs(value)
    print_jobs(jobs)


searchJobs = tk.Button(root, text="Search jobs", padx=10,
                       pady=5, fg="white", bg="#13224F",
                       command=get_jobs)

searchJobs.place(x=300, y=100)


root.mainloop()
