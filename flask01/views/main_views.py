from flask import Blueprint

# 특정 /main/ 하위에 있는 함수들을 일괄적으로 관리하기 위한 flask의 기능
                # 코드에서 부르는 상대적 이름, 실제 파일명, url에 매칭되는 경로 
mbp = Blueprint('main', __name__, url_prefix='/')

# localhost:5001/main/
@mbp.route('/')
def hello():
    return f'{__name__} hello'

# flask 에서 값을 주소줄로 입력받아서 사용하는 방법
@mbp.route('/<username>')
def print_string(username):
    return f'{__name__} {username} hello'

# <자료형: 변수명>
# <path:subpath> : /를 포함하여 서브경로 전달
#<float:변수명> : float 전달
# <int ~~
@mbp.route('/<path:subpath>')
def print_path(subpath):
    return f'{__name__} {subpath} hello'

@mbp.route('/상품명/')
@mbp.route('/items')
@mbp.route('/items/<itemname>')
@mbp.route('/items/<itemname>/<quantity>')
def print_item(itemname='기본값', quantity = 0):
    return f'{__name__} ({itemname} : {quantity}) hello'