# student pass or fail calculate using if elif else
#  four subjects as input 
sub1 = int(input('Enter mark of subject 1:  '))
sub2 = int(input('Enter mark of subject 2:  '))
sub3 = int(input('Enter mark of subject 3:  '))
sub4 = int(input('Enter mark of subject 4:  '))

sumofall = sub1+sub2+sub3+sub4

if sub1<33 or sub2 <33 or sub3 <33 or sub4 <33:
    print('\nYou are fail ! , any one of the subject score less than 33')
elif sumofall/4 < 45 :
    print('\nYou are failed ! , average is less than 45% ')
else:
    print('Congrats! , You passed the exam !!! ')