from expense_tracker.commands import add, total
from tests.conftest import args, make_store


def _seed(store):
    add.handle(args(amount="12.50", category="groceries", date="2026-01-15", note=""), store)
    add.handle(args(amount="40.00", category="transport", date="2026-01-16", note=""), store)
    add.handle(args(amount="10.00", category="food", date="2026-01-17", note=""), store)


def test_total_all(tmp_path, capsys):
    store = make_store(tmp_path)
    _seed(store)
    capsys.readouterr()  # discard output from seeding
    code = total.handle(args(category=None), store)
    assert code == 0
    assert capsys.readouterr().out == "$62.50\n"


def test_total_filtered_by_category(tmp_path, capsys):
    store = make_store(tmp_path)
    _seed(store)
    capsys.readouterr()  # discard output from seeding
    code = total.handle(args(category="groceries"), store)
    assert code == 0
    assert capsys.readouterr().out == "$12.50\n"


def test_total_empty(tmp_path, capsys):
    store = make_store(tmp_path)
    code = total.handle(args(category=None), store)
    assert code == 0
    assert capsys.readouterr().out == "$0.00\n"


def test_total_category_with_no_matches(tmp_path, capsys):
    store = make_store(tmp_path)
    _seed(store)
    capsys.readouterr()  # discard output from seeding
    code = total.handle(args(category="rent"), store)
    assert code == 0
    assert capsys.readouterr().out == "$0.00\n"
