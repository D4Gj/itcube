# -*- coding: utf8 -*-
from os import system
import platform
from textwrap import wrap

if platform.system() == 'Windows':
    clcmd = 'cls'
else:
    clcmd = 'clear'

nextFuncName = 'start'

width = 100

pics = \
['''
         \O/
|         |     |
|_########|___@@|
|               |\n''',
'''
_         0
 |_    __/|\\
   |_     |/
     |_  / \__
       |_\\
         |_\n''',
'''
|
|__\__0__
|     \\  \\
|      \\
|      /\   |
|     / _\_/
| |      |
| |@@__0-^-0____|
| |             |\n''',
'''
      _____
      |   |
      |___|
    \\___|__/
     \\____/
 _____/__\\____
  |         |
  |         |
  |         \\
  |      физика\n''',
'''
    ______
   /      \\
   |      |
 __|______|__
 |          |
 | 0 . 0  0 |
 | ^   ^  ^ |
 |__________|\n''']

def write(sentence):
    print('#-' + '-' * width + '-#')
    for line in wrap(sentence, width):
        print('| {0:^{1}} |'.format(line, width))
    print('#-' + '-' * width + '-#')

def num_input():
    result = -1
    try:
        result = int(input('Введите вариант ответа и нажмите Enter >>> '))
    except Exception:
        print('\nВвод должен быть целым числом без лишних символов.')
        result = num_input()
    return result

def selection(*args):
    lenght = len(args)
    for i in range(lenght):
        print('({}) {}'.format(i + 1, args[i]))
    result = num_input()
    while result < 1 or result > lenght:
        print('Введенное число должно быть в диапазоне от 1 до {}'.format(lenght))
        result = num_input()
    return result

def enter():
    input('- Нажмите Enter, чтобы продолжить -')

