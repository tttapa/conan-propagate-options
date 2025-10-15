#include <iostream>
#include <libfoo/foo.hpp>

void foo() { std::cout << "foo" << std::endl; }

#ifdef FOO_WITH_V2
void foo_v2() { std::cout << "foo_v2" << std::endl; }
#endif
