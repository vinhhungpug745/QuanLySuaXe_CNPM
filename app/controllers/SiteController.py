from flask import Flask, render_template


class SiteController:

    # [GET] /components
    def index(self):
        return render_template("index.html" ,page="Trang chủ")
    
