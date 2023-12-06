import anime_app


class TestSettings:
    def test_settings(self):
        assert (
            not anime_app.app.DEBUG
        ), "Проверьте, что DEBUG в настройках Flask выключен"
        assert (
            settings.DATABASES["default"]["ENGINE"] == "django.db.backends.postgresql"
        ), "Проверьте, что используете базу данных postgresql"
