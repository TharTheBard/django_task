from django.apps import apps


def json_to_models(instances_json):
    for instance_dict in instances_json:
        for model_name in instance_dict:
            model = apps.get_model('api', model_name)
            keywords_to_model_instance(model, instance_dict[model_name])


def keywords_to_model_instance(model, kwargs):
    model(**kwargs).save()