class GameData():

    def start(self):
        print(pics[0])
        write('Прекрасный солнечный день! За окном щебечут птицы, куда-то летят пушистые белые облака, а я, Василий Бубочкин, опаздываю в школу.')
        enter()
        system(clcmd)
        write('Подскакиваю с кровати и внезапно вспоминаю, что на урок нужно обязательно принести компас, глобус, гигрометр и астролябию, появление без которых чревато двойкой в дневнике, выговором у директора, вызовом родителей и позорным стоянием в углу класса в назидание остальным ученикам.')
        choice = selection('Бежать за глобусом на чердак.', 'Подумать о бессмысленности всего сущего и остаться в кровати.')
        if choice == 1:
            return 'run_on_attic'
        if choice == 2:
            return 'comes_to_mind'

    def comes_to_mind(self):
        write('(Некстати вспоминается учительница Ираида Захаровна, которая терпеть не может опоздавших и обязательно позвонит родителям в поисках своего ученика)')
        enter()
        return 'run_on_attic'

    def run_on_attic(self):
        print(pics[1])
        write('Я подскакиваю, и, поддергивая спадающие штаны пижамы, бегу к лестнице, ведущей на чердак.')
        enter()
        return 'locked'

    def locked(self):
        print(pics[4])
        write('На чердачной двери висит замок, кодом от которого является число Пи. Но что это за число?')
        choice = selection('3.14', '0.42', '1.25')
        if choice == 1:
            system(clcmd)
            write('Введенный код оказался верным, и замок со скрипом открылся.')
            enter()
        else:
            system(clcmd)
            write('Хмм... Кажется, код оказался неверным. Пришлось идти в мамину комнату и смотреть в записную книжку с паролями.')
            print('Верный ответ: 3.14')
            enter()
        return 'attic'

    def attic(self):
        write('Как же пыльно на чердаке! В пробивающихся сквозь дыры в крыше солнечных лучах танцуют пылинки, падая на старую трухлявую мебель, загадочные ящики, коробки и безногий рояль.')
        choice = selection('Искать глобус', 'Сесть на ступеньки и наблюдать за пылинками')
        if choice == 1:
            return 'search'
        if choice == 2:
            return 'sit_on_the_steps'

    def sit_on_the_steps(self):
        write(' - "Должно быть, здесь водятся летучие мыши..." - подумалось мне. "Как было бы здорово, если бы одна из них меня укусила и я стал бы Бэтменом!" Воодушевленный этой идеей, лезу на чердак.')
        enter()
        return 'search'

    def search(self):
        write('Пробираясь между залежами старого хлама, на меня сверху неожиданно сваливается жирный паук.')
        choice = selection('Завизжать и упасть в обморок', 'Смахнуть паука и продолжить поиски')
        if choice == 1:
            return 'game_over'
        if choice == 2:
            return 'ouch'

    def ouch(self):
        write('"Ай, занозу посадил!" - воскликнул я, доставая из рояля глобус, завернутый в новогоднюю подарочную бумагу. "И как я догадался, что он лежит именно здесь?"')
        selection('Сожалея о том, что так и не стал Бэтменом, спуститься в ванную, чтобы вытащить занозу', 'Размышляя о вариантах разведения на чердаке небольшой стаи летучих мышей, спуститься в ванную, чтобы смыть с себя вековую пыль')
        return 'bathroom'

    def bathroom(self):
        write('Включив свет в ванной, первое, что я увидел - это свое отражение в зеркале. "До чего же я мил и очарователен!" - внезапно озарило меня. "Вот нос у меня прямо как у Люка Скайуокера! А глаза... Глаза такие же красивые, как у Аквамена!! Ну до чего же я хорош!!!"')
        choice = selection('Экспериментировать с прической с помощью маминого геля для волос', 'Прийти в себя и вспомнить, что где-то здесь как раз должен валяться гигрометр, нужный на уроке Ираиде Захаровне')
        if choice == 1:
            return 'experiment'
        if choice == 2:
            return 'find_a_hydrometer'

    def experiment(self):
        write('Включив фен, решаю, что неплохо было бы смыть пыль со своих великолепных волос. Фен случайно выскальзывает из рук, я закономерно получаю удар током и падаю в обморок.')
        enter()
        return 'game_over'

    def find_a_hydrometer(self):
        write('Нашариваю под ванной гигрометр, радуюсь и решаю, что не все еще потеряно! Осталось найти только компас и астролябию! Вспоминаю, что астролябия точно лежала в родительской спальне, мама часто пользовалась ей, чтобы отыскать путь к потерянным папиным носкам.')
        enter()
        system(clcmd)
        write('Размахивая руками, изо всех сил мчусь в спальню, чтобы попутный ветер сдул с меня чердачную пыль.')
        choice = selection('Споткнуться о ковер, приложиться головой о дверь спальни, посмотреть на звездочки в глазах, отключиться', 'Добраться до спальни без обморока')
        if choice == 1:
            return 'game_over'
        if choice == 2:
            return 'bedroom'

    def bedroom(self):
        print(pics[2])
        write('Как же прекрасна жизнь, когда астролябия находится в первом же месте, куда я заглянул! А заглянул я, конечно, в вентиляционное отверстие под потолком, куда же еще? Поставил стул на колесиках на родительскую кровать, для надежности примотав его синей изолентой, забрался на него, открыл решетку воздуховода и...')
        choice = selection('Упасть на пол вместе со стулом, отделаться легким испугом и обмороком', 'Достать астролябию и четыре разных носка из вентиляции, благополучно спуститься вниз')
        if choice == 1:
            return 'game_over'
        if choice == 2:
            return 'compass'

    def compass(self):
        write('Где же компас? Неожиданно я вспоминаю, что компас-то я отдал Витьке из параллельного класса в обмен на замечательный самодельный пистолетик, который стреляет шариками из фольги. И я с упоением стрелял ими в Ираиду Захаровну, пока она мелом на доске рисовала границы Ульяновской области на карте мира. Эх, до чего ж весело было! Всем, кроме Ираиды Захаровны. Ей просто возраст не позволяет правильно воспринимать хорошие шутки.')
        enter()
        system(clcmd)
        write('Без компаса двойка обеспечена. К Витьке идти бесполезно, он его уже, небось, на кусочки разобрал и по карманам распихал... Интересно, а что будет, если взять Витьку за шиворот и встряхнуть хорошенько? Тогда из него, как из копилки посыпятся гвоздики, монетки, камешки и прочая ерундень. В чем причина такого удивительного явления природы?')
        choice = selection('Магнитные бури', 'Сила трения', 'Инерция', 'Аномальные возмущения ближайшей черной дыры')
        system(clcmd)
        if choice == 3:
            write('Ну какой я молодец, какой умница!!! Впору самому себя по голове погладить и пятерку поставить!')
        else:
            write('Эх, плохо меня физике учили в школе... Инерция же!')
            print('Верный ответ: инерция')
        enter()
        system(clcmd)
        write('А делать-то что? Без компаса двойка обеспечена. К Витьке идти бесполезно, он его уже, небось, на кусочки разобрал...')
        choice = selection('Заплакать и самому нарисовать двойку в дневнике, чтобы не терять времени', 'Собраться и пойти в школу без компаса', 'Внезапно вспомнить, что в телепередаче "Делаем адронный коллайдер из подручных материалов" ведущий как-то рассказывал, как сделать компас своими руками, если ты случайно заблудился в глухой тайге.')
        if choice == 3:
            pass
        else:
            system(clcmd)
            write('Это как-то по-девчачьи. Я же не слабак какой-то! Попробую-ка я все-таки собрать компас.')
            enter()
        return 'compass2'

    def compass2(self):
        write('В тщетных попытках я пытаюсь отрыть в глубинах своей памяти рецепт компаса. Какая же из комбинаций верна?')
        choice = selection('Монетка, плоскогубцы, банка от варенья, часовой механизм и наждачная бумага', 'Расческа, меховое покрывало, воздушный шарик и китайские палочки', 'Клочок листа от учебника физики, чашка с недопитым чаем, иголка и магнит')
        if choice != 3:
            system(clcmd)
            write('Что-то не сходится... Подумаю-ка я еще.')
            enter()
            system(clcmd)
            GameData().compass2()
        return 'hall'

    def hall(self):
        write('Это нужно попробовать! И я даже знаю, где взять старый учебник физики - он уже пару месяцев подпирает ножку стола в зале! Пойду-ка я туда.')
        enter()
        system(clcmd)
        print(pics[3])
        write('Вот незадача! Учебник под ножкой стола, а на столе старинный драккар викингов, который папа долгими месяцами складывал из спичек без клея и гвоздей. Подпереть стол домкратом - первая идея разбилась об отсутствие домкрата в пределах видимости. Может, как фокусники в телевизоре - быстро выдернуть учебник из под стола и кораблик останется стоять как стоял? Чем я хуже этих фокусников? Могу даже мантию надеть!')
        selection('Оторвать кусок портьеры, сказать "Сим-сим, откройся!" и выдернуть учебник', 'Отпилить верхушку стола вместе с драккаром и переставить на пол, освободив ножки', 'Смазать учебник машинным маслом и аккуратно вытащить его, положив взамен учебник математики')
        system(clcmd)
        write('"Почему драккары всегда падают перпендикулярно земле?" - грустно размышлял я, собирая обломки папиного творения. "И когда папин ремень будет отскакивать от моей нижней части - это упругость или инерция?"')
        enter()
        system(clcmd)
        write('Этим вопросам суждено было остаться без ответа, а учебник по физике наконец-то был в моих руках!')
        enter()
        system(clcmd)
        write('Ну, дело за малым - пора искать иголку! Точно, она была в шкафчике в коридоре, среди маминых рукодельных принадлежностей.')
        enter()
        return 'hallway'

    def hallway(self):
        write('Давящая тишина царила в полумраке коридора. Мрачные тени прятались в углах, тихонько поскрипывала деревянная вешалка, словно таила в себе нечто таинственное и ужасное... Зловеще нависали надо мной фетровые папины шляпы и казалось, что вот-вот мамино пальто взмахнет драповыми рукавами и плавно поплывет по коридору, шепча "Не трогай мои игооолкиии..."')
        choice = selection('Запаниковать и в ужасе упасть в обморок', 'Вызвать МЧС, полицию, скорую помощь, телевидение и охотников за привидениями', 'Включить свет и облегченно выдохнуть, увидев, что коридор чист, светел и прекрасен')
        if choice != 3:
            system(clcmd)
            write('Да что я, трус какой-то? Я даже папы с ремнем не боюсь, а тут какое-то пальто! Ну-ка, где тут выключатель?')
            enter()
        system(clcmd)
        write('Напевая вполголоса незатейливую арию Брунгильды, лезу в шкаф и достаю мамину шкатулку со всякими рукодельными штучками. Сколько же здесь всего!')
        enter()
        return 'magnet'

    def magnet(self):
        write('Ага, вот и игла загадочно мерцает в глубине среди клубков. Что у нас дальше? Да, магнит! Ну тут все просто, магнитов у нас в доме полно!')
        choice = selection('Оторвать магнитик из Анапы с холодильника', 'Разобрать японские колонки, чтобы достать магнит из динамика', 'Отклеить магниты с водяных счетчиков')
        if choice == 1:
            system(clcmd)
            write('Нет, слишком слабенький.')
            enter()
            return 'magnet'
        if choice == 2:
            return 'game_over2'
        if choice == 3:
            return 'water'

    def game_over2(self):
        write('С интересом развинчиваю технику, краем глаза замечая, что забыл отключить колонку от сети. Бабах!!! Что-то ярко сверкнуло и бумкнуло. Кажется, это конец. Медленно оседаю в обморок.')
        print('Попробуйте снова.')
        enter()
        return 'start'

    def water(self):
        write('Вода должна принадлежать народу! Но работники водоканала тоже хотят кушать и денег, поэтому смело отрываю тяжелый магнит со счетчика в ванной и, довольный собой, продолжаю поиски.')
        enter()
        return 'kitchen'

    def kitchen(self):
        write('Вот я и на кухне. Кухня - это всегда хорошо. Здесь есть еда и чайник. Я люблю еду. Особенно вкусную и когда никто не кричит на весь дом: "Вася, закрой холодильник, это на Новый Год!". Наливаю чашечку ароматного чая, тянусь рукой к печеньке и вспоминаю, что вообще-то я пришел сюда по делу. Итак, делаем компас!')
        choice = selection('Выпить чай, почитывая учебник физики и задумчиво тыкая иглой в магнит', 'Кинуть в чашку с чаем магнит и наблюдать, как игла притягивается к чашке с внешней стороны', 'Оторвать листочек от учебника, положить на него намагниченную иглу и опустить его плавать в чашку')
        if choice != 3:
            system(clcmd)
            write('Упс, кажется, я что-то делаю не так.')
            enter()
            return 'kitchen'
        else:
            system(clcmd)
            write('Ура, у меня получилось! Все предметы в сборе! Теперь с чистой душой и грязными руками можно смело отправляться к Ираиде Захаровне! Уж меньше пятерки она мне никак не поставит за мои-то подвиги!!!')
            enter()
            return 'fortune'

    def fortune(self):
        write('А дальше случилось нечто невероятное! А что именно - решать тебе. И только от твоего выбора сейчас зависит моя судьба. Испытаем удачу?')
        choice = selection('"Кот в мешке"', '"Что в черном ящике?"', '"Сектор "Приз" на барабане!"')
        if choice == 1:
            return 'phone_call'
        if choice == 2:
            return 'game_over3a'
        if choice == 3:
            return 'vitya'

    def vitya(self):
        write('Сложив все нужные предметы в рюкзак и осторожно неся в руках чай с компасом, я радостно помчался в школу. Но открыв входную дверь, в меня врезался какой-то бешеный болид, расплескав весь чай и набив мне большую шишку на лбу. Витька?? Витька, а ты чего тут делаешь-то?')
        enter()
        system(clcmd)
        write('Стремительный вихрь по имени Витька ворвался в дом, радостно вопя: "Ураааа!!! В школу сегодня не идееем!!! На карантин закрыли, представляешь? Вот повезло-то!!!"')
        enter()
        system(clcmd)
        write('Я медленно осел на пол, прямо в лужу разлитого чая. Как не идем? А зачем же я тогда вот это вот всё делал сегодня? А Ираида Захаровна?')
        enter()
        system(clcmd)
        write('"А у Ираиды Захаровны ветрянку нашли! Поэтому и карантин!!! Она вся в зеленке, как инопланетянин с Альфа Центавры!!!" - энергия переполняла Витьку через край и разбрызгивалась по коридору радужными фейерверками. "Я вообще к тебе в гости пришел, чтобы не скучно было!!! Чем займемся? А давай вечный двигатель построим из стиральной машинки??? Или лучше ракету из спичечных головок наделаем и в ванной запустим! Или... Или поиграем в индейцев и соорудим вигвам из стульев и ковра!"')
        enter()
        return 'good_end'

    def good_end(self):
        write('Я смотрел на счастливого друга и одинокая слеза предательски ползла по моей щеке... Мне не было жалко потерянного времени, я не боялся нотаций родителей за испорченные вещи, мне просто было радостно и легко, как бывает легко только в раннем детстве, когда нет еще школы, географии, Ираид Захаровен, а есть только беззаботное и беспечное счастье...')
        enter()
        return 'end'

    def phone_call(self):
        write('Смотрю на часы - ну все, опоздал. Настроение на нуле, палец с занозой пульсирует, пыль попала в нос, и, кажется, вместе с паучком.')
        enter()
        system(clcmd)
        write('Внезапно звонок. О, мама звонит. Небось, Ираида Захаровна уже позвонила ей и нажаловалась, что я в школу не явился. И компас не принес. И про шарики из фольги рассказала, наверное. Сейчас влетит мне!!!')
        choice = selection('Не отвечать на звонок', 'Ответить на звонок')
        if choice == 1:
            return 'uncomfortable'
        if choice == 2:
            return 'sunday'

    def uncomfortable(self):
        write('"Неудобно как-то, мама звонит"')
        choice = selection('Не отвечать на звонок', 'Ответить на звонок')
        if choice == 1:
            return 'uncomfortable2'
        if choice == 2:
            return 'sunday'

    def uncomfortable2(self):
        write('"Да что я, трус, что ли какой? Это ж мама! Ну поругается, покричит... Переживу как-нибудь!"')
        enter()
        return 'sunday'

    def sunday(self):
        write('"Васенька, солнце, ты уже позавтракал?" - радостный голос мамы вводит в легкий ступор. "Дддя....?" - нервно соглашаюсь я. "У тебя все в порядке?" "Нууу..." - вспоминаю разгромленный чердак и изоленту на кровати. "Васенька, ты сегодня рано не вставай. Воскресенье. Да и каникулы. Отдохни как следует, хорошо?"')
        selection('Осознать, что сейчас каникулы и Ираида Захаровна с астролябией приснилась в кошмарном сне', 'Догадаться, что по пути на чердак попал в пространственно-временную дыру и проскочил в другое измерение, где у школьников каникулы', 'Понять, что маму подменили инопланетяне, которые хотят захватить планету')
        return 'final'

    def game_over(self):
        write('(Я очнулся, когда наступили сумерки. Где-то раздавались встревоженные голоса родителей, которые не могли меня найти, а у меня перед глазами стояло суровое лицо Ираиды Захаровны, которая поджав губы произнесла: "Хана тебе, Бубочкин! И двойка в четверти")')
        print('\nПопробуйте снова.')
        enter()
        return 'start'

    def game_over3a(self):
        write('Внезапно я услышал, как входная дверь со скрипом открывается. Чьи-то тяжелые шаги раздаются в полутьме коридора.')
        enter()
        system(clcmd)
        write('Неужели это папа вернулся с работы раньше обычного? Точно! Могучая фигура отца проплыла по коридору в спальню, и оттуда раздался сдавленный стон. Ага. Наверняка это папа обнаружил сломанный стул и кровать в изоленте... Ой, что сейчас будет! "ВАСИЛИЙ!!! ВАСИЛИЙ, ГДЕ ТЫ?" Что-то мне не по себе стало. Коленки предательски задрожали и холодный пот выступил.')
        enter()
        system(clcmd)
        write('"ВАСЯ, МАЛЬЧИК МОЙ, ТЫ В ЗАЛЕ? ВАСЯ?? ЭТО ЧТО ЗА... МОЙ ДРАККАААААР!!!" Последнее, что я увидел, сползая по стенке в обморок - это стремительно приближающаяся к кухне фигура отца, размахивающая чем-то, сильно напоминающим его офицерский ремень...')
        enter()
        return 'game_over3b'

    def game_over3b(self):
        write('Глубокий продолжительный обморок. Очнулся я только к вечеру. На улице уже стемнело, сильно пахло валерианкой и за стеной раздавались голоса родителей, обсуждающих процесс моего воспитания. Ну что ж. День прошел не зря. Жаль, что завтра снова в школу. Что у нас там будет? Алгебра, русский, биология.. Биология. Ох ты! Ведь к завтрашнему уроку на биологию нужно будет обязательно принести золотую рыбку, побеги молодого бамбука, трех самцов богомола и череп птеродактиля!!!')
        print('\n(Продолжение следует)\n')
        enter()
        return 'end'

    def final(self):
        write('*Глубокий и продолжительный обморок.*')
        enter()
        return 'end'

    def end(self):
        system(clcmd)
        write('Конец!')
        enter()
        system(clcmd)
        exit()


while True:
    system(clcmd)
    gamedataObj = GameData()
    current = getattr(gamedataObj, nextFuncName)
    nextFuncName = current()
