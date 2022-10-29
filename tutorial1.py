

"""Midpoint"""
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 4))
plt.title("Midpoint Line Algorithm")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
def midpoint(ax, ay, bx, by):
  w = bx - ax
  h = by - ay
  F = (h-w)/2

  x = ax
  y = ay

  st.header(f"x = {x}, y = {y}")

  xcoordinates = [x]
  ycoordinates = [y]

  while(x<bx):
    x = x + 1
    if(F<0):
      F = F + h

    else: 
      F = F + (h-w)
      y = y + 1

    xcoordinates.append(x)
    ycoordinates.append(y)
    st.header(f"x = {x}, y = {y}")
    

  plt.plot(xcoordinates, ycoordinates)
  plt.show()
  st.pyplot(fig)

if __name__=="__main__":
  print("Enter the starting point of x: ")
  x1 = int(input())
  
  print("Enter the starting point of y: ")
  y1 = int(input())

  print("Enter the ending point of x: ")
  x2 = int(input())
  
  print("Enter the ending poing of y: ")
  y2 = int(input())

  midpoint(x1, y1, x2, y2)