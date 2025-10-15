#include <libfoo/foo.hpp>
#include <libwrapper/wrapper.hpp>

void wrap_foo() {
#ifdef FOO_WITH_V2
    foo_v2();
#else
    foo();
#endif
}
