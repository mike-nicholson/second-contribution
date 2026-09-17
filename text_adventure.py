"""A small text-based adventure game.

You wake up in an old house and need to find the key and reach the exit.
Commands: go <direction>, look, take <item>, inventory, help, quit
"""

rooms = {
    "hallway": {
        "description": "A dusty hallway. Doors lead north and east.",
        "exits": {"north": "study", "east": "kitchen"},
        "items": [],
    },
    "study": {
        "description": "A study lined with old books. A rusty key sits on the desk.",
        "exits": {"south": "hallway"},
        "items": ["key"],
    },
    "kitchen": {
        "description": "A kitchen with a locked back door.",
        "exits": {"west": "hallway", "east": "garden"},
        "items": [],
        "locked_exit": "east",
    },
    "garden": {
        "description": "A garden with a gate leading to freedom!",
        "exits": {"west": "kitchen"},
        "items": [],
        "is_exit": True,
    },
}


def describe_room(room_name):
    room = rooms[room_name]
    print(f"\n{room['description']}")
    if room["items"]:
        print(f"You see: {', '.join(room['items'])}")
    print(f"Exits: {', '.join(room['exits'])}")


def go(current_room, direction, inventory):
    room = rooms[current_room]
    if direction not in room["exits"]:
        print("You can't go that way.")
        return current_room

    if room.get("locked_exit") == direction and "key" not in inventory:
        print("That door is locked. Maybe you need a key.")
        return current_room

    return room["exits"][direction]


def take(current_room, item_name, inventory):
    room = rooms[current_room]
    if item_name in room["items"]:
        room["items"].remove(item_name)
        inventory.append(item_name)
        print(f"You picked up the {item_name}.")
    else:
        print(f"There's no {item_name} here.")


def print_help():
    print("\nCommands: go <direction>, look, take <item>, inventory, help, quit")


def main():
    current_room = "hallway"
    inventory = []

    print("You wake up in an old house with no memory of how you got here.")
    print_help()
    describe_room(current_room)

    while True:
        command = input("\n> ").strip().lower()
        parts = command.split()

        if not parts:
            continue

        action = parts[0]

        if action == "quit":
            print("Goodbye!")
            break
        elif action == "help":
            print_help()
        elif action == "look":
            describe_room(current_room)
        elif action == "inventory":
            print(f"You are carrying: {', '.join(inventory) if inventory else 'nothing'}")
        elif action == "go" and len(parts) > 1:
            current_room = go(current_room, parts[1], inventory)
            if rooms[current_room].get("is_exit"):
                print("\nYou push open the garden gate and escape the house. You win!")
                break
            describe_room(current_room)
        elif action == "take" and len(parts) > 1:
            take(current_room, parts[1], inventory)
        else:
            print("I don't understand that command.")


if __name__ == "__main__":
    main()
