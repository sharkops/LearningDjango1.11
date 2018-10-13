from django.core.mail import send_mail


def generate_random_code(length=8):
    """
    生成给定长度的随机字符串
    :return:
    """
    import random
    s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.sample(s, length))


def send_to_register_email(email, to_emails, send_type='register'):
    """
    用于给指定的邮箱地址发送链接
    :param email: 发件人邮箱地址
    :param to_emails: 收件箱地址，必须是列表或者元祖
    :param send_type: 类型 注册或者找回密码
    :return:
    """
    if send_type == 'register':
        email_title = "鲨鱼在线学习平台激活链接"
        email_body = "请点击此链接地址激活账号: http://www.sharkyun.com/active/{}/"
        email_body = email_body.format(generate_random_code(16))
    elif send_type == 'r':
        email_title = "鲨鱼在线学习平台找回密码"
        email_body = "请点击此链接地址: http://www.sharkyun.com/active/{}/"
        email_body = email_body.format(generate_random_code(16))

    else:
        email_title, email_body = '', ''

    send_mail(
        subject=email_title,
        message=email_body,
        from_email=email,
        recipient_list=to_emails
    )

send_to_register_email()