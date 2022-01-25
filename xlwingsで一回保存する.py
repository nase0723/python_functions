import xlwings as xw

book_name = "save_once_file"

# ブックを開いて保存しないと値が挿入されないので一度xlwingsで開いて保存する
class Save_once:
    def __init__(self, book_name):
        wb = xw.Book(book_name)
        app= xw.apps.active
        wb.save()
        app.quit()
        
Save_once(book_name)