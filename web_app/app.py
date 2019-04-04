""" Web application for a calculator  """
from dotenv import load_dotenv
from flask import Flask, render_template, flash, redirect, url_for, session, request
from flask.logging import create_logger
from core.calculator import Calculator
from .settings import SECRET_KEY

load_dotenv()

CALCULATOR = Calculator()

APP = Flask(__name__)
APP.secret_key = SECRET_KEY

LOGGER = create_logger(APP)


@APP.route("/", methods=["GET"])
def index():
    """ Returns the root page showing the user's total  """
    calculator_total = 0
    if "calculator_total" in session:
        calculator_total = session["calculator_total"]
    return render_template("index.html", calculator_total=calculator_total)


@APP.route("/add", methods=["POST"])
def add():
    """ UI showing the result of adding the number_to_add param """

    number_to_add = 0
    if request.form.get("input_number", "") != "":
        number_to_add = request.form["input_number"]

    previous_total = 0
    if "calculator_total" in session:
        previous_total = session["calculator_total"]

    calculator = Calculator(starting_total=previous_total)

    new_total = calculator.add(float(number_to_add))
    session["calculator_total"] = new_total
    LOGGER.info(
        "Added %s to %s resulting in %s", number_to_add, previous_total, new_total
    )
    flash(f"Added {number_to_add}!")
    return redirect(url_for("index"))


@APP.route("/subtract", methods=["POST"])
def subtract():
    """ UI showing the result of subtracting the number_to_subtract param """

    number_to_subtract = 0
    if request.form.get("input_number", "") != "":
        number_to_subtract = request.form["input_number"]

    previous_total = 0
    if "calculator_total" in session:
        previous_total = session["calculator_total"]

    calculator = Calculator(starting_total=previous_total)

    new_total = calculator.subtract(float(number_to_subtract))
    session["calculator_total"] = new_total
    LOGGER.info(
        "Added %s to %s resulting in %s", number_to_subtract, previous_total, new_total
    )
    flash(f"Subtracted {number_to_subtract}!")
    return redirect(url_for("index"))


@APP.route("/clear", methods=["POST"])
def clear():
    """ Resets the calculator's value to 0 """
    session["calculator_total"] = 0
    LOGGER.info("calculator cleared")
    flash("Calculator cleared!")
    return redirect(url_for("index"))
