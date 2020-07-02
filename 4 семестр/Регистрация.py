class regstr:
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
    regstr = book()
    regstr.add_guest('Dima')
    regstr.delete_guest('Dima')
    regstr.add_guest('Serega')
    regstr.add_guest('Dima')
    regstr.record_file()
