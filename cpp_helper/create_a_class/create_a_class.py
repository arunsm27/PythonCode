#include <stdio.h>

with open("class.cpp", "w") as file:
    file.write("#include<iostream>\r\n")
    file.write("int main(int argc, char* argv[])\r")
    file.write("{ \r\n  std::cout << 'Hello World  ' << std::endl; \r\n");
    file.write("\r\n return (0);\r\n}\r")
    
    
    
    
    
