from flask import Flask, render_template


class TransactionController:

    # [GET] /components
    def index(self):
        return render_template("components.html", page="Transactions")
    

    # [GET] /components/:slug
    def show(self,slug):
        return render_template("componentDetail.html",slug=slug)
