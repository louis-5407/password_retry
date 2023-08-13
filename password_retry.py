i = 0
while i <= 3:
	pa_wo = input("請輸入密碼")
	if pa_wo == "a123456":
		print("登入成功")
		break
	else:
		i = i + 1
		l = 4 - i
		if l != 0:
			print("錯了，還有",l,"次")



