def main():
    """Place your input"""
    x = input("Please enter a smiley or frowney face: ").strip()
    print(convert(x))


def convert(x):
    """Convert to emojis"""
    final_input = x.replace(":(", "🙁").replace(":)", "🙂")
    return final_input


main()