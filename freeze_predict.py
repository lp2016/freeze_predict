# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 14:31:07 2017

@author: Administrator

程序执行顺序：
1.首先执行classify函数，classify函数将生成一个data_type.txt文件，
  data_type.txt包含一列数据，表示15_data.csv中每一行数据的类型
  一共三个类型，1：正常  2：结冰 3：噪声数据
2.然后将data_type中的这一列数据复制到15_data.csv的data_type属性列（自己添加的）
3.执行final_data函数：读取经过步骤2处理的15_data.csv，如果某一行data_type 属性不为0，即该行数据不是噪声数据，
  则将这一行数据添加到sict_data.csv中
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
  
#将data_type.txt中的数据手动复制到 15_data.csv的最后一列 data_type(现在就手工处理，之后有时间在直接利用程序处理)
#然后读取15_data.csv 将其中data_type不等于0的行追加到新的文件sict_data.csv中
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