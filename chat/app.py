from flask import Flask,render_template,url_for,request,jsonify
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from .config import configs
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from datetime import datetime
app=Flask(__name__)
app.config.from_object(configs['development'])
db=SQLAlchemy(app)
admin=Admin(app)
socketio=SocketIO(app)


class Lessons(db.Model):
    id=db.Column(db.Integer,primary_key=True,index=True)
    lesson=db.Column(db.String(100),nullable=False)
    date=db.Column(db.String(10),index=True,nullable=False)
    def __repr__(self):
        return f"lesson:{self.lesson},date:{self.date}"
    def to_json(self):
        json_lessons={
                'lesson':self.lesson,
                'date':self.date
                }
        return json_lessons
admin.add_view(ModelView(Lessons,db.session))

@app.route('/',methods=['GET','POST'])
def home():    
    return render_template('index.html')

def get_time():
    date=datetime.now()
    yr,mnth,day=date.year,date.month,date.day
    date=f"{day}/{mnth}/{yr}"
    return date
@socketio.on('request')
def handle_custom_event(data,methods=['GET','POST']):
    if data.get('data')=='query_lessons':
        lessons=Lessons.query.all()
        msg={"lessons":[lesson.to_json() for lesson in lessons]}
        print('data:',msg)
        socketio.emit('receive',msg)
    elif data.get('lesson') is not None:
        pydate=(get_time())
        data['date']=pydate
        socketio.emit('receive',data)
        print('new lesson',data)
        success(data)
def success(data):
    lesson=Lessons(date=data.get('date'),lesson=data.get('lesson'))
    db.session.add(lesson)
    db.session.commit()
    
if __name__=='__main__':
    socketio.run(app)
    

