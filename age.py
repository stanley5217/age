driving = input('請問你有沒有開過車?')
if driving != '有' and driving != '沒有':
	print('只能輸入有/沒有')
	raise SystemExit

age = input('請問你的年齡?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你是合法的')
	else:
		print('你違法了')
elif driving == '沒有':
	if age >= 18:
		print('可以考駕照了了喔')
	else:
		print('再等等喔')