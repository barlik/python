#include <iostream>
#include <math.h>

class Foo {
    public:
        void bar(){
            std::cout << "Hello" << std::endl;
        }
};

extern "C" {
    Foo* Foo_new(){ return new Foo(); }
    void Foo_bar(Foo* foo){ foo->bar(); }
}


extern "C" {
double square(int x, int y)
{
	return pow(x, y);
}
}

