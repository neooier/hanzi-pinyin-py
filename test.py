# index.py

from hanzi_pinyin import pinyin, detailed_pinyin, alls

def main():
    # Example usage of the functions
    char = '阿'
    print(f"Pinyin for '{char}': {pinyin(char)}")
    print(f"Detailed Pinyin for '{char}': {detailed_pinyin(char)}")
    # print(f"All entries: {alls()}")

if __name__ == "__main__":
    main()
