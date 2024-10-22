def condition_by_between(filters: list, model, column, start_value, end_value):
    _filter = None
    if start_value is not None and end_value is not None:
        _filter = getattr(model, column).between(start_value, end_value)
        filters.append(_filter)
    return _filter


def condition_by_in(filters: list, model, column, value):
    _filter = None
    if value and isinstance(value, list):
        value = [_ for _ in value if _ is not None]
        _filter = getattr(model, column).in_(value)
        filters.append(_filter)
    return _filter


def condition_by_like(filters: list, model, column, value, position: str = "LR"):
    _filter = None
    if value is not None and value != "":
        if position == "LR":
            value = f"%{value}%"
        elif position == "L":
            value = f"%{value}"
        elif position == "R":
            value = f"{value}%"
        else:
            value = f"%{value}%"
        _filter = getattr(model, column).like(value)
        filters.append(_filter)
    return _filter


def condition_by_regex(filters: list, model, column, value):
    _filter = None
    if value:
        _filter = getattr(model, column).like(value)
        filters.append(_filter)
    return _filter


def condition_by_not_in(filters: list, model, column, value):
    _filter = None
    if value is not None:
        _filter = getattr(model, column).notin_(value)
        filters.append(_filter)
    return _filter


def condition_by_not_like(filters: list, model, column, value):
    _filter = None
    if value:
        _filter = getattr(model, column).notlike(value)
        filters.append(_filter)
    return _filter


def condition_by_is_null(filters: list, model, column):
    _filter = getattr(model, column).is_(None)
    filters.append(_filter)
    return _filter


def condition_by_not_null(filters: list, model, column):
    _filter = getattr(model, column).isnot(None)
    filters.append(_filter)
    return _filter


def condition_by_not_in_list(filters: list, model, column, value):
    _filter = None
    if value is not None:
        _filter = ~getattr(model, column).in_(value)
        filters.append(_filter)
    return _filter


def condition_by_eq(filters: list, model, column, value):
    _filter = None
    if value is not None:
        _filter = getattr(model, column) == value
        filters.append(_filter)
    return _filter


def condition_by_not_eq(filters: list, model, column, value):
    _filter = None
    if value is not None:
        _filter = getattr(model, column) != value
        filters.append(_filter)
    return _filter


def condition_by_gt(filters: list, model, column, value):
    _filter = None
    if value is not None:
        _filter = getattr(model, column) > value
        filters.append(_filter)
    return _filter


def condition_by_gte(filters: list, model, column, value):
    _filter = None
    if value is not None:
        _filter = getattr(model, column) >= value
        filters.append(_filter)
    return _filter


def condition_by_lt(filters: list, model, column, value):
    _filter = None
    if value is not None:
        _filter = getattr(model, column) < value
        filters.append(_filter)
    return _filter


def condition_by_lte(filters: list, model, column, value):
    _filter = None
    if value is not None:
        _filter = getattr(model, column) <= value
        filters.append(_filter)
    return _filter


def condition_by_relation(filters: list, model, _column, _relation, _value, _end_value=None, _position="LR"):
    if _relation == "in":
        condition_by_in(filters, model, _column, _value)
    elif _relation == "like":
        condition_by_like(filters, model, _column, _value, _position)
    elif _relation == "regex" or _relation == "re":
        condition_by_regex(filters, model, _column, _value)
    elif _relation == "between":
        condition_by_between(filters, model, _column, _value, _end_value)
    elif _relation == "not in" or _relation == "ni":
        condition_by_not_in(filters, model, _column, _value)
    elif _relation == "not like" or _relation == "nl":
        condition_by_not_like(filters, model, _column, _value)
    elif _relation == "is null" or _relation == "is empty" or _relation == "inl":
        condition_by_is_null(filters, model, _column)
    elif _relation == "not null" or _relation == "nn":
        condition_by_not_null(filters, model, _column)
    elif _relation == "not in list" or _relation == "nil":
        condition_by_not_in_list(filters, model, _column, _value)
    elif _relation == "eq" or _relation == "=":
        condition_by_eq(filters, model, _column, _value)
    elif _relation == "not eq" or _relation == "!=":
        condition_by_not_eq(filters, model, _column, _value)
    elif _relation == "gt" or _relation == ">":
        condition_by_gt(filters, model, _column, _value)
    elif _relation == "gte" or _relation == ">=":
        condition_by_gte(filters, model, _column, _value)
    elif _relation == "lt" or _relation == "<":
        condition_by_lt(filters, model, _column, _value)
    elif _relation == "lte" or _relation == ">=":
        condition_by_lte(filters, model, _column, _value)


def query_with_order_by(query, order_by_list: list = None):
    """
    :param query:
    :param order_by_list: [{"column":User.id,"order":"desc"}]
    :return:
    """
    if order_by_list is not None:
        for order in order_by_list:
            column = order.get("column")
            if column:
                if order.get("order") == "desc":
                    query = query.order_by(column.desc())
                else:
                    query = query.order_by(column.asc())
    return query


def single_model_format_order(model, sort_list):
    """
    :param model:
    :param sort_list: [{"column":"id","order":"desc"}]
    :return:
    """
    new_sort_list = []
    if sort_list is not None:
        for order in sort_list:
            column = order.get("column")
            if column:
                if hasattr(model, column):
                    column = getattr(model, column)
                    if order.get("order") == "desc":
                        column = column.desc()
                    else:
                        column = column.asc()
                    new_sort_list.append(column)
    return new_sort_list
