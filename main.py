import tkinter as tk
import requests
import json

def fetch_and_save_data():
    id = id_entry.get()
    try:
        response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id}")
        if response.status_code == 200:
            data = response.json()
            with open(f"post_{id}.json", "w") as file:
                json.dump(data, file, indent=4)
            result_label.config(text="Данные сохранены в файл.")
        else:
            result_label.config(text="Ошибка при запросе данных.")
    except requests.exceptions.RequestException:
        result_label.config(text="Ошибка при выполнении запроса.")

window = tk.Tk()
window.title("Запрос данных JSONPlaceholder")
id_label = tk.Label(window, text="Введите ID:")
id_label.pack()
id_entry = tk.Entry(window)
id_entry.pack()
fetch_button = tk.Button(window, text="Запросить и сохранить", command=fetch_and_save_data)
fetch_button.pack()
result_label = tk.Label(window, text="")
result_label.pack()
window.mainloop()