import pytest

from django.urls import reverse

from .models import QueryStatistic
from .utils import get_current_database_id


def test_query_statistic_model(db):
    # Test fetching QueryStatistic objects from pg_stat_statements database.
    assert QueryStatistic.objects.first() is not None

    # Count will be increased since statistics of the query that
    # calculates the count will be added to the pg_stat_statements.
    query_statistic_count = QueryStatistic.objects.count()
    assert QueryStatistic.objects.count() == (query_statistic_count + 1)


def test_get_current_database_id(db):
    database_id = get_current_database_id()
    assert QueryStatistic.objects.filter(query="SELECT current_database()", dbid=database_id).exists()


def test_get_admin_app_index_view(admin_client):
    response = admin_client.get(reverse("admin:app_list", kwargs={"app_label": "django_pg_stat_statements"}))
    assert response.status_code == 200


def test_get_admin_app_querystatistic_changelist_view(admin_client):
    response = admin_client.get(reverse("admin:django_pg_stat_statements_querystatistic_changelist"))
    assert response.status_code == 200
