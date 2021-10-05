import sys, os, json, re

PSALMS_WITHOUT_SUPERSCRIPTIONS = ["1","2","10","33","43","71","91","93","94","95","96","97","99","104","105","106","107","111","112","113","114","115","116","117","118","119","135","136","137","146","147","148","149","150"]

def main(origin, source):
    os.chdir(source)
    book_list = open("Books.json", "r")
    book_list_json = json.load(book_list)
    for book in book_list_json:
        book = book.replace(" ", "")
        book_file = open(f"{book}.json", "r")
        book_json = json.load(book_file)
        book_path = make_book(origin, book_json["book"])
        make_chapters(book_path, book_json["chapters"])
        book_file.close()
    book_list.close()
    return

def make_book(origin, title):
    path = os.path.join(origin, title)
    os.mkdir(path)
    return path

def make_chapters(origin, chapters):
    for chapter in chapters:
        path = os.path.join(origin, chapter["chapter"])
        os.mkdir(path)
        make_verse(path, chapter["verses"])
    return

def make_verse(origin, verses):
    if re.search('Psalm', origin) and not origin.split("/")[-1] in PSALMS_WITHOUT_SUPERSCRIPTIONS:
        open(origin + "/0.md", "x")
    for verse in verses:
        number = verse["verse"]
        file = origin + f"/{number}.md"
        open(file, "x")
    return

if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print("Need source folder")
        sys.exit()
    main(os.getcwd(), sys.argv[1])