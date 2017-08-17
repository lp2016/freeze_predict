# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 14:31:07 2017

@author: Administrator

����ִ��˳��
1.����ִ��classify������classify����������һ��data_type.txt�ļ���
  data_type.txt����һ�����ݣ���ʾ15_data.csv��ÿһ�����ݵ�����
  һ���������ͣ�1������  2����� 3����������
2.Ȼ��data_type�е���һ�����ݸ��Ƶ�15_data.csv��data_type�����У��Լ���ӵģ�
3.ִ��final_data��������ȡ��������2�����15_data.csv�����ĳһ��data_type ���Բ�Ϊ0�����������ݲ����������ݣ�
  ����һ��������ӵ�sict_data.csv��
"""

#from numpy import *
import csv
import time

normalInfo_path='e:15_normalInfo.csv'
failureInfo_path='e:15_failureInfo.csv'
data_path='e:15_data.csv'

def classify():
  
  start1=[]
  end1=[]
  startTime_normal=[]
  endTime_normal=[]
  
  with open(normalInfo_path,'r') as normal_file:
      reader=csv.reader(normal_file)
      for row in reader:          
          start1.append(row[0]) 
          end1.append(row[1])
      del start1[0]
      del end1[0]  
      for item in start1:
          timearray=time.strptime(item,'%Y/%m/%d %H:%M')
          startTime_normal.append(time.mktime(timearray))
      for item in end1:
          timearray=time.strptime(item,'%Y/%m/%d %H:%M')
          endTime_normal.append(time.mktime(timearray))
  normal_file.close()
  
  start1=[]
  end1=[]
  startTime_failure=[]
  endTime_failure=[]
  with open(failureInfo_path,'r') as failure_file:
      reader=csv.reader(failure_file)
      for row in reader:
          start1.append(row[0]) 
          end1.append(row[1])
      del start1[0]
      del end1[0]  
      for item in start1:
          timearray=time.strptime(item,'%Y/%m/%d %H:%M')
          startTime_failure.append(time.mktime(timearray))
      for item in end1:
          timearray=time.strptime(item,'%Y/%m/%d %H:%M')
          endTime_failure.append(time.mktime(timearray))
  failure_file.close()
  
  data1=[]
  data_type=[]
  with open(data_path,'r') as data_file:
      reader=csv.reader(data_file)
      for row in reader:
          data1.append(row[0]) 
         
      del data1[0] 
      for item in data1:
          flag=0
          timearray=time.strptime(item,'%Y/%m/%d %H:%M')
          timestamp=time.mktime(timearray)
          for i in range(0,len(startTime_normal)):
              if timestamp>=startTime_normal[i] and timestamp<=endTime_normal[i]:
                  data_type.append('+1')
                  flag=1
          for i in range(0,len(startTime_failure)):
              if timestamp>=startTime_failure[i] and timestamp<=endTime_failure[i]:
                  data_type.append('-1')
                  flag=1
          if flag==0:
              data_type.append('0')
              
  data_file.close()
  with open('data_type.txt','a') as f:
      for item in data_type:
          f.write(item)
          f.write('\n')
  f.close()    
  
#��data_type.txt�е������ֶ����Ƶ� 15_data.csv�����һ�� data_type(���ھ��ֹ�����֮����ʱ����ֱ�����ó�����)
#Ȼ���ȡ15_data.csv ������data_type������0����׷�ӵ��µ��ļ�sict_data.csv��
def final_data():
     with open(data_path,'r') as data_file:
      reader=csv.reader(data_file)
      with open('sict_data.csv','a',newline='') as f:
           for row in reader:
              if row[28] !='0' and row[0] !='time':
                  row[0]=time.mktime(time.strptime(row[0],'%Y/%m/%d %H:%M'))
                  writer1=csv.writer(f)
                  writer1.writerow(row)
      f.close()          

    
              
if __name__ =="__main__":
    #classify()
    final_data()