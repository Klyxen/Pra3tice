import string

#main class
class Scan:
    def __init__(self, target):
        self.target = target

    def scan(self):
        scan_range = list(string.printable)
        result = ""
        for target_char in self.target: #finds the first character first
            for char in scan_range:
                print(f"Scanning: {repr(char)}")
                if char == target_char:
                    result += char
                    break
        return result

#Give a password, weak or strong
given = "Hanah123_password"

#prints
scanner = Scan(given)
result = scanner.scan()
print("------------------")
print("Found : ", result)
print("_________________")
