from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField,SelectField
from wtforms.validators import DataRequired

class CommentsForms(FlaskForm):
    comment= TextAreaField('Comment',validators=DataRequired())
    vote=RadioField('default arguments',choices=[('1','UpVote'),('1''DownVote')])
    submit=SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us more about you',validators=DataRequired())
    submit = SubmitField('Submit')

class AddPitch(FlaskForm):
    title = TextAreaField('Your pitch title')
    category_id = SelectField('Select category',choices=[('1','Interview'),('1','Interview'),('1','dating'),('1','Product'),('1','Pick Up lines')])
    content = TextAreaField('Your pitch')
    submit =SubmitField('Create your pitch')
class UpvoteForm(FlaskForm):
    '''
    Class to create a wtf form for upvoting a pitch
    '''
    submit = SubmitField('Upvote')
class DownForm(FlaskForm):
    '''
    Class to create a wtf form for downvoting a pitch
    '''
    submit = SubmitField('Downvote')