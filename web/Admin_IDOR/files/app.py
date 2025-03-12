from flask import Flask, render_template, request
app = Flask(__name__)

empl_info = [
    {'id': 1, 'img': 'https://infostart.ru/upload/iblock/ce8/ce89b0905991716071e29098b8dd4b3f.jpg', 'name': 'Виталий Бэдкодович', 'desc': 'Разработчик ПО', 'desc2': 'Наш многоуважаемый разработчик. Специализируется на создании сложных систем и решении нестандартных задач.', 'phone': '+79159264325', 'mail': 'vitbadcode'},
    {'id': 2, 'img': 'https://media-1obl-ru.storage.yandexcloud.net/resize_cache/943694/e71ad92e8a086fd0ad26a63a20c0e003/iblock/2f6/2f693dd595914f9535433ceb69c482b6.jpg', 'name': 'Олег Клиентович', 'desc': 'Менеджер', 'desc2': 'Наш менеджер по работе с клиентами. Всегда на связи и готов помочь с любыми вопросами.', 'phone': '+79223044949', 'mail': 'manager'},
    {'id': 3, 'img': 'https://i.postimg.cc/jS0RCCpN/5325668888110821613.jpg', 'name': 'Антон Наумов', 'desc': 'Любит пирожки и сосиску в тесте', 'desc2': 'Уважаемый работник со стажем. Специализируется на разработке более совершенных сортов сосисок в тесте.', 'phone': '+79515379475', 'mail': 'nikitosik'},
    {'id': 4, 'img': 'https://pl99.kg/wp-content/uploads/2015/12/ie9g7yfwuzi6tal168o7f9bb0z87p1g6-1.jpg', 'name': 'Иван Бэкдорович', 'desc': 'NAITCTF{1D0R_1T5_B4D_4ND_C0MM0N}', 'desc2': "NAITCTF{1D0R_1T5_B4D_4ND_C0MM0N} <script>alert('Как ты меня нашел?!?')</script>", 'phone': '+133713371337', 'mail': '<a href="https://t.me/fredr0ck">backdoor'},
    {'id': 5, 'img': 'https://avatars.dzeninfra.ru/get-zen_doc/9367095/pub_641784129ae6211eb80d92c9_6417848968b5dc1e53b0187e/scale_1200', 'name': 'Андрей Претензович', 'desc': 'Тестировщик', 'desc2': 'Наш тестировщик. Отвечает за качество продуктов, находит и устраняет ошибки.', 'phone': '+79923435642', 'mail': 'fixbugs'},
    {'id': 6, 'img': 'https://services.kontur.ru/Files/Modules/Article/30041_big_md_1x.jpg?t=1727821388', 'name': 'Алексей Владыкович', 'desc': 'Наш величайший директор', 'desc2': 'Наш директор. Управляет компанией и вдохновляет команду на новые достижения.', 'phone': '+13054240102', 'mail': 'mrboss'}
]


@app.route('/', methods=['GET'])
def start():
    return render_template('index.html', empl_info=empl_info)

@app.route('/employee', methods=['GET'])
def take_emp():
    id = request.args.get('id')
    pers_info = empl_info[int(id)-1]
    return render_template('employee.html', id=id, pers_info=pers_info)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)  