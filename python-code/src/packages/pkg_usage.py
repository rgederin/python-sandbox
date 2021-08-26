import pkg.mod1, pkg.mod2

pkg.mod1.foo()
pkg.mod2.bar()

from pkg.mod1 import foo
foo()

from pkg.mod2 import bar as qux
qux()

from pkg import mod1
mod1.foo()

from pkg import mod2 as quux
quux.bar()