
from pyscript import document

my_list = ["Khloe Sunga", "David Tecson", "Brielle Maglaqui"]

def check_member(event=None):
    first = document.getElementById("first_name").value.strip()
    last = document.getElementById("last_name").value.strip()
    full_name = f"{first} {last}".strip()

    is_member = full_name.lower() in [
        name.lower() for name in my_list
    ]

    messages = {
        True: f"Congratulations {full_name}! You are now part of the Math Club.",
        False: f"Sorry {full_name}, your name is not on the list."
    }

    result = document.getElementById("result")

    result.innerText = (
        messages[is_member]
        if full_name
        else "Please enter your first and last name."
    )
