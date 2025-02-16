from defaultapp.core.repo.log import get as log_repo_get


def test_log(app_ctx):
    results = log_repo_get(app_ctx)
    assert len(results) == 6
