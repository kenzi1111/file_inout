def main():
    # ファイルオブジェクトを生成
    with open("users.csv", "r", encoding="utf-8") as f:
        text = f.read()
        # text = f.readlines()
    users = text.split("\n")

    # print(text)
    # print(users)

    for user in users:
        # 空行は無視する
        if user == "":
            continue

        name, age = user.split(",")

        print(f"Name:{name} Age:{age}")


if __name__ == "__main__":
    # read01()
    main()
