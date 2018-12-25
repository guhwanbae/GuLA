CXX = g++
CXXFLAGS = -std=c++14 -W -Wall -O2

INCFLAGS = -I/usr/include/xtensor -I/usr/include/xtl -I/usr/include/xtensor-blas
LIBS = -lblas -llapack

SRCS = hello_xtensor.cc

TARGET = hello_xtensor

$(TARGET) :
	$(CXX) $(CXXFLAGS) $(INCFLAGS) $(SRCS) -o $(TARGET) $(LIBS) -DHAVE_CBLAS=1

clean :
	rm -f $(TARGET)


