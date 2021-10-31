import csv
def write_into_csv(info_list):
    with open('student.csv','a',newline='')as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow("Name","Age","contact","-Mail")
        writer.writerow(info_list)
if __name__ == '__main__':
    condition= True
    while(condition):
        student=input("Enter student information in this format (Name,Age,Contact,Email id):")
        print("Entered informaton:"+student)
        student_list=student.split(' ')
        print("\nThe informations are:\nName:{}\nAge:{},\ncontact:{},\nE-Mail:{}"
              .format(student_list[0],student_list[1],student_list[2],student_list[3]))
        choice_check=input("Is the entered information correct?(yes/no):")
        if choice_check=="yes":
            write_into_csv(student_list)
            check=input("Enter (yes/no) if you want to enter information for another student:")
            if (check=="yes"):
                condition = True
            elif(check=="no"):
                condition = False
        elif choice_check=="no":
           print("\nPlease re-enter the information correctly")

