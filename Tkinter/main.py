import tkinter as tk

root = tk.Tk()
root.title("Form")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


# ----------------
def add_to_list(user_input, item_list):
    text = user_input.get()
    if text:
        item_list.insert(0, text)
        user_input.delete(0, tk.END)

def clear_list(user_input, item_list):
    user_input.delete(0, tk.END)
    item_list.delete(0, tk.END)

# --------------
main_frame = tk.Frame(root)
main_frame.grid(row=0, column=0, sticky="nsew")
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)

entry = tk.Entry(main_frame)
entry.grid(row=0, column=0, sticky="ew")

entry.bind("<Return>", lambda event: add_to_list(entry, text_list))
entry.bind("<Escape>", lambda event: clear_list(entry, text_list))

entry_btn = tk.Button(main_frame, text="Add", command=lambda: add_to_list(entry, text_list))
entry_btn.grid(row=0, column=1)

clear_btn = tk.Button(main_frame, text="Clear list", command=lambda: clear_list(entry, text_list))
clear_btn.grid(row=0, column=2)

text_list = tk.Listbox(main_frame)
text_list.grid(row=1, column=0, columnspan=3, sticky="nsew")

frame2 = tk.Frame(root)
frame2.grid(row=0, column=3, sticky="nsew")
frame2.columnconfigure(3, weight=1)
frame2.rowconfigure(1, weight=1)


entry2 = tk.Entry(frame2)
entry2.grid(row=0, column=3)

add2 = tk.Button(frame2, text="Add1", command=lambda: add_to_list(entry2, text_list2))
add2.grid(row=0,column=4)

clear2 = tk.Button(frame2, text="Clear2", command=lambda: clear_list(entry2, text_list2))
clear2.grid(row=0, column=5)

text_list2 = tk.Listbox(frame2)
text_list2.grid(row=1, column=3, columnspan=3, sticky="nsew")



# --------------
root.mainloop()
