# -*- coding: utf-8 -*-
from django import forms
# from service.models import Message


class AnswerForm(forms.Form):

    def __init__(self, *args, **kwargs):
        answers = kwargs.pop('answers')
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.fields['answers'] = forms.ModelMultipleChoiceField(queryset=answers, widget=forms.CheckboxSelectMultiple())

    def clean_answers(self):
        answers = self.cleaned_data['answers']

        # print answers.values('is_true')
        # if answers.filter(is_true=False).exists():
        #     raise forms.ValidationError('Invalid Answer')
        return answers


# class MessageForm(forms.ModelForm):
#     class Meta:
#         model = Message
#         fields = ['text']
#         widgets = {
#             'text': forms.Textarea(attrs={'autofocus': True})
#         }