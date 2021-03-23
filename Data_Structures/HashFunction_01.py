#  Copyright (c) 2021.
#  Vyacheslav Shchurov (diskoknife@gmail.com)

"""

Make a simple phone numbers book which can Add number. Delete number. Find
number. Here's over the Stepik task. Additional from me:
1) Book can be read from file where all of the phones can be written
in next patterns:
    a) +00000000000 client;
    b) +0-000-000-000 client;
    c) 123-45-67 client;
    d) 1234567890 client.
    count of cyphers = {5...12}
    numbers must be in only  one style.
    e.g.:
    no hyphens, no pluses.
2) Some control:
    a) Exit from the program only if you print "exit" (file autosaves)
    b) In start of program you have choice between open existing database or make new
    c) If you print "number <client>" -> program shows number of client that you search
    d) Onprint 'whois <number>' -> program shows name of phone number owner

"""

class OuterFile:
    def openfile(self, file, param):
        with open(file, param) as f:
            pass