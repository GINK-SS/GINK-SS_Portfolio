from flask import Blueprint, g, jsonify
from Model.db_introduce import *

BP = Blueprint('introduce', __name__)

# 자기소개서 반환
@BP.route('/view/gink/ss/introduce')
def showme_sangmin():
    info = db_showme_sangmin(g.db) # 내 자기소개서 내용
    activity = db_showme_activity(g.db) # (임시) 내 활동내역
    price = db_showme_price(g.db) # (임시) 내 수상내역
    
    return jsonify(
        status = "success",
        result1 = info,
        result2 = activity,
        result3 = price
    )