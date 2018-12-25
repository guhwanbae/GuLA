CXX = g++
CXXFLAGS = -std=c++11 -W -Wall -O2

INCFLAGS = -I/usr/local/include/eigen3

SRCS = hello_eigen.cc

TARGET = hello_eigen

$(TARGET) :
	$(CXX) $(CXXFLAGS) $(INCFLAGS) $(SRCS) -o $(TARGET)

clean :
	rm -f $(TARGET)


