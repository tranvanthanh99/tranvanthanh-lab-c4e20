from gmail import GMail,Message
from random import randint,choice



html_content = """
<p style="text-align: center;"><strong>cộng h&ograve;a x&atilde; hội chủ nghĩa việt nam</strong></p>
<p style="text-align: center;"><strong>độc lập - tự do - hạnh ph&uacute;c</strong></p>
<p style="text-align: center;">&nbsp;</p>
<h1 style="text-align: center;"><strong>ĐƠN XIN NGHỈ HỌC</strong></h1>
<p>&nbsp;</p>
<p>k&iacute;nh gửi thầy gi&aacute;o, em t&ecirc;n l&agrave; Trần Văn Th&agrave;nhs</p>
<p>h&ocirc;m nay em viết mail n&agrave;y để xin thầy nghỉ học vì {{sickness}} </p>
<p>&nbsp;</p>
<p>em xin cảm ơn&nbsp;</p>
<p>Trần Văn Th&agrave;nh</p>
"""

relist = ["a","b","c","d"]
# new_content = html_content.replace("{{sickness}}",relist[randint(0,len(relist)-1)])
new_content = html_content.replace("{{sickness}}",choice(relist))

gmail = GMail('thanhvantranc4e20@gmail.com','vantran297')
msg = Message('Test Message',to='20130075@student.hust.edu.vn',html=new_content)
gmail.send(msg)