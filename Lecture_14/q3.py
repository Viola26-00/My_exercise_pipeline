#!/usr/bin/python3
seqs=['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']

for i in range(0,4):
	for j in range(0,4):
		count=0
		if j>i:
			for site in range(0,9):
				if seqs[i][site]==seqs[j][site]:
					count=count+1
			print("the percentage of seq",i+1,"and","seq", j+1, ":", count/len(seqs[i])*100)
		


#想法上

#想把每條序列存成不同變數來省迴圈：迴圈裡寫 seq_i 或 seq_[i] 都做不到。變數名稱裡的 i 不會被換成數字；seq_[i] 只是存進另一個 list。list 本身用 seqs[0]
#、seqs[1] 取，就已經是「每條各自存好」
#以為一個 i 就能代表一對：一對需要兩個數字，i 是第一條、j 是第二條，再加 site 管位置，共三層
#迴圈順序：位置迴圈要在最裡面，因為要「一對比完所有位置 → 算百分比 → 換下一對」

#count 的位置

#放在所有迴圈外面 → 從不歸零，數字一路累加
#放在 i 那層 → 每換一個 i 才歸零，同一個 i 的不同 j 會累加
#正確：放在 j 那層，也就是每一對開始前歸零

#排除配對的條件

#j!<i → SyntaxError，Python 沒有 !<
#改成 j>i，它本身就同時排除自己（i=j）和往前重複（j<i），不需要再加 i!=j
#把 j>i 寫在最裡面的 if → 只擋住 count+1，print 照樣執行，會印出 16 行
#正確：if j>i 要包住整個 site 迴圈和 print

#print

#放在 i 那層 → 每個 i 印一次，不是每一對
#跟 if j>i 對齊 → 不屬於 if，16 對全部都印
#正確：在 if j>i 裡面、site 迴圈結束之後

#輸出內容

#count/len 是比例，要乘 100 才是百分比
#要印出是哪兩條在比；索引從 0 開始，顯示給人看時要 +1













































 
