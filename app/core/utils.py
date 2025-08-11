from django import utils


def get_basic_filters(params, id_field='id', name_field='name'):
    filters = {}
    obj_id = params.get(id_field)
    obj_name = params.get(name_field)

    if obj_id:
        filters['id'] = obj_id
    elif obj_name:
        filters['name__iexact'] = obj_name

    return filters


def get_product_filters(params):
    filters = {}
    category = params.get('category')
    category_id = params.get('category_id')
    room = params.get('room')
    room_id = params.get('room_id')

    if category_id:
        filters['category__id'] = category_id
    elif category:
        filters['category__name__iexact'] = category

    if room_id:
        filters['room__id'] = room_id
    elif room:
        filters['room__name__iexact'] = room

    return filters