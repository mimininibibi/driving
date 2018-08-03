country = input ('請輸入你的國家:')
age = input('請輸入你的年齡:')
age = int (age)

if country == '台灣':
	if age >= 18 :
	    print ('你可以考駕照了')
	else:
	    print ('No，你還不可以考駕照!!')


if country == '美國':
	if  age >= 16:
	    print ('你可以考駕照了')
	elif age < 16:
	    print ('No，你還不可以考駕照!!')

