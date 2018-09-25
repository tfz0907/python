import uuid
from flask import render_template
from flask_mail import Message
from flask_restful import Resource,fields,marshal_with,reqparse
from App.exts import db,mail,cache
from App.models import UserModel
from werkzeug.security import generate_password_hash

#参数解析
parser=reqparse.RequestParser()
parser.add_argument('username',type=str,required=True,help='必须填写用户名')
parser.add_argument('password',type=str,required=True,help='必须填写密码')
parser.add_argument('email',type=str,required=True,help='必须填写邮箱')


#
user_fields={
    'u_name':fields.String(attribute='name'),
    'u_email':fields.String(attribute='email')

}

#

result_fields = {
    'returnCode': fields.String,
    'msg': fields.String,
    'returnValue': fields.Nested(user_fields)
}

class UserRegisterResource(Resource):
    @marshal_with(result_fields)
    def post(self):
        #注册

        #获取客户端提交过来的东西
        parse=parser.parse_args()
        username=parse.get('username')
        password=parse.get('password')
        email=parse.get('email')

        user=UserModel()

        user.name=username
        user.passwd=generate_password_hash(password)
        user.email=email
        #注册时设置token的值(唯一标识一个用户)
        user.token=str(uuid.uuid4())

        try:
            db.session.add(user)
            db.session.commit()
            #临时存储5分钟,在5分钟之内激活有效(临时存储user.token,user.id)
            cache.set(user.token,user.id,timeout=300)

            #给指定的邮箱发送邮件
            msg=Message(subject='用户激活',sender='tfzv58@163.com',recipients=[email])
            #邮箱内容
            msg.html=render_template('email_active.html', username=username, active_url='http://127.0.0.1:5000/urr/?u_token=%s' % user.token)
            #发送
            mail.send(msg)

        except Exception as e:
            return {'returnCode':'-1','msg':e}

        return {'returnCode':'0','msg':'success','returnValue':user}
