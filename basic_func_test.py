from MS.basic_functions.funcs import Base

if __name__ == '__main__':
    database = Base()
    database.createBase()
    user = {
        "imie": "Kamil",
        "nazwisko": "Z",
        "album": "1"
    }

    database.createUser(user, "id1")

    #database.deleteUser("id1")

    plik1 = {
        "nazwa": "1.jpg",
        "path": "C:\\Users\\Kamil\\Desktop\\baza\\1.jpg",
        "opis": "Okładka tomu nr. 1",
    }
    plik2 = {
        "nazwa": "2.jpg",
        "path": "C:\\Users\\Kamil\\Desktop\\baza\\2.jpg",
        "opis": "Okładka tomu nr. 2",
    }
    plik3 = {
        "nazwa": "recenzja.docx",
        "path": "C:\\Users\\Kamil\\Desktop\\baza\\recenzja.docx",
        "opis": "Recenzja komiksu",
    }

    database.createFile("id1", ["tom1", "komiks", "okladka", "NOSQL"], plik1)
    database.createFile("id1", ["tom2","komiks", "okladka"], plik2)
    database.createFile("id1", ["komiks", "recenzja"], plik3)

    database.deleteFileFromTag("id1", "komiks", "recenzja.docx")

    database.searchFileByTag("id1", "komiks")
    #database.searchFileByTag("id1", "okladka")
    #database.searchFileByTag("id1", "recenzja")

    #database.deleteTag("id1", "NOSQL")
    #database.searchFileByTag("id1", "NOSQL")
    #database.searchFileByTag("id1", "tom1")

    #database.addTagToFile("id1", "Islandia", "recenzja.docx")
    #database.searchFileByTag("id1", "Islandia")

    database._showBase()