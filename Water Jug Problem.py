# -*- coding: utf-8 -*-
"""AI-lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dfwUtNfKBDljcX-rke-rRkbb7cSCdCLB

Roll No.: 66

Name: Atharva Werulkar

Sem: 4th

Batch: E4

Lab-2

Aim:- Solve Water Jug Problem Using python
"""

capacityjug1= 4
capacityjug2= 3
jug1=0
jug2=0

def ruleEmpty(jug1,jug2):
  jug1 = 0
  jug2 = jug2
  return(jug1,jug2);

def rule2(jug1,jug2 ):
  jug1=jug1
  jug2=capacityjug2
  return (jug1,jug2)

def rule5(jug1,jug2 ):
  jug2= jug2 -(capacityjug1 - jug1)
  jug1 = jug1
  return(jug1,jug2)

def rule7(jug1,jug2 ):
  jug1 = jug1+jug2
  jug2=0
  return(jug1,jug2)

while (jug1!=2 and jug2!=2):

  (jug1,jug2)= rule2(jug1,jug2)
  print(jug1,jug2)

  (jug1,jug2)= rule7(jug1,jug2)
  print(jug1,jug2)

  (jug1,jug2)= rule2(jug1,jug2)
  print(jug1,jug2)

  (jug1,jug2)= rule5(jug1,jug2)
  print(jug1,jug2)

  (jug1,jug2)= ruleEmpty(jug1,jug2)
  print(jug1,jug2)

  (jug1,jug2)= rule7(jug1,jug2)
  print(jug1,jug2)