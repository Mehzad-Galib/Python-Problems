# opening a file and writing user input on it
opening_my_file = open('my_file.txt', 'w')

print('input something for the file')
input_user = input()

opening_my_file.write(input_user)

opening_my_file.close()

# opening the file for the second time to read the contents of the file

opening_my_file2 = open('my_file.txt', 'r')

content = opening_my_file2.read()

print(content)

opening_my_file2.close()

# opening the file for the third time to append some user contents into the file

opening_my_file3 = open('my_file.txt', 'a')

print('write more things for the file')
input_user2 = input()

opening_my_file3.write(input_user2)

opening_my_file3.close()

# opening the file for the fourth time to read the contents of the file 

opening_my_file_4 = open('my_file.txt', 'r');

content_2 = opening_my_file_4.read()

print(content_2)

opening_my_file_4.close()