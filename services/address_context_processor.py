# from contacts.models import Contacts

# def contacts(request):
#     Contacts.objects.create(
#         city='г.Красноярск', 
#         street='ул. Красноярская',
#         building='22', 
#         opening_hours='09:00', 
#         closing_hours='20:00', 
#         main_number='9999999999', 
#         postcode='666666', 
#         email='CleanAutoKRSK@Mail.ru'
#         )

#     # Нужно изменить так, чтоб оно не вызывалось на каждой странице
#     # проверять, чтоб оно уже было в базе данных

#     return {"contacts": Contacts.objects.get(pk=1)}