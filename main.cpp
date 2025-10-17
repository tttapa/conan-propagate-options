#include <bar.hpp>
#include <foo.hpp>

int main() { return bar_get_foo() == foo ? 0 : 1; }
