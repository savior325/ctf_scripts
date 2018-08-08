# encoding: UTF-8

file_reserve = open('d:/1.jpg', 'wb')
file_source = open('d:/columns.jpg', 'rb')
data = file_source.read()[::-1]
file_reserve.write(data)
file_reserve.close()
file_source.close()



