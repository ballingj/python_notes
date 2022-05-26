# https://plum-poppy-0ea.notion.site/Conditionals-Tweet-Checker-Exercise-0ca1730428424073a7eb868e6135db6c
print("*"*25)
tweet = input("Enter your tweet: ")
max_char = 140
char_count = len(tweet)
if char_count > max_char:
    print(
        f"Your {char_count} character tweet is {len(tweet) - 140} characters too long")
else:
    print(f"That {char_count} character tweet is okay.")
