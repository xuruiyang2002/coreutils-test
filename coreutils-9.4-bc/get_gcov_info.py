import json
import sys
import os
import math

# note : usage is : python3 'dirver_name' 'getFile/getCov'
argvs = sys.argv[1:]
opt = argvs[0]

#######################

gcov_path = opt
#print("python script: gcov_path = ", gcov_path)
gcov_dir = os.path.split(gcov_path)[0]
#print("python script: gcov_dir = ", gcov_dir)
all_coverage_path = gcov_dir + "/temp.out"
#print("python script: all_coverage_path = ", all_coverage_path)
all_line_count = 0

with open(str(all_coverage_path),'r') as f:
  line = f.readline()
  tokens = line.split(' ')
  for idx in range(len(tokens)):
    if tokens[idx].find("executed:") != -1:
      precent = float(tokens[idx].split(':')[1].split('%')[0]) / 100.0
      all_line = int(tokens[idx + 2])
      #total covered lines of code 单个测试用例所有被执行的行数
      all_line_count += math.ceil(precent*all_line) 


with open(str(gcov_path),'r') as f:
  lines = f.readlines()
  analysis_flag = False
  covered_line = 0
  target_line = 0 #可执行的行数
  #这里计算覆盖率是忽略那些注释行的
  #可能gcov原来统计覆盖率没有忽略注释，在这里返回重新计算的覆盖率covered_rate和gcov的数据算出来的被执行行数all_line_count
  for line in lines:
    if line.find("#####") == -1 and line.find("-:") == -1: #可执行且被覆盖的行
      target_line += 1
      covered_line += 1  # find executed lines begin with number: "6:"
    if line.find("#####") != -1 : #可执行但未被覆盖的行
      target_line += 1   # compute not coverd line in total
 
  covered_rate = covered_line / target_line * 100
  print(covered_rate,",",all_line_count)

