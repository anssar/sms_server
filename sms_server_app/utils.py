import requests

def check_phone(phone):
    phone = str(phone)
    if len(phone) != 11:
        return False
    if phone[:2] != '89':
        return False
    try:
        phone = int(phone)
    except:
        return False
    return True
    
def send_xml(url, login, password, sender, phone, text):
    template = '''
    <?xml version="1.0" encoding="utf-8" ?>
    <request>
    <message type="sms">
    <sender>{}</sender>
    <text>{}</text>
    <abonent phone="{}" number_sms="1"/>
    </message>
    <security>
    <login value="{}" />
    <password value="{}" />
    </security>
    </request>
    '''

    headers = {'Content-Type': 'text/xml', 'charset': 'utf-8'}

    requests.post(url, headers=headers, data=template.format(
    sender, text, phone, login, password).encode('utf-8'))

