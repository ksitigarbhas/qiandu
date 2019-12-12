from django.db import models
from user.models import User

# Create your models here.

#小说表
class Fiction(models.Model):
    fiction_img = models.FileField(upload_to='fiction_img/',default='fiction_img/default.jpg')
    ficiton = models.IntegerField(choices=((0,'连载中'),(1,'已完结')),verbose_name='小说状态')
    ficiton_name = models.CharField(max_length=64,verbose_name='小说名字')
    detail = models.TextField(verbose_name='小说简介')
    tuijian = models.IntegerField(verbose_name='推荐数量')
    dashang = models.IntegerField(verbose_name='打赏数量')
    dianji = models.IntegerField(verbose_name='点击数量',default=0)
    char_number = models.DecimalField(max_digits=7,decimal_places=2,verbose_name='字数(w)')
    author = models.ForeignKey(to='Author',db_constraint=False,on_delete=models.DO_NOTHING)  #小说作者
    tag = models.ManyToManyField(to='Fiction_tag')  #小说标签


    class Meta:
        verbose_name_plural='小说表'

    def __str__(self):
        return self.ficiton_name


#作者表
class Author(models.Model):
    author_name = models.CharField(max_length=32,verbose_name='作者')
    author_detail = models.TextField(verbose_name='作者简介')
    author_icon = models.FileField(upload_to='icom/',default='icom/default.jpg')
    author_user = models.ForeignKey(to='User',null=True,db_constraint=False,on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural='作者表'


#小说分类
class Fction_category(models.Model):
    category_name = models.CharField(max_length=64,verbose_name='分类名字')
    class Meta:
        verbose_name_plural='小说分类表'


    def __str__(self):
        return self.category_name



#小说章节表
class Fiction_catelog(models.Model):
    fiction_catelog = models.CharField(max_length=64,verbose_name='小说章节')
    centent = models.TextField(verbose_name='章节内容')
    fction = models.ForeignKey(to='Fiction',null=True,verbose_name='小说外键',on_delete=models.CASCADE)
    category = models.ForeignKey(to='Fction_category',null=True,verbose_name='小说分类',db_constraint=False,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='小说章节表'


#评论点赞表
class comment(models.Model):
    comment_time = models.DateTimeField(auto_now_add=True) #评论时间
    comment_content = models.TextField()  #评论内容
    user = models.ForeignKey(to='User',db_constraint=False,on_delete=models.DO_NOTHING) #评论用户
    fiction = models.ForeignKey(to='Fiction',db_constraint=False,on_delete=models.CASCADE)  #评论的小说
    up_number = models.IntegerField(default=0) #点赞数
    parent = models.ForeignKey(to='comment',db_constraint=False,null=True,on_delete=models.DO_NOTHING) #子评论



#小说标签表
class Fiction_tag(models.Model):
    tag = models.CharField(max_length=32,verbose_name='标签名')

    class Meta:
        verbose_name_plural='小说标签表'

    def __str__(self):
        return self.tag


#小说书架表
class Fiction_list(models.Model):
    fiction = models.ForeignKey(to='Fiction',null=True,db_constraint=Fiction,on_delete=models.DO_NOTHING,verbose_name='小说外键')
    user = models.ForeignKey(to='User',db_constraint=False,on_delete=models.DO_NOTHING,verbose_name='用户外键')







