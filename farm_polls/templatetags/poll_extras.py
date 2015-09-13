from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    if dictionary!=None:
        return dictionary.get(key)
    else:
        return None

@register.simple_tag
def poll_data(dictionary, q_id, pr_id, answer_type):
    if dictionary!=None:
        value0 = dictionary.get('%s'%q_id)
    else:
        value0=None

    if value0!=None:
        value1=value0.get('%s'%pr_id)
    else:
        value1=None

    value=''
    # CheckBox and Radio
    if (answer_type==1 or answer_type==2 or answer_type==3) and (value1!=None):
        value='checked'

    return value