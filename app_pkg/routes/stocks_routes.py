# web_app/routes/stocks_routes.py

from flask import Blueprint, request, render_template
import yfinance as yf

stocks_routes = Blueprint("stocks_routes", __name__)

@stocks_routes.route("/stocks")
def stocks_form():
    return render_template("stocks_form.html")

@stocks_routes.route("/stocks/results")
def stocks_results():
    symbol = request.args.get("symbol") or "AAPL"
    df = yf.Ticker(symbol).history(period="1d")

    latest_price = round(df["Close"][0], 2)

    return render_template(
        "stocks_results.html",
        symbol=symbol,
        latest_price=latest_price
    )
