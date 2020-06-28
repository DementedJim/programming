class book:
    def __init__(self):
        self.guests = list()

    def add_guest(self, name):
        self.guests.append({"First_name": name})
        
    def delete_guest(self, name): 
        for guest in self.guests:
            if guest.get("First_name") == name:
                self.guests.remove(guest)

    def record_file(self): 
        import json
        with open("./book.json", 'a') as file: #the a flag means open the file for appending
            data = {"Guest_list": self.guests }
            json.dump(data, file) 

if __name__ == '__main__':
    book = book()
    book.add_guest('Dima')
    book.delete_guest('Dima')
    book.add_guest('Serega')
    book.add_guest('Dima')
    book.record_file()