# myMongoDB
MongoDB的安装好基本使用
## 环境
1. Python 3.6
2. Django 2.0.7
3. mongoengine 0.15.3
4. Mac

## MongoDB 安装 使用
1. 在本地配置MongoDB
> a. 安装
```
brew install mongodb
```
> b. 添加路径

```
export PATH=/usr/local/Cellar/mongodb/4.0.2/bin/:$PATH
```
>c .创建数据存储库

```
sudo mkdir -p /data/db
```
2. 测试使用
> a.启动 mongodb服务端

```
sudo mongod
```
>b. 启动 mongodb 客户端(另一个窗口)

```
sudo mongo
```
>c. 显示所有数据库
	
```
show dbs
```
>d.创建数据库
		
```
use students
```

>e.插入数据
	
```
db.students.insert({"name":"cox"})
```
## Django 项目
1. 安装mongoengine

```
pip3 install mongoengine
```
2. 在 models.py

```
...
import mongoengine

class User(mongoengine.Document):
    name = mongoengine.StringField()
    age = mongoengine.IntField()
    meta = {"db_alias": "default"}
...
```
3.在 views.py

```
...
from mongoengine import connect
class home(APIView):
    def post(self,request):
        connect('project1')
        connect('project1', host='mongodb://localhost:27017/test_database')
        User.objects.create(name="cox",age=12) #新增数据
        return HttpResponse("mongodb")
...
```
4.其他操作
>a. 查询数据
```
User.objects.filter(name="cox")
```
>b. 删除数据
```
User.objects.filter(name="cox").delete()
```


















