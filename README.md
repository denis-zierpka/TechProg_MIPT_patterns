# Битва стратегий

В данной версии игры сражаются два игрока, которые в самом начале игры выбирают себе команду из 3-х персонажей (можно с повторениями).
На выбор доступны Archer, Infantryman, Horseman и Swordsman. После выбора персонажей каждым игроком, начинается само сражение.

В сражении игроки ходят по очереди, каждый из них делает следующее:
1) Выбирает своего персонажа, которым он бы хотел ходить
2) Выбирает персонажа, который будет атакован у противника

После этого происходит сам процесс атаки (у персонажа противника снимаются жизни в размере параметра силы атакующего)


Для запуска игры необходимо ввести команду:

1) python main.py      
или       
python3 main.py



## Описание архитектуры


1) В рамках предложенной игры было принято решение использовать такой порождающий паттерн проектирования, как "Фабричный метод".

Этот паттерн позволяет определить общий интерфейс создания объектов в классе, позволяя изменить поведение в подклассе.
В нашем случае общим интерфейсом служит класс WarriorFactory, а в наследуемых от него фабриках ArcherFactory, InfantrymanFactory, HorsemanFactory, SwordsmanFactory 
для созданию объектов типа Archer, Infantryman, Horseman, Swordsman переопределяются методы create_warrior, позволяющие создавать объекты нужных нам типов.

Такой паттерн избавляет класс от привязки к конкретным классам объектов, а также упрощает добавление новых.


2) Во второй части проекта было реализовано взаимодействие с пользователем через графический интерфейс, то есть пользователь выбирает объекты (наполнение игрового мира объектами).

Для удобного взаимодействия реализован мост GameGraphics, который позволяет отрисовывать окно для пользователя и позволяет получать данные его выбора, не вдаваясь в реализацию этого класса.

3) В третьей части проекта был реализован процесс атаки (выбор игроком своего персонажа и персонажа противника)

### Анализ поведенческих паттернов

1. Command - это поведенческий паттерн проектирования, который превращает запросы в объекты, позволяя передавать их как аргументы при вызове методов.
Этот паттерн рекомендуется к использованию в случае, когда в пользовательском интерфейсе есть несколько объектов, желающих обратиться к одинаковой команде бизнес-логики.
   
Такой паттерн мог бы быть использован в случае, если бы кнопки создания команды для игрока напрямую вызывали бы методы добавления/создания Warrior в бизнес-логике. Однако
в нашем случае, мы позволяем игроку сначала выбрать себе команду (он может добавлять себе персонажей нажимая на +, а удалять используя -). Иначе говоря, генерируется список необходимых к созданию
объектов, который далее одной единственной операцией посылает данный в класс бизнес-логики. Такое решение было принято не случайно, поскольку мы хотим дать игроку возможность убирать людей из своей команды,
не связывая сильно между собой интерфейс и бизнес-логику.


2. CoR (Chain of Responsibility) - это поведенческий паттерн проектирования, который позволяет передавать запросы последовательно по цепочке обработчиков. 
   Каждый последующий обработчик решает, может ли он обработать запрос сам и стоит ли передавать запрос дальше по цепи. Этот паттерн рекомендуется к использованию в случае, если для проверки некоторого запроса 
   необходимы этапы проверки, это может быть полезно тогда, когда не имеет смысл проверять следующий этап, пока не пройден предыдущий.
   
Такой паттерн не может быть использован в нашем проекте, поскольку у нас нет глобальных классов проверки, которые мы могли бы упорядочить в цепочку обязанностей. У нас есть проверки, например, на кол-во выбранных 
персонажей, а далее корректность выбора соперников в двух командах, однако это одиночные проверки, не требующие нескольких уровней.


3. Visitor - это поведенческий паттерн проектирования, который позволяет добавлять в программу новые операции, не изменяя классы объектов, над которыми эти операции могут выполняться. Этот паттерн рекомендуется к использованию
тогда, когда мы хотим иметь возможность пользоваться разной логикой, разными методами при работе с отличающимися объектами.
   
Такой паттерн мог бы быть использован в случае, если бы в зависимости от Warrior, происходили разные действие, однако атака производится одинаковым и объективным методом (у атакуемого вычитается из здоровья значение, 
равное силе атакующего). При такой реализации суть игры заключается в правильном выборе в свою команду персонажей, игрок может использовать разные стратегии в игре, но зависит это исключительно от него, а не от
нашей реализации дополнительных бонусов и действий в зависимости от персонажа.


4. Observer - это поведенческий паттерн проектирования, который создаёт механизм подписки, позволяющий одним объектам следить и реагировать на события, происходящие в других объектах.
Этот паттерн рекомендуется к использованию в случае, если бы мы хотим в одном объекте уметь реагировать на изменение в другом (можно сказать, желаем оформить подписку).
   
Такой паттерн не может быть использован, поскольку никакие изменения в нашем проекте не требуют автоматического изменения или запуска действий у других классов. Можно было бы реагировать например, на 
уменьшение жизней персонажа до 0 (прекращения его работы), однако это не имеет никакого смыла, поскольку у каждого персонажа есть параметр его существования, так что удалять его из списка объектов
не требуется, а производить какие-либо действия с неработающим персонажем смысла нет. Тем более, что в случае удаления персонажа, в конце игры не останется информации о том, какие игроки были у противника, а 
также кто из них выжил, а кто нет.






   



### Участники проекта:
- Цирпка Денис Б05-023, 1 курс
- Мастинен Никита Б05-023, 1 курс
