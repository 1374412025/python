import os
filename = 'student.txt'
def main():
    while True:
        menu()
        choice = int(input('请选择您需要选择的功能:'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice == 0:
                answer = input('您确定退出系统吗?y/n')
                if answer == 'y' or answer == 'Y':
                    print('谢谢您的使用!!')
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                update()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()
def menu():
    print('-------------学生管理系统------------')
    print('\t\t\t1.录入学生信息')
    print('\t\t\t2.查找学生信息')
    print('\t\t\t3.删除学生信息')
    print('\t\t\t4.修改学生信息')
    print('\t\t\t5.排序')
    print('\t\t\t6.统计学生总人数')
    print('\t\t\t7.显示所有学员信息')
    print('\t\t\t0.退出程序')
    print('-----------------------------------')
def insert():
    student_list = []
    while True:
        id = input('请输入ID(如1001):')
        # if len(id) != '4':
        #     print('学员ID不符合规定! 请输入如(1001)!')
        #     break
        if not id:
            break
        name = input('请输入姓名:')
        if not name:
            break
        try:
            english=int(input('请输入英语成绩:'))
            Python=int(input('请输入Python成绩:'))
            Java=int(input('请输入Java成绩:'))
        except:
            print('输入无效,不是整数类型,请重新输入')
            continue
        #讲录入的学生信息保存到字典当中
        student = {'id':id,'name':name,'english':english,'Python':Python,'Java':Java}
        student_list.append(student)
        answer = input('你是否继续添加学生信息?y/n\t')
        if answer =='y':
            continue
        else:
            break
    #调用保存函数save
    save(student_list)
    print('学生信息录入完毕!!!')
def save(lst):
    try:
        stu_txt = open(filename,'a',encoding='utf-8')
    except:
        stu_txt = open(filename,'w',encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()
def search():
    student_query = []
    id = ''
    name = ''
    while True:
        if os.path.exists(filename):
            mode = input('按照ID查找请输入1，按照学生名字查找请输入2：')
            if mode == '1':
                id = input('请输入你需要查找学生的ID：')
            elif mode == '2':
                name = input('请输入你需要查找学生的姓名：')
            else:
                print('您的输入有误，请重新输入')
                search()  # 重新调用
            with open(filename, 'r', encoding='utf-8') as rfile:
                student = rfile.readlines()
                for item in student:
                    d = dict(eval(item))
                    if id != '':
                        if d['id'] == id:
                            student_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)

            # 显示已查询出来的学生结果
            student_show(student_query)
            # 清空这个列表
            student_query.clear()
            answer = input('你是否需要继续查询学生信息？ y/n\n')
            if answer == 'y':
                continue
            else:
                break
        else:
            print('没有保存学生信息')
            return
#显示查询结果
def student_show(lst):
    if len(lst) == 0:
        print('没有找到学员相关信息,无数据显示！！ ')
        return
    #定义标题显示格式
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID','姓名','英语成绩','Python成绩','Java成绩','总成绩'))
    #定义内容的显示格式
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('Python'),
                                 item.get('Java'),
                                 int(item.get('english'))+int(item.get('Python'))+int(item.get('Java'))
                                 ))
def delete():
    while True:
        student_id = input('请输入要删除的学生的ID:')
        if student_id != '':
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8')as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False  #标记是否删除
            if student_old:
                with open(filename,'w',encoding='utf-8')as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))#将字符串转为字典
                        if d['id']!=student_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{student_id}的学生信息已被删除')
                    else:
                        print(f'没有找到ID为{student_id}的学生信息')
            else:
                print('无学生信息')
                break
            show()  #删除之后要重新显示所有的学生信息
            answer = input('是否继续删除?y/n\n')
            if answer == 'y':
                continue
            else:
                break
def update():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8')as rfile:
            student_old = rfile.readlines()
    else:
        return
    student_id = input('请输入要修改的学员ID:')
    with open(filename,'w',encoding='utf-8')as wfile:
        for item in student_old:
            d=dict(eval(item))
            if d['id'] == student_id:
                print('找到学生信息,可以修改他的下那个相关信息了!')
                while True:
                    try:
                        d['name'] = input('请输入姓名:')
                        d['english'] = input('请输入学员英语成绩:')
                        d['Python'] = input('请输入学员Python成绩:')
                        d['Java'] = input('请输入学员Java成绩:')
                    except:
                        print('您的输入有误,请重新输入!!')
                    else:
                        break
                wfile.write(str(d)+'\n')
                print('修改成功')
            else:
                wfile.write(str(d)+'\n')
        answer = input('是否继续修改其他学生信息?y/n\n')
        if answer == 'y':
            update()
def sort():
    show()
    if os.path.exists(filename):
        #R 只读的方式打开这个文件
        with open(filename,'r',encoding='utf-8') as rfile:
            student_list = rfile.readlines()
        student_new = []
        for item in student_list:
            d = dict(eval(item))
            student_new.append(d)
    else:
        return
    acs_or_desc = input('请选择(0-升序,1-降序)')
    if acs_or_desc == '0':
        acs_or_desc_bool = False
    elif acs_or_desc == '1':
        acs_or_desc_bool = True
    else:
        print('您的输入有误，请重新输入：')
        sort()
    mode = input('请选择排序方式(1.按英语成绩排序 2.按Python成绩排序 3.按Java成绩排序 0.按总成绩排序)')
    if mode == '1':
        student_new.sort(key=lambda x : int(x['english']),reverse=acs_or_desc_bool)
    elif mode == '2':
        student_new.sort(key=lambda x : int(x['Python']),reverse=acs_or_desc_bool)
    elif mode == '3':
        student_new.sort(key=lambda x : int(x['Java']),reverse=acs_or_desc_bool)
    elif mode == '0':
        student_new.sort(key=lambda x : int(x['english'])+int(x['Python'])+int(x['Java']),reverse=acs_or_desc_bool)
    else:
        print('您的输入有误,请重新输入:')
        sort()
    student_show(student_new)
def total():
    #判断文件是否存在 如果存在开始统计
    if os.path.exists(filename):
        #R 只读的方式打开这个文件
        with open(filename,'r',encoding='utf-8') as rfile:
            students = rfile.readlines()
            if students:
                print('一共有{}名学生。'.format(len(students)))
            else:
                print('还没有录入学员信息!')
    #文件不存在 输出暂未保存信息
    else:
        print('暂未保存数据信息..')
def show():
    student_list = []
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students = rfile.readlines()
        for item in students:
            #把拿到的信息转换为字典类型转换到列表内
            student_list.append(eval(item))
            #如果这个列表不为空 他的布尔值为true
        if student_list:
            #调用显示函数 传入需要显示的对应数据
            student_show(student_list)
    else:
        print('暂未保存数据信息..')
if __name__ == '__main__':
   main()