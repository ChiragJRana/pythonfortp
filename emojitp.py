import emoji
name = input('Enter the name of the emoji').split()
emojiname = ':'+'_'.join(name)+':'
print(emoji.emojize(emojiname)) 