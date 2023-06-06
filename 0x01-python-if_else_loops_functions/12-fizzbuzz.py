#!/usr/bin/python3
def fizzbuzz():
    print(
        "{0}".format(
            "".join(
                "Fizz " if i % 3 == 0 else "Buzz " if i % 5 == 0 else str(i) + " "
                for i in range(1, 101)
            ),
            end=" ",
        )
    )
