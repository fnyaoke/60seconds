from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import PitchForm,UpdateProfile,ReviewForm
from ..import db,photos
from ..models import User,Pitch,Review
from flask_login import login_required,current_user
import markdown2

#Views
@main.route("/")
def index():
    """
    View root page function that return the index page and its data
    """
    pitches = Pitch.query.all()

    title = "Home - Welcome to my Pitch"
    return render_template('index.html',title=title,pitches=pitches)

@main.route("/post",methods=['GET','POST'])
@login_required
def post():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data
        category= form.category.data
        like=0
        dislike=0

        # Updated pitch instance
        new_pitch = Pitch(pitch_title=title,pitch_body=pitch,category=category,like=like,dislike=dislike,user=current_user)

        # save pitch method
        new_pitch.save_pitch()
        return redirect(url_for('main.post'))

    title="Post your pitch"
    return render_template('post.html',title=title,pitch_form=form)

@main.route('/pitch_review/<int:id>',methods=['GET','POST'])
@login_required
def pitch_review(id):
    pitch=Pitch.query.get_or_404(id)
    comment= Review.query.all()
    form=ReviewForm()

    if request.args.get("like"):
        pitch.like = pitch.like+1

        db.session.add(pitch)
        db.session.commit()

        return redirect("/pitch_review/{pitch_id}".format(pitch_id=pitch.id))

    elif request.args.get("dislike"):
        pitch.dislike=pitch.dislike+1

        db.session.add(pitch)
        db.session.commit()

        return redirect("/pitch_review/{pitch_id}".format(pitch_id=pitch.id))

    if form.validate_on_submit():
        review = form.review.data

        new_review = Review(id=id,review=review,user_id=current_user.id)

        new_review.save_review()
        return redirect(url_for('main.pitch_review',id=id))
    reviews = Review.query.all()
    return render_template('pitch_review.html',comment=comment,pitch=pitch,review_form=form,reviews=reviews)

@main.route('/user/<uname>')
def profile(uname):
    user=User.query.filter_by(username=uname).first()
    pitches = Pitch.query.filter_by(user_id=user.id).all()

    if user is None:
        abort(404)

    return render_template("profile/profile.html",user=user,pitches=pitches)

@main.route('/user/<uname>/update',methods=['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form=form)

@main.route('/user/<uname>/update/pic',methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename= photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()

    return redirect(url_for('main.profile',uname=uname))
