from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from flask_login import login_required
from ..models import User,Pitch
from .forms import UpdateProfile,AddPitch
from .. import db,photos

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Pitch Deck'

    return render_template('index.html', title = title)

@main.route('/interview/pitches/')
def interview():
    '''
    View root page function that returns the index page and its data
    '''
    pitches= Pitch.get_all_pitches()
    title = 'Home - Welcome to The best Pitching Website Online'
    return render_template('interview.html', title = title, pitches= pitches )

@main.route('/pick_up_lines/pitches/')
def pick_up_line():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Pick Up Lines'

    pitches= Pitch.get_all_pitches()

    return render_template('pickup.html', title = title, pitches= pitches )

@main.route('/dating/pitches/')
def dating():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'dating Pitches'

    pitches= Pitch.get_all_pitches()

    return render_template('dating.html', title = title, pitches= pitches )


@main.route('/product/pitches/')
def product():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Product Pitches'
    pitches= Pitch.get_all_pitches()
    return render_template('product.html', title = title, pitches= pitches )
@main.route('/loggedin')
def loggedin():

    title='Pitch Deck'

    return render_template('login.html',title=title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile.html",user=user)

@main.route('/user/<uname>/update',methods =['GET','POST'])
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data

        # db.session.add(user)
        # db.session.commit()

        return redirect(url_for('.profile',uname=user.username))
    title = 'Update || Profile'
    return render_template('update_profile.html',form=form,title=title)

@main.route('/user/<uname>/update/pic',methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        # db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/user/<pitchname>/pitch',methods= ['GET','POST'])
@login_required
def addpitch(pitchname):

    form = AddPitch()

    if form.validate_on_submit():
        pitch = Pitch(content=form.content.data,name=form.title.data)
        # db.session.add(pitch)
        # db.session.commit()

        flash('THe pitch has been posted')
        return redirect(url_for('main.addapitch',pitchname=pitch.name))

    title = 'add a new pitch'
    return render_template('new_pitch.html',form=form,title=title)

@main.route('/all_pitches')
def all_pitches():

    return render_template('all-pitches.html')
