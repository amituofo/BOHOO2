#! -*- coding:utf-8 -*-

from django import forms
from django.forms import ModelForm

from groups.models import Category, Group, Topic, Reply, TopicImage

CITIES = ((u"北京", u"北京"), (u"天津", u"天津"), (u"河北", u"河北"), (u"山西", u"山西"), (u"内蒙古", u"内蒙古"), (u"辽宁", u"辽宁"),
          (u"吉林", u"吉林"), (u"黑龙江", u"黑龙江"), (u"上海", u"上海"), (u"江苏", u"江苏"), (u"浙江", u"浙江"), (u"安徽", u"安徽"),
          (u"福建", u"福建"), (u"江西", u"江西"), (u"山东", u"山东"), (u"河南", u"河南"), (u"湖北", u"湖北"), (u"湖南", u"湖南"),
          (u"广东", u"广东"), (u"广西", u"广西"), (u"海南", u"海南"), (u"重庆", u"重庆"), (u"四川", u"四川"), (u"贵州", u"贵州"),
          (u"云南", u"云南"), (u"西藏", u"西藏"), (u"陕西", u"陕西"), (u"甘肃", u"甘肃"), (u"青海", u"青海"), (u"宁夏", u"宁夏"),
          (u"新疆", u"新疆"), (u"台湾", u"台湾"), (u"香港", u"香港"), (u"澳门", u"澳门"), (u"海外", u"海外"))


class category(ModelForm):
    """ 分类form @fanlintao
    name    分类名称
    parent  父分类
    """
    name = forms.CharField(label=u'名称', widget=forms.TextInput(attrs={}))
    parent = forms.ModelChoiceField(label=u'父分类', queryset=Category.objects.all(), widget=forms.Select())

    class Meta:
        model = Category

    def __unicode__(self):
        return "分类:%s" % self.name


class group(ModelForm):
    """ 小组form @fanlintao
    name            名称
    description     描述
    category        分类
    group_type      小组类型
    member_join     加入小组的方式
    place   群组地点
    """
    GROUP_TYPE_CHOICES = (('open', u'公开'), )   # ('private', u'秘密')  暂时不启用
    MEMBER_JOIN_CHOICES = (('everyone_can_join', '任何人'),) #('need_check', '需要验证'))

    name = forms.CharField(label=u'名称',
                           widget=forms.TextInput(
                               attrs={'class': 'span10 required', 'placeholder': u'群组的名称'}
                           ))
    #category = forms.ModelChoiceField(label=u'分类', queryset=Category.objects.all(),
    #                                  widget=forms.Select(attrs={'class': 'span4 required'}))  #  分类因为联动,单独处理,view中需要注意
    group_type = forms.ChoiceField(label=u'群组类型', choices=GROUP_TYPE_CHOICES,
                                   widget=forms.Select(attrs={'class': 'span4 required'}), initial='open')
    member_join = forms.ChoiceField(label=u'加入方式', choices=MEMBER_JOIN_CHOICES,
                                    widget=forms.Select(attrs={'class': 'span4 required'}),
                                    initial='everyone_can_join')
    place = forms.CharField(label=u'群组地点',
                            widget=forms.Select(choices=CITIES, attrs={'class': 'span4 required'}))
    description = forms.CharField(label=u'描述',
                                  widget=forms.Textarea(
                                      attrs={'class': 'span10 required', 'placeholder': u'群组作用、功能等简要描述'}
                                  ))

    class Meta:
        model = Group
        fields = ('name', 'group_type', 'member_join', 'place', 'description')

    def __unicode__(self):
        return "小组:%s" % self.name


class topicForm(ModelForm):
    """ 话题form @fanlintao
    name  标题
    content  内容
    group 小组
    """
    TOPIC_TYPE_CHOICES = ((2,'公司杂谈'), (3,'拼车信息'))
    name = forms.CharField(label=u'标题', widget=forms.TextInput(attrs={'class': 'span12 required'}))
    content = forms.CharField(label=u'内容', widget=forms.Textarea(attrs={'class': 'span12 required'}))
    topic_type = forms.ChoiceField(label=u'话题类型', choices=TOPIC_TYPE_CHOICES,
                                   widget=forms.Select(attrs={'class': 'span4 required'}), initial=2)

    def __init__(self, *args, **kwargs):
        super(topicForm, self).__init__(*args, **kwargs)
        self.fields['group'].widget = forms.HiddenInput()

    class Meta:
        model = Topic
        fields = ('name', 'content', 'group')

    def __unicode__(self):
        return "话题:%s" % self.name


class topicImageForm(ModelForm):
    """
    话题图片上传form
    """
    image = forms.ImageField(required=False)

    class Meta:
        model = TopicImage
        fields = ('image',)


class replyForm(ModelForm):
    """
    回复  form @fanlintao
    content 回复内容
    """
    content = forms.CharField(label=u'回复内容', widget=forms.Textarea(attrs={'class': 'span12 reply_content required'}))
    reply_id = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Reply
        fields = ('content',)

    def __unicode__(self):
        return "回复内容:%s" % self.content
