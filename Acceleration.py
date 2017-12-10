#!/usr/bin/python3
v=25
u=0
t=10

print('We have,\n\tv = {} m/s\n\tu = {} m/s\n\tt = {} s'.format(v,u,t))

print('\tAcceleration(a)=?\nNow,\n\t   v = u + at\n\tOR,  a = (v-u) / t')

acc=(v-u)/t
print('\t     = ({}-{}) / {}\n\t     = {}'.format(v,u,t,acc))

print('\n Therefore, Acceleration = {} m/s\u00b2.'.format(acc))

print('Press enter any key to exit the program...',end='')
input()
exit()
