# GZHUOJContestTools
GZHUOJ比赛工具集

本工具是基于 https://github.com/KIDx/GzhuOJ 编写的。

`gzhuoj.py` 中提供了一些基本的函数，用来注册账号，修改信息，添加账号到比赛中。

`monitor.py` 是一个用来辅助发放气球的脚本。

---

关于组织学校的比赛，需要做的一些事：

- 收集好比赛选手的信息，至少要包括：学院，班级，学号，姓名，性别
- 注册选手的比赛账号，修改账号的密码，将账号导入到比赛中
- 提前了解好赛场的电脑的情况，确定哪些座位是不可用，如：无法开机，无法联网，软件无法使用。然后用于安排座位。
- 发气球

当然要做的其他事情还有很多，这里只列举这些工具相关的事情

第一个脚本中的代码基本都有注释，按照注释基本就可以调用那些函数进行操作。需要进行的操作有，注册账号，修改账号的个人信息，修改账号的密码（脚本里面提供了一个生成密码的函数，推荐使用这个函数来生成密码，生成的密码在打印之后没有歧义），将账号添加到比赛中。

然后，为每个同学安排座位，再比赛前需要去机房里确定好每个机子的情况，机子是否能开机，是否能联网，软件能否使用。根据这些信息为每个学生安排座位。然后通过安排好的座位就可以打印签到表和密码发放。同时，准备每个每个机房的csv文件，文件要求看第二个脚本。

在机房进行比赛的时候是要断外网的，所以一开始在确定好哪些机子是好的以后，每个机房都要留几台机子备用。并且，还需要留一台机子用于发放气球。这台发放气球的机子需要在断网之前安装好python，并且按照好requests模块。 **注意安装好之后就不要重启电脑的了，会还原** 。当然，可以用自己的电脑来作为发放气球的电脑。

---

一些经验教训：
- 出题出友好点，不要高估
- 题目的数据需要从不同的角度考虑，尽可能考虑每种情况，不要只有随机数据。尽量从不同水平的选手出发思考他们的解题方法来构造数据
- 每个机房留一些位置，机子总是会出现不可预料的问题
- 比赛前要再三确认号名单，**在比赛前一个星期给个共享表格，让比赛选手确认信息并打钩** 。这样可以确定哪些人是报名了不来的
- 比赛过程中不要 rejudge，这个 oj 有 bug，随意 rejudge 可能会引发问题
- 题目的公式最好用 **截图** ，不要直接用 latex