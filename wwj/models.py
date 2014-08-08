#coding:utf-8
from django.db import models

# Create your models here.
from mptt.models import MPTTModel, TreeForeignKey
class MpttMeetInfo(MPTTModel):
    '''
    #每个用户对应一个MpttMeetInfo，作为外键
    #初始化时init出树结构
    #存储的时候每个节点是数据库一条记录，不过他们记得住自己在树中的位置
    '''
    title = models.CharField(max_length=50)
    parent = TreeForeignKey("self", blank=True, null=True, related_name="children")
    class MPTTMeta:
    	#如此以来可排序
        order_insertion_by = ['title']

    def __unicode__(self):
        return self.title

class Owner(models.Model):
	'''
    test ForeignKey
    创建Owner时新建一个MpttMeetInfo,用代码创建好结构，调用创建函数
    '''
	name = models.CharField(max_length=100, verbose_name='姓名')
	meetInfo = models.ForeignKey(MpttMeetInfo,blank=True, null=True, verbose_name=u'会议信息')

	def InitMpttMeetInfo():
	    #赋值给meetInfo
		root = MpttMeetInfo.objects.create(title="会议信息")
		baseSetting = MpttMeetInfo.objects.create(title="基本设置", parent=root)
		MpttMeetInfo.objects.create(name="大会征文", parent=root)
		MpttMeetInfo.objects.create(name="风格设置", parent=baseSetting)
		return root
    
    @classmethod
    def create(cls, name):
    	meetInfo = InitMpttMeetInfo()
        book = cls(name=name,meetInfo = )
        # do something with the book
        return book

#初始化会议信息树

