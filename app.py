from flask import Flask, render_template, Blueprint
import View.introduce as introduce
import View.template as template
from Model.db_init import get_db, close_db

# app 생성
def create_app():
    app = Flask(__name__)
    # 아스키 코드로 출력 안하고 한글 보이게 설정
    app.config.update(
        JSON_AS_ASCII=False
    )

    # REQUEST 오기 직전
    @app.before_request
    def before_request():
        get_db()
    # REQEUST 끝난 직후
    @app.teardown_request
    def teardown_request(exception):
        close_db()

    app.register_blueprint(introduce.BP)
    app.register_blueprint(template.BP)

    return app

# 실행
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)