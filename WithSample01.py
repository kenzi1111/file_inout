class WithSample01:
    def __enter__(self):
        print("===== Enter!!! =====")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("===== Exit!!! =====")


if __name__ == "__main__":
    with WithSample01():
        print("Hello")
