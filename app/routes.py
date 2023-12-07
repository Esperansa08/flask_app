from flask import render_template, flash, redirect, url_for, request, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db, cache
from app.forms import LoginForm, RegistrationForm, AddForm, UpdateForm
from app.models import User, Anime
from random import randrange
import threading
import asyncio
from dotenv import load_dotenv
import os
import requests
# from flask_caching import Cache
# cache = Cache(app)

load_dotenv()

# from celery import Celery
# import schedule


# celery = Celery(__name__)


# @celery.task
# def create_backup():
#     # Ваш код для создания резервной копии
#     schedule.every().day.at("02:00").do(create_backup)


# celery.start()


from typing import Any, Dict, Optional


async def background_task():
    """
    Асинхронный метод.
    Получить рандомный тайтл из базы Кинопоиска
    :return: название - описание
    """
    response = requests.get(
        os.getenv("SERVER_URL"),
        params={"genres.name": "аниме"},
        # headers={'X-API-KEY': os.getenv('TOKEN')})
        headers={"X-API-KEY": "TMTAE1J-SY84Z4S-G26ZA5T-HAT3VD0"},
    )
    name = response.json()["name"]
    description = response.json()["description"]
    return f"{name} - {description}"


def start_task():
    background_thread = threading.Thread(target=background_task)
    background_thread.start()


@app.route("/")
@app.route("/index")
@login_required
async def index():
    kinopoisk = await background_task()
    quantity = Anime.query.count()
    if not quantity:
        return "В базе данных нет аниме."
    offset_value = randrange(quantity)
    anime = Anime.query.offset(offset_value).first()
    context = {
        "anime": anime,
        "kinopoisk": kinopoisk,
    }
    return render_template("index.html", context=context)


@app.route("/add_anime", methods=["GET", "POST"])
@login_required
def add_anime():
    form = AddForm()
    anime = Anime.query.filter_by(title=form.title.data).first()
    if anime is not None:
        flash("Такое аниме уже есть в базе")
    if form.validate_on_submit():
        anime = Anime(title=form.title.data, description=form.description.data)
        db.session.add(anime)
        db.session.commit()
        flash("Запись в базу добавлена!")
        return redirect(url_for("index"))
    return render_template("add_anime.html", form=form)


@app.route("/delete/<int:id>", methods=["GET", "POST"])
@login_required
def delete_anime(id):
    anime = Anime.query.filter_by(id=id).first()
    if anime is None:
        flash("Такого аниме нет в базе")
        return redirect(url_for("index"))
    db.session.delete(anime)
    db.session.commit()
    flash("Запись удалена из базы!")
    return redirect(url_for("anime_list"))


@app.route("/update/<int:id>", methods=["GET", "POST"])
@login_required
def update_anime(id):
    anime = Anime.query.get_or_404(id)
    form = UpdateForm(obj=anime)
    if anime is None:
        flash("Такого аниме нет в базе")
        return redirect(url_for("anime_list"))
    if form.validate_on_submit():
        anime.title = form.title.data
        anime.description = form.description.data
        anime.id = anime.id
        db.session.add(anime)
        db.session.commit()
        flash("Запись изменена в базе!")
        return redirect(url_for("anime_list"))
    return render_template("update_anime.html", form=form)


@app.route("/anime_list", methods=["GET"])
@cache.cached(timeout=60)
@login_required
def anime_list():
    anime = Anime.query.all()
    return render_template("anime_list.html", anime=anime)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("index")
        return redirect(next_page)
    return render_template("login.html", title="Sign In", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now a registered user!")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)


@app.errorhandler(404)
def not_found_error(error):
    return render_template("core/404.html"), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template("core/500.html"), 500


# @app.route('/swagger', methods=['GET'])
# def get_api_spec():
#     swag = swagger(app)
#     swag['info']['version'] = "1.0"
#     swag['info']['title'] = "anime_app"
#     print(swag)
#     swag['info']['paths'] = 'j,jm,hjmcjmcj'
#     return jsonify(swag)
