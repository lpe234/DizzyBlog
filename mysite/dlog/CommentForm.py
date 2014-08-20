#coding=utf-8
from django import forms
from models import Comment

# class CommentForm(forms.Form):
#     name = forms.CharField(max_length=20, label=u'昵称', error_messages={'required': '请输入姓名'})
#     address = forms.CharField(max_length=20, label=u'地址', required=False)
#     email = forms.EmailField(label=u'邮件', required=False)
#     context = forms.CharField(label=u'评论', widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'address', 'email', 'context']
        labels = {
            'name': u'昵称',
            'address': u'地址',
            'email': u'邮件',
            'context': u'评论',
        }
        widgets = {
            # 'context': forms.Textarea(attrs={'cols': 80, 'rows': 20})
            'context': forms.Textarea,
            # 'article': forms.HiddenInput,
        }
        # error_messages = {
        #     'name': {
        #         'required': u'请输入姓名'
        #     }
        # }
        # help_texts = {
        #
        # }