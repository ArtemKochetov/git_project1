import flask
from flask import jsonify, request

from . import db_session
from .records import Records

blueprint = flask.Blueprint(
    'records_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/records')
def get_news():
    db_sess = db_session.create_session()
    news = db_sess.query(Records).all()
    return jsonify(
        {
            'news':
                [item.to_dict(only=('title', 'about', 'cost', 'user.name'))
                 for item in news]
        }
    )


@blueprint.route('/api/records/<int:news_id>', methods=['GET'])
def get_one_news(news_id):
    db_sess = db_session.create_session()
    news = db_sess.query(Records).get(news_id)
    if not news:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'news': news.to_dict(only=(
                'id', 'title', 'about', 'cost', 'note', 'user.name'))
        }
    )


@blueprint.route('/api/records', methods=['POST'])
def create_news():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['title', 'about', 'cost', 'user_id', 'note']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    record = Records(
        title=request.json['title'],
        about=request.json['about'],
        cost=request.json['cost'],
        user_id=request.json['user_id'],
        note=request.json['note']
    )
    db_sess.add(record)
    db_sess.commit()
    return jsonify({'success': 'OK'})

# Edit it
# @blueprint.route('/api/news/<int:news_id>', methods=['DELETE'])
# def delete_news(news_id):
#     db_sess = db_session.create_session()
#     news = db_sess.query(News).get(news_id)
#     if not news:
#         return jsonify({'error': 'Not found'})
#     db_sess.delete(news)
#     db_sess.commit()
#     return jsonify({'success': 'OK'})