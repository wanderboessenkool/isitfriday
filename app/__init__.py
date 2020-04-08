from flask import (
  Blueprint,
  flash,
  Flask,
  g,
  render_template,
  request,
  session
)

import os
import sys
import logging
import datetime

def create_app():
  app=Flask(__name__)
  if "gunicorn" in os.environ.get("SERVER_SOFTWARE", ""):
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
  app.logger.info('Started, waiting for requests')

  @app.route("/")
  def home():
    nights_to_sleep = (11 - datetime.date.today().weekday()) % 7
    override = request.args.get("nts")
    if override:
      nights_to_sleep = int(override) % 7
    return render_template("friday.html", nights_to_sleep=nights_to_sleep)

  return app
