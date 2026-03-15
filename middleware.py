# middleware.py

from config import MENUS


def process_menu(session, digit):

    current_menu = session["current_menu"]

    if current_menu not in MENUS:
        return {"error": "Invalid menu"}

    menu = MENUS[current_menu]

    if digit not in menu["options"]:
        return {
            "status": "invalid",
            "prompt": menu["prompt"]
        }

    option = menu["options"][digit]
    action = option["action"]

    if action == "goto":

        target = option["target"]

        session["current_menu"] = target

        return {
            "status": "ok",
            "menu": target,
            "prompt": MENUS[target]["prompt"]
        }

    if action == "end":

        return {
            "status": "hangup",
            "message": option["message"]
        }