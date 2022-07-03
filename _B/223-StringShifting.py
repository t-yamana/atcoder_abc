
if __name__ == '__main__':
    text = input()

    prior = text
    later = text

    for i in range(len(text)):
        shifted = text[i::] + text[:i:]
        prior = min(prior, shifted)
        later = max(later, shifted)

    print(prior)
    print(later)
