
#  param= num of mail adresses will get
TEMP_MAIL_URL_GET_ADDRESSES = "https://www.1secmail.com/api/v1/?action=genRandomMailbox&count={}"

#params: username and domail name of mail address
TEMP_MAIL_URL_GET_MAILS_LIST = "https://www.1secmail.com/api/v1/?action=getMessages&login={}&domain={}"

#params: username , domain name of mail address and mail id
TEMP_MAIL_URL_GET_MAIL_DATA = "https://www.1secmail.com/api/v1/?action=readMessage&login={}&domain={}&id={}"

#params: username , domain name of mail address ,  mail id and file name
TEMP_MAIL_URL_GET_MAIL_FILE = "https://www.1secmail.com/api/v1/?action=readMessage&login={}&domain={}&id={}&file={}"
