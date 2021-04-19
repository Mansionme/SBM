from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentInfo,ClassInfo
import xlrd
from django.core import serializers
from django.http import JsonResponse
import json
from django.views.decorators.http import require_http_methods
# Create your views here.

def QueryInfo(request):
    dict_list = []
    name = request.GET.get('name')
    data={}
    if name:
        query = StudentInfo.objects.filter(name=name)
        data = {}
        dict_list = []
        try:
            if (query):
                for student in query:
                    dict_list.append(student.to_dict())
                data = {
                'msg':'success!',
                'error_num':0,
                'data':dict_list
                }
            else:
                data = {
                'msg':"查找失败，没有这个同学",
                'error_num':2,
                }
        except Exception as e:
            data = {
            'msg':str(e),
            'error_num':1
            }

    else:
        try:
            students = StudentInfo.objects.all()
            for student in students:
                dict_list.append(student.to_dict())
            data = {
                'msg':'success!',
                'error_num':0,
                'data':dict_list
            }
        except Exception as e:
            data['msg'] = str(e)
            data['error_num'] = 1

    return JsonResponse(data)
def ExcelRead(request):
    if request.method == 'POST':
        f = request.FILES['file']
        excel_type = f.name.split('.')[1]
        if excel_type in ['xls','xlsx']:
            wb = xlrd.open_workbook(filename=None,file_contents=f.read())
            ws = wb.sheet_by_index(0)
            total_list = [] #用于存储所有学生的所有数据
            for row in range(1,ws.nrows):
                row_list = ws.row_values(row)
                total_list.append(row_list)
            for x in range(len(total_list)):
                total_list[x][1] = int(total_list[x][1])
                total_list[x][1]= str(total_list[x][1])
            class_list = []   #获得班级 
            new_class_list = []    #对班级进行去重操作
            for x in range(len(total_list)):
                class_list.append(total_list[x][2])
            new_class_list = list(set(class_list))
            for row in ClassInfo.objects.all():
                row.delete()
            for name in new_class_list:
                class_save = ClassInfo(major_name=name)
                class_save.save()
            for row in StudentInfo.objects.all(): #避免表的重复，在每次写入时先删除表
                row.delete()
            response = {}
            try:
                for x in range(len(total_list)):
                    class_id = ClassInfo.objects.filter(major_name=total_list[x][2])
                    student = StudentInfo(
                        name=total_list[x][3],
                        major=class_id[0],
                        student_num=total_list[x][1],
                        the_1st_judge=total_list[x][4],
                        the_2nd_judge=total_list[x][5],
                        the_3rd_judge=total_list[x][6],
                        the_4th_judge=total_list[x][7],
                        the_5th_judge=total_list[x][8],
                        the_6th_judge=total_list[x][9],
                        the_7th_judge=total_list[x][10],
                        the_8th_judge=total_list[x][11]
                        )
                    student.save()
                response['msg'] = 'success'
                response['error_num'] =0

            except Exception as e:
                response['msg'] = str(e)
                response['error_num'] = 1

            return JsonResponse(response)
                
        else:
            return JsonResponse({'msg':"excel格式上传错误","error_num":1})
    else:
        return render(request,'read.html')

def Query_by_Name(request):
    name = request.GET['name']
    query = StudentInfo.objects.filter(name=name)
    data = {}
    dict_list = []
    try:
        if (query):
            for student in query:
                dict_list.append(student.to_dict())
            data = {
                'msg':'success!',
                'error_num':0,
                'data':dict_list
            }
        else:
            data = {
                'msg':"查找失败，没有这个同学",
                'error_num':2,
            }
    except Exception as e:
        data = {
            'msg':str(e),
            'error_num':1
        }
    return JsonResponse(data)
    
def Query_Classes(request):
    data = {}
    try:
        class_name = request.GET.get('class_name')
        major_name = ClassInfo.objects.filter(major_name=class_name)[0]
        dict_list = []
        if (major_name):
            students = StudentInfo.objects.filter(major=major_name)
            for student in students:
                dict_list.append(student.to_dict())
            data = {
                    'msg':'success!',
                    'error_num':0,
                    'data':dict_list
                }
        else:
            data = {
                'msg':'要查找的班级不存在',
                'error_num':2
            }

    except Exception as e:
        data={
            'msg':str(e),
            'error_num':1
        }
    return JsonResponse(data)

def DataTime(request):
    time=StudentInfo.objects.all()[0].created
    data={
        'time':time
    }
    return JsonResponse(data)
        


