class InventoryManager:

    def __init__(self):

        self.items = []

    def add_item(
        self,
        item
    ):

        self.items.append(
            item
        )

        print(
            f"{item} added"
        )

    def show_inventory(self):

        print(
            self.items
        )
