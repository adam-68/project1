import win32clipboard
import json


def convert_to_dict():

    win32clipboard.OpenClipboard()
    tasks = win32clipboard.GetClipboardData().split("\r\n")
    win32clipboard.CloseClipboard()
    tasks_json = []
    sizes_convert_dict = {
        "35.5W": "5",
        "36W": "5.5",
        "36.5W": "6",
        "37.5W": "6.5",
        "38W": "7",
        "38.5W": "7.5",
        "39W": "8",
        "40W": "8.5",
        "40.5W": "9",
        "41W": "9.5",
        "42W": "10",
        "42.5W": "10.5",
        "43W": "11",
        "44W": "11.5",
        "44.5W": "12",
        "40": "7",
        "40.5": "7.5",
        "41": "8",
        "42": "8.5",
        "42.5": "9",
        "43": "9.5",
        "44": "10",
        "44.5": "10.5",
        "45": "11",
        "45.5": "11.5",
        "46": "12",
        "47": "12.5",
        "47.5": "13",
        "48": "13.5",
        "48.5": "14",
        "49.5": "15"

    }
    try:
        for i in range(len(tasks)):
            row = tasks[i].split("\t")
            task = {
                "id": f"{i+1}".strip(),
                "sku": row[0].strip().lower(),
                "size": sizes_convert_dict[row[1].strip()],
                "webhook_url": row[2].strip(),
                "bypass": row[3].strip().lower(),
                "product_url": row[4].strip(),
            }
            tasks_json.append(task)

        with open("USER_DATA/tasks.json", "w") as file:
            json.dump(tasks_json, file)
    except Exception as error:
        print(f'Task import error: {error}')


convert_to_dict()