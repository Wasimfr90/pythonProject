class XYZ:
    def f1(self):
        try:
            a = int(input("Enter a number\n"))
        except Exception as e:
            print("Enter int only value for a")
        else:
            print(a)

        finally:
            print("FINALLY: anyhow I will be printed.")

x = XYZ()
x.f1()