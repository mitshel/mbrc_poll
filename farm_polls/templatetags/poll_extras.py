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
        if answer_type!=1:
            value1=value0.get('%s'%pr_id)
        else:
            # для radiubutton номер препарата в имени не отражаются так как все кнопки имеют одно и тоже имя qXpr0
            value1=value0.get('0')
    else:
        value1=None

    value=''
    # Radio
    if (answer_type==1) and (value1=='%s'%pr_id):
        value='checked'
    # CheckBox
    if (answer_type==2 or answer_type==3) and (value1!=None):
        value='checked'
    # Number
    if (answer_type==4) and (value1!=None):
        value='value=%s'%value1
    # Text
    if (answer_type==5) and (value1!=None):
        value='value="%s"'%value1
    # Select
    if (answer_type==6) and (value1!=None):
        value=value1
    return value

@register.simple_tag
def poll_data_selected(dictionary, q_id, pr_id, item_name):
    value=''
    if poll_data(dictionary, q_id, pr_id,6)==item_name:
        value='selected'
    return value
