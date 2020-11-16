#
# class Mail:
#         mail_id     :   str
#         sender      :   str
#         receiver    :   str
#         date        :   str
#         subject     :   str
#         msg         :   str
#         have_files  :   bool
#         files       :   list (of filenames)

# API for mail model: - use: --------from .mail import funcNAme

#     def get_new_mail_addr(count = 1)  - get amount of mail addr to create -> returns ARRAY of temp mails

#     def get_mail_list(mail_addr) - get temp mail listen to-> returns mail OBJECT

#     def get_mail_data(mail) - get mail OBJECT -> returns updated mail object with msg and files data

#     def get_mail_files(mail) - get mail OBJECT -> returns ???

#     def send_mail(mail): - get mail OBJECT -> returns status

#     def create_mail_by_params(receiver, subject, msg, files=None, sender = "new" ) - get data to create a mail -> return a mail OBJECT


from .mail_model import get_mail_data, get_mail_files, get_mail_list, get_new_mail_addr,send_mail, create_mail_by_params
