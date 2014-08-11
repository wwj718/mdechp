#coding:utf-8
from django.db import models
from jsonfield import JSONField


# Create your models here.
from mptt.models import MPTTModel, TreeForeignKey
class MpttMeetInfo(MPTTModel):
    '''
    #每个用户对应一个MpttMeetInfo，作为外键
    #初始化时init出树结构
    #存储的时候每个节点是数据库一条记录，不过他们记得住自己在树中的位置
    '''
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
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

    def InitMpttMeetInfo(self):
        '''赋值给meetInfo'''
        root = MpttMeetInfo.objects.create(title="会议信息")
        baseSetting = MpttMeetInfo.objects.create(title="基本设置", parent=root)
        MpttMeetInfo.objects.create(title="大会征文", parent=root)
        MpttMeetInfo.objects.create(title="风格设置", parent=baseSetting)
        return root

    def save(self, *args, **kwargs):
        self.meetInfo = self.InitMpttMeetInfo()
        super(Owner, self).save(*args, **kwargs)

#初始化会议信息树

######################################################
#test JSONField

class Meet(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    #meetInfo = JSONField(default={"check":0}) #must use "",'' error admin will cause error , because obj -> string , in view ok
    meetInfo = JSONField(default="")
    def InitMeetInfo(self):
        '''
        #初始化会议信息给meetInfo
        #使用json来应对不稳定的数据结构，广告信息可以随着用户的需求随意生成树状结构
        '''
        info = {
            "baseSetting":{"a1":"","a2":""},
            "test1":"",
            "test2":""
            }

        return info

    def save(self, *args, **kwargs):
        self.meetInfo = self.InitMeetInfo()
        super(Meet, self).save(*args, **kwargs)
