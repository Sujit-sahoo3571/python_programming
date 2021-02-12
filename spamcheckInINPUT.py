# spam check 

text = input('Enter a Text \n')

if 'make a lots of money' in text :
    spam = True
elif 'buy now' in text:
    spam = True
elif 'subscribe'in text:
    spam = True
elif 'click this link' in text:
    spam = True
else :
    spam = False
if spam :
    print('This text is spam ')
else:
    print('This text is not spam ')


# Not a good idea of using this kind of loop 
# l = ['make a lots of money','buy now', 'subscribe','click this link']

# # for i in l:
# #     if i in text :
# #         print('spam')
# #     else :
# #         print('Not Spam')