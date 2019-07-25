import recognizer as rec
import image_generator as ig


def start():
    params = ["name", "municipality", "province", "last name", "first name", "middle name",
              "birthday", "status", "citizenship", "street name", "city", "precinct number"]
    values = rec.populate(params)
    ig.create_id(values)


if __name__ == "__main__":
    start()

