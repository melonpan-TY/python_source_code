#python ver.3.8.0
#pip ver 20.3.3

#シート名の変更
import openpyxl #openpyxlをインポートする
wb = openpyxl.load_workbook("test.xlsx") #作業フォルダからエクセルファイルを指定
ws = wb.worksheets[0] #シートインデックス0（シート番号は０始まり）
ws.title = "Sheetone" #シート1を"(任意の名前)"に変更する
wb.save("test.xlsx") #セーブする
wb.close() #ファイル閉じる
print(wb.sheetnames) #Shellにシート名を表示する
