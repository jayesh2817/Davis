import matplotlib.pyplot as plt
import numpy as np

# print(np.pi)
# print(np.sin(np.pi/2)) #sin
# print(np.cos(np.pi/2)) #cos
# print(np.tan(np.pi/2)) #tan
# print(1/np.cos(np.pi/4)) #sec
# print(1/np.sin(np.pi/4)) #cosec
# print(1/np.tan(np.pi/4)) #cot

# x = np.arange(1,11)
# y = np.arange(10,110,10)
# plt.figure(figsize=(4,5))
# plt.plot(x,y,'r--')
# plt.show()

# x_sin = np.arange(0, 2*np.pi, 0.1)
# y_sin = np.sin(x_sin)
# print(y_sin)

# plt.figure(figsize=(4,5))
# plt.plot(x_sin, y_sin, 'g--')
# plt.title('Sine Wave')
# plt.show()

# x_cos = np.arange(0, 2*np.pi, 0.1)
# y_cos = np.cos(x_cos)
# print(y_cos)

# plt.figure(figsize=(4,5))
# plt.plot(x_cos, y_cos, 'b--')
# plt.title('Cosine Wave')
# plt.show()

# x_tan = np.arange(0, 2*np.pi, 0.1)
# y_tan = np.tan(x_tan)
# print(y_tan)

# plt.figure(figsize=(4,5))
# plt.plot(x_tan, y_tan, 'm--')
# plt.title('Tan Wave')
# plt.show()

# # ----------- Added to fix the error -----------
# x_cot = np.arange(0, 2*np.pi, 0.1)
# y_cot = 1/np.tan(x_cot)
# print(y_cot)
# # ----------------------------------------------

# plt.figure(figsize=(4,5))
# plt.subplot(2,2,1)
# plt.plot(x_sin, y_sin, 'g--')
# plt.title('Sine Wave')

# plt.subplot(2,2,2)
# plt.plot(x_cos, y_cos, 'b--')
# plt.title('Cosine Wave')

# plt.subplot(2,2,3)
# plt.plot(x_tan, y_tan, 'm--')
# plt.title('Tan Wave')

# plt.subplot(2,2,4)
# plt.plot(x_cot, y_cot, 'r--')
# plt.title('Cot Wave')

# plt.show()

# print(np.random.random(1))
# print(np.random.random((1,10)))
# print(np.random.randint((1,10)))
# print(np.random.randint(1,10,(3,4,5)))
# print(np.random.rand(2,2))
# a=np.arange(1,11)
# print(a)
# print(np.random.choice(a))

s1="jayesh is my name"
s2="i am a student"

print(np.char.add(s1,s2))
print(np.char.upper(s1))
print(np.char.lower(s1))
print(np.char.split(s2))

s3="jayesh is my name\name"
print(np.char.splitlines(s3))

print(np.char.replace(s1,'jayesh','ram'))

print("*****goood bye*****")

print(np.char.center('good bye',50,'*'))
