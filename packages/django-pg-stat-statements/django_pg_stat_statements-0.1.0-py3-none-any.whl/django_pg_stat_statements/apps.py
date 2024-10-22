from django.apps import AppConfig


class PGStatStatementsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_pg_stat_statements'
    verbose_name = "PostgreSQL Stat Statements"
