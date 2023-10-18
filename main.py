import tkinter as tk
from tkinter import messagebox
from tkinter import Scrollbar
from utils import DBLPScraper

class DBLPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DBLP文章列表下载")
        self.root.geometry("400x200")

        self.label = tk.Label(root, text="请输入计算机科学家姓名:")
        self.label.pack()

        self.author_name_entry = tk.Entry(root)
        self.author_name_entry.pack()

        self.search_button = tk.Button(root, text="搜索文章列表", command=self.search_articles)
        self.search_button.pack()

    def search_articles(self):
        author_name = self.author_name_entry.get()
        if not author_name:
            messagebox.showerror("错误", "请输入作者姓名")
            return

        scraper = DBLPScraper()
        articles = scraper.get_author_articles(author_name)

        if articles:
            result_window = tk.Tk()
            result_window.title(f"{author_name} 的文章列表")

            text_widget = tk.Text(result_window, wrap=tk.WORD)
            text_widget.pack(expand=True, fill=tk.BOTH,side=tk.LEFT)

            scrollbar = Scrollbar(result_window, command=text_widget.yview)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            text_widget.config(yscrollcommand=scrollbar.set)

            for i, title in enumerate(articles, 1):
                text_widget.insert(tk.END, f"{i}. {title}\n" )



        else:
            messagebox.showinfo("提示", f"未找到作者 {author_name} 的文章列表")

if __name__ == "__main__":
    root = tk.Tk()
    app = DBLPApp(root)
    root.mainloop()
